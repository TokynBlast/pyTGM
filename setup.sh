# Build pyTGM

if !command -v python3 >/dev/null; then
    echo "Python 3 is not installed."
else
    if !command -v pip list nanobind wheel setuptools >/dev/null; then
        echo "One of the following:\n     wheel\n     setuptools\n     nanobind\nis not installed.\nPython will install it automatically.\n\n"
    fi
    echo "Compiling and installing pyTGM..."
    python3 setup.py sdist
    python3 -m pip install dist/*
fi