#!/bin/bash

: ${VAULT_PGP_KEYS:=.vault_pgp_keys}

set -e

# read list of key fingerprints from .vault_pgp_keys
fingerprints=( $(awk '! /^#|^$/ {print $1}' ${VAULT_PGP_KEYS}) )

# build a list of "-r <recipient>" arguments for gpg
recipients=()
for fp in "${fingerprints[@]}"; do
	recipients+=(-r "$fp")
done

# run the command line (read from stdin, write to stdout)
gpg --batch --encrypt --armor "${recipients[@]}"
