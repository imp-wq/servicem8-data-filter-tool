#!/bin/bash

# Set this to your repo (e.g. username/repo)
REPO="imp-wq/your-repo"

# File with your secrets (key=value format)
SECRETS_FILE=".env"

while IFS='=' read -r key value; do
  if [[ ! -z "$key" ]]; then
    echo "Setting secret: $key"
    gh secret set "$key" -b"$value" --repo "$REPO"
  fi
done < "$SECRETS_FILE"
