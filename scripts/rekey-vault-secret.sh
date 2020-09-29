#!/bin/sh

: ${VAULT_SECRET:=.vault_secret}

tmpfile=$(mktemp ./.keyXXXXXX)
trap "rm -f $tmpfile" EXIT

set -e

# decrypt vault secret and re-encrypt it using current list of
# pgp fingerprints
gpg --batch --decrypt "$VAULT_SECRET" |
	./scripts/encrypt-to-vault-pgp-keys.sh > $tmpfile
mv $tmpfile "$VAULT_SECRET"
