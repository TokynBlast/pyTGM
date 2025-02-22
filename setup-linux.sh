# Build pyTGM from source on Linux

if command -v apt-get >/dev/null; then
    sudo apt-get update && sudo apt-get install -y python3-dev cmake
elif command -v dnf >/dev/null; then
    sudo dnf install -y python3-devel cmake
elif command -v pacman >/dev/null; then
    sudo pacman -Sy --noconfirm python cmake
elif command -v zypper >/dev/null; then
    sudo zypper install -y python3-devel cmake
elif command -v pkg >/dev/null; then
    sudo pkg install -y python cmake
elif command -v emerge >/dev/null; then
    sudo emerge --ask dev-lang/python dev-util/cmake
elif command -v apk >/dev/null; then
    sudo apk add --no-cache python3-dev cmake
else 
    echo "Unsupported package manager. Install Python dev headers, CMake, and optionally Ninja manually."
    exit 0
fi