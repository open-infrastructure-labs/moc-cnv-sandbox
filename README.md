# MOC CNV Sandbox

Configuration and documentation for the [CNV][] Sandbox at the [Mass Open Cloud][] (MOC).

[cnv]: https://www.redhat.com/en/resources/container-native-virtualization
[mass open cloud]: https://massopen.cloud/

## Playbooks

- `playbook-preinstall.yml`

  Set up provisioning host and generate the install configuration.

- `playbook-postinstall.yml`

  Fetches authentication credentials from the provisioning host and
  then uses the OpenShift API to perform post-configuration tasks
  (installing certificates, configuring SSO, installing CNV, etc).

## Encryption

Files with credentials and other secrets are encrypted using
[ansible-vault][]. The vault key itself is included in the repository and
is encrypted using GPG to the identities listed in the
[.vault_pgp_keys][] file.

[ansible-vault]: https://docs.ansible.com/ansible/latest/user_guide/vault.html
[.vault_pgp_eys]: .vault_pgp_keys

### Adding a new PGP key

1. Add the key fingerprint to `.vault_pgp_keys`.

   We use key fingerprints rather than email addresses to ensure that we
   are using the correct key (you may have multiple keys with the same
   email address in your keychain).

2. Run the `scripts/rekey-vault-secret.sh` script. This will decrypt the
   vault secret and then re-encrypt it to all the identities in the list.

### Updating the vault secret

If you want to replace the vault secret (e.g., you think the unencrypted
secret has been compromised):

1. Run the `scripts/rekey-vault-files.sh` script. This will generate a new
   random key, use `ansible-vault` to rekey all vaulted files with the new
   key, and then encrypt the key to the identities in `.vault_pgp_keys`.
