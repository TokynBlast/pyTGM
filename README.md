# Workflow Status
### Python
[![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml)<br>
[![Lint with Isort](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml)<br>
[![Safety Linting](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml)<br>
[![SHA256 Generate and Update](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml)<br>

### C++
[![C++ Linting](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml)


# pyTGM (Python Terminal Game Maker)

pyTGM is a simplified alternative to Pygame, focusing on ASCII and ANSI based game development, contained completley within the terminal,<br>
with utilities for encryption, markup, mouse input, and much more.

To download pyTGM using pip, run ```pip install pyTGM```<br>
**THE NAME IS CASE-SENSETIVE**

It is **NOT** recommended that you download earlier than 4.1.0; Earlier than this, importing was untested!<br>
Amongst other things, all previous versions were built for windows only.<br>
4.1.0 fixes this.

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
