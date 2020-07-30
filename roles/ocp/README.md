## OpenShift API Roles

The roles in this directory make configuration changes in OpenShift using
Ansible's [k8s][] module.

## Roles

[k8s]: https://docs.ansible.com/ansible/latest/modules/k8s_module.html

- `api`

  Library role used by other roles for common operations.

- `authz`

  Ensure that users cannot create resources without being added to an
  `approved-users` group.

- `cnv`

  Install and configure the [CNV][] operator.

- `default-ingress-certificate`

  Update the default ingress certificate [1][].

  [1]: https://docs.openshift.com/container-platform/4.4/security/certificates/replacing-default-ingress-certificate.html

- `firewall`

  Create firewall rules to block traffic from another OpenShift
  cluster operating on the same network. This caused issues under
  OpenShift 4.4 but is probably unnecessary with 4.5.x.

- `hostpath`

  Configure the hostpath provisioner.

- `lso`

  Install and configure the [Local Storage Operator][lso]

- `moc-sso`

  Configure SSO using MOC keycloak instance.

- `public-net`

  Create a bridged network for the public ("baremetal") interface.

[cnv]: https://docs.openshift.com/container-platform/4.4/security/certificates/replacing-default-ingress-certificate.html
[lso]: https://docs.openshift.com/container-platform/4.5/storage/persistent_storage/persistent-storage-local.html
