#!/usr/bin/bash
# STACK_ID: io.wilsonfiy.stacks.ubuntu
# BASE_IMAGE: bpds/ubuntu-base:ubuntu
#

set -e

ID_PREFIX="io.wilsonfiy.stacks"
REPO_PREFIX=bpds/ubuntu
PLATFORM=amd64
DIR=$(pwd)
IMAGE_DIR=$(realpath ".")
TAG=$(basename "${IMAGE_DIR}")
STACK_ID="${ID_PREFIX}.${TAG}"
BASE_IMAGE=${REPO_PREFIX}-base:${TAG}
RUN_IMAGE=${REPO_PREFIX}-run:${TAG}
BUILD_IMAGE=${REPO_PREFIX}-build:${TAG}

echo "start Stack ID: ${STACK_ID}"

echo "start BUILDING ${BASE_IMAGE}..."
docker build --platform=${PLATFORM} --tag "${BASE_IMAGE}" "${IMAGE_DIR}/base"
echo "done BUILDING ${BASE_IMAGE}"

echo "start BUILDING ${BUILD_IMAGE}..."
docker build --platform=${PLATFORM} --build-arg "base_image=${BASE_IMAGE}" --build-arg "stack_id=${STACK_ID}" --tag "${BUILD_IMAGE}" "${IMAGE_DIR}/builder"
echo "done BUILDING ${BUILD_IMAGE}"

echo "start BUILDING ${RUN_IMAGE}..."
docker build --platform=${PLATFORM} --build-arg "base_image=${BASE_IMAGE}" --build-arg "stack_id=${STACK_ID}" --tag "${RUN_IMAGE}" "${IMAGE_DIR}/run"
echo "done BUILDING ${RUN_IMAGE}"

echo "done Stack ID: ${STACK_ID}"
echo "Images:"
echo "${BASE_IMAGE}" 
echo "${BUILD_IMAGE}"
echo "${RUN_IMAGE}"