# OpenShift IPI Installation notes

## Hardware configuration

### Boot mode

All hardware must be configured to boot in UEFI mode. On the Dell
nodes I'm working with, this is `System BIOS -> Boot Settings -> Boot
Mode`.

### Solarflare NICs

The hardware we're using has Solarflare 10Gb NICs. I had to reset all
the NICs to their default configuration in order to support network
booting.

### PXE booting issues

One node does not reliably PXE boot when requested via `ipmitool`. We can work
around this by running `wipefs -fa /dev/sda` on the node prior to a reinstall,
which wipes the boot record in order to prevent it from booting from the local
disk.

This may be a BIOS configuration issue, but I haven't yet spotted the problem.

## Networking issues

We had the following requirements for our OpenShift install:

- Hosts are not connected directly to the IPMI network. They require a
  static route to reach that network.

- The IPMI network is not generally accessible. We require an explicit
  firewall exception for each host that requires access to the IPMI
  network.

The above requirements conflict with the use of a bootstrap vm. Because the
bootstrap vm has an unknown MAC address, it's not possible to create a static
configuration for it in the DHCP server.  This means that:

- We can't assign it a static ip address
- We can't assign it a static route via dhcp (unless we want to
  publish that static route to *all* hosts on the same network)
- Because we can't assign it a static address, we can't create a firewall
  exception for it

### Solution 1: Static configuration via ignition profile

Ian (`ipilcher`) suggested that we could embed a static network
configuration via the Ignition profile. Unfortunately, the ignition
profile is fetched only *after* the system has initially configured
the interfaces, which requires DHCP.

### Solution 2: Static lease using a wildcard MAC address

If the bootstrap vm is the *only* libvirt vm booting on the network,
we can provide a static lease in the [dnsmasq][] configuration by using
wildcards in the MAC address, like this:

```
dhcp-host=52:54:00:*:*:*,192.12.185.107,bootstrap.cnv.massopen.cloud
```

Because this will match *anything* that looks like a libvirt MAC
address, we won't be able to use it with multiple bootstrap vms
running on the same network.

### Solution 3: Small dynamic address range

If we are confident that most hosts on the public network are not
attempting to configure interfaces using DHCP, we can create a small
dynamic range to be used by the bootstrap vms, for example:

```
dhcp-range=192.12.185.130,192.12.185.135,255.255.255.0
```

This may erroneously hand out leases to hosts we weren't expecting to
configure, but arguably that represents a configuration problem on the
affected host.

If we wanted to, we could restrict this dynamic range to libvirt vms:

```
dhcp-host=52:54:00:*:*:*,set:libvirt
dhcp-range=tag:libvirt,192.12.185.130,192.12.185.135,255.255.255.0
dhcp-range=192.12.185.0,static,255.255.255.0
```

We would need to create firewall exceptions for all addresses in this
range, which has security implications.

### Solution 4: Custom boot image

The default RHCOS boot image relies on DHCP to configure network
interfaces. We can build a custom image that assigns a static ip
instead.

The process looks like this:

- Fetch the original RHCOS compressed image
- Uncompress the image
- Use `virt-edit` (or `guestfish`, etc) to edit the grub configuration
  (`/dev/sda1:/grub2/grub.cfg`) to replace the `ip=dhcp,dhcp6` kernel
  command line option with the necessary options to set a static
  network configuration:

    - `ip` for setting interface addresses
    - `nameserver` for setting nameserver entries
    - `rd.route` for setting a static route

    I used the following command line to make these changes:

    ```
    virt-edit -a $CUSTOM_IMAGE -m /dev/sda1 \
    -e "s|ip=dhcp,dhcp6|ip=128.31.28.94::128.31.28.1:255.255.255.0::ens3:off ip=172.22.0.2:::255.255.255.0::ens4:off nameserver=128.31.24.12 nameserver=128.31.24.11 rd.route=10.0.0.0/19:128.31.28.16|g" \
    /grub2/grub.cfg
    ```
- Compress the updated image
- Generate the `sha256` checksum of the image
- Update `install_config` to point at the new image by setting the 
  `bootstrapOSImage` option (this option is documented in
  [section
  7.2](https://openshift-kni.github.io/baremetal-deploy/4.4/Deployment.html#additional-install-config-parameters_ipi-install-prerequisites).

Creating a custom image has the advantage of working around most of
the network related issues.

In order to use the custom image, you'll need to run a local http server to make the image available to the install process. "[Creating an RHCOS iamges cache](https://openshift-kni.github.io/baremetal-deploy/4.4/Deployment.html#ipi-install-creating-an%20rhcos-images-cache_ipi-install-prerequisites) suggests one option for doing this.

Ian provided [this
example](https://github.com/schmaustech/ocp-auto/blob/master/jumphost/rhcos-refresh.sh)
of a script that creates a customized RHCOS image.

[dnsmasq]: http://www.thekelleys.org.uk/dnsmasq/doc.html
