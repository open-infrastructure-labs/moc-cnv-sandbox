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

- `playbook-postinstall.yml`

  This playbook fetches authentication credentials from the
  provisioning host and then uses the OpenShift API to perform
  post-configuration tasks (installing certificates, configuring SSO,
  installing CNV, etc).

## See also

- [Getting started with OpenShift and CNV](https://gitlab.com/open-infrastructure-labs/moc-cnv-sandbox/-/tree/docs)

  (Available in the `docs` branch of this repository)
