if command -v apt-get >/dev/null; then
    sudo apt-get update && sudo apt-get install -y python3-dev cmake
elif command -v dnf >/dev/null; then
    sudo dnf install -y python3-devel cmake
elif command -v pacman >/dev/null; then
    sudo pacman -Sy --noconfirm python cmake
elif command -v zypper >/dev/null; then
    sudo zypper install -y python3-devel cmake
elif command -v brew >/dev/null; then 
    brew install python cmake
elif command -v pkg >/dev/null; then
    sudo pkg install -y python cmake
elif command -v emerge >/dev/null; then
    sudo emerge --ask dev-lang/python dev-util/cmake
elif command -v apk >/dev/null; then
    sudo apk add --no-cache python3-dev cmake
elif command -v winget >/dev/null; then
    winget install --silent Python.Python.3 CMake
elif command -v choco >/dev/null; then
    choco install -y python cmake
elif command -v scoop >/dev/null; then
    scoop install python cmake
elif [[ "$OS" == "Windows_NT" ]]; then
    echo "Your on Windows!\nPlease install Python dev and CMake manually."
    exit 1
else 
    echo "Unsupported package manager. Install Python dev headers and CMake manually."
    exit 1
fi
