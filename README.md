# Workflow Status
[![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml)<br>
[![Lint with Isort](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml)<br>
[![Safety Linting](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml)<br>
[![SHA256 Generate and Update](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml)<br>
![Static Badge](https://img.shields.io/badge/C%2B%2B%20Linting-passing-lime_green)

> [!NOTE]
> gon will likely be added later or never.

<sub>Development is now up to the community. I have started the project, and now it's up to others to continue.<br>I have moved to other projects, and will occasionally update the program.</sub>

From now on, TokynBlast will only accept changes and fix found bugs.
The rest is up to the community...
TokynBlast has a bunch of other projects, and wants to expand outside of GitHub.
He is currently making sites. (FCFS basis!)
TokynBlast is working with a good friend.
Eventuall, he will come back here, and projects will occasionallybe updated!

The C++ linting badge isnt Github made, because I look for certain errors, and report back to here if it worked or not.<br>
Clang Tidy doesn't know how it should work.

## Installing
To install, run ```pip install pyTGM```<br>
You may need Python3-dev. (Python.h)<br>
You need Microsoft Visual Studio on Windows.
When setting up Python, enable these (If applicable):
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

## Bugs and Features
To report a bug, go [here](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=)<br>
For feature request, go [here](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=)

## Contributing
All contributions are greatly appreciated.<br>
To make a contribution, make a new branch [here](https://github.com/TokynBlast/pyTGM/branches)<br>
Then, add (or remove), to improve the repo!<br>
Once we know it's working and safe, somebody will merge the request!

# Suggestions
You don't always need everything for this library.
Some things, like a beep can be used with \a
These are called escape sequences.
They can be combined with the library, to make the game even more powerful.

# Features

## File Operations
```python
file.line(name, line, text)           # Modify a single line of a file
file.patt(name, pattern, replacement)     # Replace a pattern of text in a file
```

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

# Placing the cursor at a pair of coordinates
terminal.pos()

# Mouse Click Detection
terminal.click()             # A return value of (-1, -1) means the click was invalid

# Keyboard Press Detection
terminal.geky(times)
```


## Sound Support
Works across Windows, macOS, and Linux:
```python
# Play audio file
psound('../sounds/mysound.mp3')
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


### SHA256:
```python
encrypt.sha256(text)
```


### hk512:
```python
exncrypt.hk512.encode(data, key)
exncrypt.hk512.decode(data, key)
```

## Links
- [Homepage](https://pytgm.tokynblast.space/home)
- [Documentation](https://pytgm.tokynblast.space/documentation/use)
- [Source Code](https://github.com/TokynBlast/pyTGM/tree/main)
- [Bug Tracker](https://github.com/TokynBlast/pyTGM/issues)
- [Changelog](https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt)

## License
pyTGM is licensed under Bspace, created by Tokyn Blast.
