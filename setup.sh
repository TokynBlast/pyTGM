#!/bin/bash

if command -v apt-get >/dev/null; then
    sudo apt-get update && sudo apt-get install -y python3-dev
elif command -v dnf >/dev/null; then
    sudo dnf install -y python3-devel
elif command -v pacman >/dev/null; then
    sudo pacman -Sy --noconfirm python
elif command -v zypper >/dev/null; then
    sudo zypper install -y python3-devel
elif command -v brew >/dev/null; then
    brew install python
elif command -v pkg >/dev/null; then
    sudo pkg install -y python
elif command -v emerge >/dev/null; then
    sudo emerge --ask dev-lang/python
elif command -v apk >/dev/null; then
    sudo apk add --no-cache python3-dev
else
    echo "Unsupported package manager. Install Python development headers manually."
    exit 1
fi
