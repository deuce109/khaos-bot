#!/bin/sh

if [ -f /etc/alpine-release ]; then
    PLATFORM="alpine"
elif [ -f /etc/lsb-release ]; then
    PLATFORM="debian"
elif [ -f /etc/debian_version ]; then
    PLATFORM="debian"
elif [ -f /etc/redhat-release ]; then
    PLATFORM="fedora"
elif [ -f /etc/SuSE-release ]; then
    PLATFORM="suse"
elif [ -f /etc/gentoo-release ]; then
    PLATFORM="gentoo"
elif [ -f /etc/arch-release ]; then
    PLATFORM="arch"
else
    exit 1
fi

echo "${PLATFORM}"