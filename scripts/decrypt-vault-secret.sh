#!/bin/sh

: ${VAULT_SECRET:=.vault_secret}
gpg --batch --decrypt "$VAULT_SECRET"
