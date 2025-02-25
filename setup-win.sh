# Build pyTGM on Windows

if command -v winget >/dev/null; then
    winget install --silent Python.Python.3 CMake
elif command -v choco >/dev/null; then
    choco install -y python cmake
elif command -v scoop >/dev/null; then
    scoop install python cmake
elif [[ "$OS" == "Windows_NT" ]]; then
    echo "No package manager detected. Install Python, CMake, and optionally Ninja manually from their official websites."
    exit 0
else 
    echo "Unsupported package manager. Install Python dev headers, CMake, and optionally Ninja manually."
    exit 0
fi
