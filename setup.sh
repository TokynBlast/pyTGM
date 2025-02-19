#!/bin/bash

if command -v apt-get >/dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3-dev libsoundio-dev
elif command -v dnf >/dev/null; then
    sudo dnf install -y python3-devel libsoundio-devel
elif command -v pacman >/dev/null; then
    sudo pacman -Sy --noconfirm python libsoundio
elif command -v zypper >/dev/null; then
    sudo zypper install -y python3-devel libsoundio-devel
elif command -v brew >/dev/null; then
    brew install python libsoundio
elif command -v pkg >/dev/null; then
    sudo pkg install -y python libsoundio
elif command -v emerge >/dev/null; then
    sudo emerge --ask dev-lang/python media-libs/libsoundio
elif command -v apk >/dev/null; then
    sudo apk add --no-cache python3-dev libsoundio-dev
else
    echo "Unknown package manager. Please install Python development headers and libsoundio manually."
    exit 1
fi
