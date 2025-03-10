# Workflow Status

<!-- Eventually, it will be |linting|security|build| -->
| **Linting** | [![C++ Lint](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml) | [![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml) | [![Isort](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml)
|-----------|----------|----------|----------|
| **Security** | [![Safety Linting](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml) | [![SHA256 Generate and Update](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml) | |
| **Build** |[![Compile C++](https://github.com/TokynBlast/pyTGM/actions/workflows/compile.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/compile.yml)| | |

> [!warning]
> The source code is currently very error prone.

## Installing
To install, run ```pip install pyTGM```<br>
All versions before 5.0.0 must be built from source.<br>
macOS is still built from source<br><br>
You will need pybind11, setuptools and wheel.<br>
There are some things for building, that are needed, which can be removed afterwards.<br>
Run setup.sh to install the materials for it.<br><br>
You will also need Python.h to build.<br>
You can get it from python3-dev<br><br>
On windows, you will need Visual Studio 2017 or later.<br>
When setting up Python, enable these (If applicable):
- Add Python to PATH
- Customize installation > Development Tools

On Linux, your OS will change the command you need to run, I have curated a command, to detect the OS and install it:<br>
```
bash -c 'if command -v apt-get >/dev/null; then sudo apt-get update && sudo apt-get install -y python3-dev elif command -v dnf >/dev/null; then sudo dnf install -y python3-devel elif command -v pacman >/dev/null; then sudo pacman -Sy --noconfirm python elif command -v zypper >/dev/null; then sudo zypper install -y python3-devel elif command -v brew >/dev/null; then brew install python elif command -v pkg >/dev/null; then sudo pkg install -y python elif command -v emerge >/dev/null; then sudo emerge --ask dev-lang/python elif command -v apk >/dev/null; then sudo apk add --no-cache python3-dev else echo "Unsupported package manager. Install Python dev headers manually." exit 1 fi'
```

# pyTGM (Python Terminal Game Maker)

pyTGM is a simplified alternative to Pygame, focusing on ASCII and ANSI based game development, contained completley within the terminal,<br>
with utilities for encryption, markup, sound playing, servers, and much more.

## Bugs and Features
To report a bug, go [here](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=)<br>
For feature request, go [here](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=)<br>
To report a compile error/warning, go [here](https://github.com/TokynBlast/pyTGM/issues/new?template=compile_report.md)

## Contributing
All contributions are greatly appreciated.<br>
To make a contribution, make a new branch [here](https://github.com/TokynBlast/pyTGM/branches)<br>
Then, add (or remove), to improve the repo!<br>
Once we know it's working and safe, somebody will merge the request!

# Suggestions
You don't always need everything for this library.
Some things, like a beep can be used with \a
These are called escape sequences./n
They can be combined with the library, to make the game even more powerful./n
In fact, that's what pyTGM does! It just provides an easier interface, to interact with these escape sequences!

# Features

## Terminal
```python
# Clear screen
terminal.cls()

# Color text (RGB)
terminal.color(0, 255, 0)  # Green text
terminal.RESET             # Reset color

# Markup
terminal.BOLD
terminal.ITALIC
terminal.UNDERLINE

# Keyboard Press Detection
terminal.geky(times=1)

# Systematically print a rect
rect(width, height, time=3, character=" ")
```


## Sound Support
Works across Windows, macOS, and Linux:
```python
# Play audio file
sound('../sounds/mysound.mp3')
```

## Local Server Support
```python
# Starting a server and client (PORT, message)
LocalServer(1080, {'MarkTheMighty':((243,332), 57)})
```
An example of a returned value would be:
```python
{'LordMinion777':((0,0), 100), 'Muyskerm':((245,334), 43)}
```

## Encryption

### b64:
```python
# Set the table
encrypt.b64.Table.table = 'ABCDEF...XYZ...12...90...!@..._+'
encrypt.b64.Table.generate('ABCDEF...XYZ...12...90...!@..._+', 32)  # (table: str, times: int)

# Encode and decode
encrypt.b64.encode(text)
encrypt.b64.decode(text)
```
When setting the table, it MUST include the characters that are being stored at the very least!
Extra characters are suggested for security.
```python
encrypt.sha256(text)
```


### hk512:
```python
encrypt.hk512.encode(data, key)
encrypt.hk512.decode(data, key)
```

## Links
- [Homepage](https://pyTGM.tokynblast.space/home)
- [Documentation](https://pyTGM.tokynblast.space/documentation/use)
- [Source Code](https://github.com/TokynBlast/pyTGM/tree/main)
- [Bug Tracker](https://github.com/TokynBlast/pyTGM/issues)
- [Changelog](https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt)

## License
pyTGM is licensed under Bspace, created by Tokyn Blast.
