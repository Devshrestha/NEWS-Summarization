#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Define some environement variables
#  Automatic export to the environment of subsequently executed commands
# source: the command 'help export' run in Terminal
export IMAGE_NAME="api-server"
export BASE_DIR=$(pwd)
export PERSISTENT_DIR=$(pwd)/../persistent-folder/
export PERSISTENT_DIR=$(pwd)/../persistent-folder/
export SECRETS_DIR=$(pwd)/../secrets/
export GCP_PROJECT="AI5-c3-group10"
export GCP_ZONE="asia "
export GOOGLE_APPLICATION_CREDENTIALS=/secrets/sevice_acc_key.json

# Build the image based on the Dockerfile
docker build -t $IMAGE_NAME -f Dockerfile .

# Create the container
# --mount: Attach a filesystem mount to the container
# -p: Publish a container's port(s) to the host (host_port: container_port) (source: https://dockerlabs.collabnix.com/intermediate/networking/ExposingContainerPort.html)
# -e: set environment variables
docker run --rm --name $IMAGE_NAME -ti \
--mount type=bind,source="$BASE_DIR",target=/app \
--mount type=bind,source="$PERSISTENT_DIR",target=/persistent \
--mount type=bind,source="$SECRETS_DIR",target=/secrets \
-p 9000:9000 \
-e GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS \
-e GCP_PROJECT=$GCP_PROJECT \
-e GCP_ZONE=$GCP_ZONE \
-e DEV=1 $IMAGE_NAME