# Workflow Status

<!-- At some point, I will be adding a build bar -->
| **Linting** | [![C++ Lint](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml) | [![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml) | [![Isort](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml)
|-----------|----------|----------|----------|
| **Security** | [![Safety Linting](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml) | [![SHA256 Generate and Update](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml) | |

## Installing
To install, run ```pip install pyTGM```<br>
For sound, you will need libsoundio (For now)<br>
To install it, run the contents of setup.sh<br><br>
You will also need Python.h to build.<br>
You can get it from python3-dev<br><br>
On windows, you will need Visual Studio 2017 or later.<br>
When setting up Python, enable these (If applicable):
- Add Python to PATH
- Customize installation > Development Tools

On macOS, you will need homebrew to install Python.<br>

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
These are called escape sequences.
They can be combined with the library, to make the game even more powerful.

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

# Placing the cursor at a pair of coordinates
terminal.pos()

# Keyboard Press Detection
terminal.geky(times=1)

# Systematically print a rect
rect(width, height, time=3, character=" ")
```


## Sound Support
Works across Windows, macOS, and Linux:
```python
# Play audio file
sound.play('../sounds/mysound.mp3')

# Stop audio file
sound.stop('../sound/mysound.wav')
```
> [!NOTE]
> Sound is currently an experiment.
> We are looking for a way to hopefully eventually make sound play, without dependencies!

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
