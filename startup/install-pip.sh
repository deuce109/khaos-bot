#!/bin/sh

PLATFORM=`sh ./detect-os.sh`

case "$PLATFORM" in
    "debian")
        apt-get update
        apt-get install -y python3-pip
        ;;
    "ubuntu")
        apt-get update
        apt-get install -y python3-pip
        ;;
    "centos")
        yum install -y python3-pip
        ;;
    "fedora")
        dnf install -y python3-pip
        ;;
    "alpine")
        apk add python3 py3-pip
        ;;
    *)
        echo "Unknown platform: ${PLATFORM}"
        exit 1
        ;;
esac