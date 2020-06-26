# MOC CNV Sandbox

Configuration and documentation for the [CNV][] Sandbox at the [Mass Open Cloud][] (MOC).

[cnv]: https://www.redhat.com/en/resources/container-native-virtualization
[mass open cloud]: https://massopen.cloud/

## Playbooks

- `playbook.yml`

  Set up provisioning host and generate the install configuration.

- `playbook-nameservers.yml`

  Set up DNS/DHCP/PXE servers for the openshift environment.

- `playbook-conserver.yml`

  Set up a console server for convenient access to IPMI serial consoles.

- `playbook-ssh-keys.yml`

  Install ssh keys on openshift hosts.

## Post install configuration

- `00-cnv.yml`

  Create CNV deployment.

- `01-hostpath-provisioner-dir.yml`

  Create machineconfig that ensures /srv/local-storage exists
  and has an appropriate selinux context.

- `02-hostpath-provisioner.yml`

  Create hostpath provisioner deployment.

- `03-hostpath-provisioner-storageclass.yml`

  Create hostpath provisioner storage class.

## See also

- [Networking with nmstate](https://docs.openshift.com/container-platform/4.4/cnv/cnv_node_network/cnv-observing-node-network-state.html)
