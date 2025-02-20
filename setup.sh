read -p "Do you want to install Ninja too? [Y/n] " nin

if command -v apt-get >/dev/null; then
    sudo apt-get update && sudo apt-get install -y python3-dev cmake
    [[ "$nin" =~ ^[Yy]$ ]] && sudo apt-get install -y ninja-build
elif command -v dnf >/dev/null; then
    sudo dnf install -y python3-devel cmake
    [[ "$nin" =~ ^[Yy]$ ]] && sudo dnf install -y ninja-build
elif command -v pacman >/dev/null; then
    sudo pacman -Sy --noconfirm python cmake
    [[ "$nin" =~ ^[Yy]$ ]] && sudo pacman -Sy --noconfirm ninja
elif command -v zypper >/dev/null; then
    sudo zypper install -y python3-devel cmake
    [[ "$nin" =~ ^[Yy]$ ]] && sudo zypper install -y ninja
elif command -v brew >/dev/null; then 
    brew install python cmake
    [[ "$nin" =~ ^[Yy]$ ]] && brew install ninja
elif command -v pkg >/dev/null; then
    sudo pkg install -y python cmake
    [[ "$nin" =~ ^[Yy]$ ]] && sudo pkg install -y ninja
elif command -v emerge >/dev/null; then
    sudo emerge --ask dev-lang/python dev-util/cmake
    [[ "$nin" =~ ^[Yy]$ ]] && sudo emerge --ask dev-util/ninja
elif command -v apk >/dev/null; then
    sudo apk add --no-cache python3-dev cmake
    [[ "$nin" =~ ^[Yy]$ ]] && sudo apk add --no-cache ninja
elif command -v winget >/dev/null; then
    winget install --silent Python.Python.3 CMake
    [[ "$nin" =~ ^[Yy]$ ]] && winget install --silent Kitware.Ninja
elif command -v choco >/dev/null; then
    choco install -y python cmake
    [[ "$nin" =~ ^[Yy]$ ]] && choco install -y ninja
elif command -v scoop >/dev/null; then
    scoop install python cmake
    [[ "$nin" =~ ^[Yy]$ ]] && scoop install ninja
elif [[ "$OS" == "Windows_NT" ]]; then
    echo "No package manager detected. Install Python, CMake, and optionally Ninja manually from their official websites."
    exit 1
else 
    echo "Unsupported package manager. Install Python dev headers, CMake, and optionally Ninja manually."
    exit 1
fi
