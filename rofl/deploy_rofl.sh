#!/usr/bin/env bash
set -euo pipefail
APP_NAME="tee-trivia-tower"
IMAGE="ttl-rofl:latest"

docker build -t "$IMAGE" .
echo "🛠  Image built as $IMAGE"

# Register with Oasis Testnet (assumes oasis-cli inside dev container or host)
oasis rofl register \
  --name "$APP_NAME" \
  --image "$IMAGE" \
  --network testnet \
  --provider default

echo "✅  Registered. Grab TEST tokens at https://faucet.testnet.oasis.io/ if needed."
