# Workflow Status
[![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml)<br>
[![Lint with Isort](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml)<br>
[![Safety Linting](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml)<br>
[![SHA256 Generate and Update](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml)<br>
![Static Badge](https://img.shields.io/badge/C%2B%2B%20Linting-passing-lime_green)



C++ Linting isnt Github made, because I look for certain errors, and report back to here if it worked or not.<br>
Clang Tidy doesn't know how it should work.

## Installing
To install, run ```pip install pyTGM```<br>
You may need Python3-dev.
You need Microsoft Visual Studio<br>
When setting up Python, enable these:
- Add Python to PATH
- Customize installation > Development Tools

On macOS, you will need homebrew to install Python:<br>
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Then, run<br>
```
brew install python
```

On Linux, your OS will change the command you need to run:<br>
Debian/Ubuntu:
```
sudo apt-get update; sudo apt-get install -y python3-dev
```

Fedora:
```
sudo dnf install -y python3-devel
```

Arch linux:
```
sudo pacman -S python
```

Dont know what OS you have?
Run this command:
```
bash -c 'if command -v apt-get >/dev/null; then sudo apt-get update && sudo apt-get install -y python3-dev; elif command -v dnf >/dev/null; then sudo dnf install -y python3-devel; elif command -v pacman >/dev/null; then sudo pacman -Sy python; elif command -v zypper >/dev/null; then sudo zypper install -y python3-devel; else echo "Unsupported package manager. Install Python dev headers manually."; exit 1; fi'
```

# pyTGM (Python Terminal Game Maker)

pyTGM is a simplified alternative to Pygame, focusing on ASCII and ANSI based game development, contained completley within the terminal,<br>
with utilities for encryption, markup, mouse input, and much more.

It is **MOST** reccomended, that you download the latest version!

## Bugs and Features
To report a bug, go [here](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=)<br>
For feature request, go [here](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=)

## Contributing
All contributions are greatly appreciated.<br>
To make a contribution, make a new branch [here](https://github.com/TokynBlast/pyTGM/branches)<br>
Then, add (or remove), to improve the repo!<br>
Once we know it's working and safe, somebody will merge the request!

## Features

### File Operations
```python
file.fm_line(name)           # Modify a line of a file
```

### Graphics and Text Styling
```python
# Clear screen
graphics.cls()

# Color text (RGB)
graphics.color(0, 255, 0)  # Green text
graphics.RESET             # Reset color

# Markup
graphics.BOLD
graphics.ITALIC
graphics.UNDERLINE

# Placing the cursor at a pair of coordinates
graphics.pos()
```


### Sound Support
Works across Windows, macOS, and Linux:
```python
# Play audio file
psound('../sounds/mysound.mp3')
```

### Local Server Support
```python
# Starting a server and client (PORT, message)
LocalServer(1080, {'MarkTheMighty':((243,332), 57)})
```
An example of a returned value would be:
```python
{'LordMinion777':((0,0), 100), 'Muyskerm':((245,334), 43)}
```

### Terminal Input Detection
```python
# Mouse Click Detection
terd.click()             # A return value of (-1, -1) means the click was invalid!

# Keyboard Press Detection
terd.geky(times)
```

### Encryption
```python
# Set the table
b64.Table.table = 'ABCDEF...XYZ...12...90...!@..._+'
b64.Table.generate('ABCDEF...XYZ...12...90...!@..._+', 32)  # (table: str, times: int)

# Encode and decode
b64.encode(text)
b64.decode(text)
```
When setting the table, it MUST include the characters that are being stored at the very least!
Extra characters are suggested for security.

## Links
- [Homepage](https://pytgm.tokynblast.space/home)
- [Documentation](https://pytgm.tokynblast.space/documentation/use)
- [Source Code](https://github.com/TokynBlast/pyTGM/tree/main)
- [Bug Tracker](https://github.com/TokynBlast/pyTGM/issues)
- [Changelog](https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt)

## License
pyTGM is licensed under Bspace, created by Tokyn Blast.
