#!/bin/sh

: ${VAULT_SECRET:=.vault_secret}

tmpfile=$(mktemp .keyXXXXXX)
trap "rm -f $tmpfile" EXIT

set -e

# generate a new key in a temporary file
openssl rand 512 > $tmpfile

# rekey all existing vaulted files. this reads files using the existing
# key and re-encrypts them using the new key.
find group_vars/ -type f -exec grep -ql '^$ANSIBLE_VAULT;' {} \;  -print0 |
	xargs -0 ansible-vault rekey --new-vault-password-file $tmpfile 

# encrypt the key, replacing .vault_secret
./scripts/encrypt-to-vault-pgp-keys.sh < $tmpfile > "${VAULT_SECRET}"
