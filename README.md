# Workflow Status
[![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml)<br>
[![Python application](https://github.com/TokynBlast/pyTGM/actions/workflows/python-app.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/python-app.yml)<br>
[![SHA3-256 Generate and Update](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml)<br>
[![Upload Python Package](https://github.com/TokynBlast/pyTGM/actions/workflows/python-publish.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/python-publish.yml)

# pyTGM (Python Terminal Game Maker)

>[!NOTE]
> There was an accidental deletion of the original pyTGM library. This is an updated version of the newest version I had on hand.
>
>This note will be deleted in the next version.

>[!NOTE]
>This will be uploaded to PyPi, the latest by December 17, 2024 PT

pyTGM is a simplified alternative to Pygame, focusing on ASCII and ANSI based game development, with utilities for encryption, randomization, and more.

## Features

### File Operations
```python
file.read.document(name)           # Read entire file
file.read.line(name, line=0)       # Read specific line
```

### Graphics and Text Styling
```python
# Clear screen
graphics.cls()

# Color text (RGB)
graphics.color(0, 255, 0)  # Green text
graphics.res               # Reset color

# Markup
graphics.bold
graphics.italic
graphics.underline
```

### Sound Support
Works across Windows, macOS, and Linux:
```python
# Play audio file
play('../sounds/mysound.mp3')

# Make a file of a frequency
generate(frequency, duration, name, sample_rate=44100, volume=0.5)
```

### Local Server Support
```python
# Starting a server and client (PORT, message)
LocalServer(1080, {'MarkTheMight':((243,332), 57)})
```
An example of a returned value would be:
```python
{'LordMinion777':((0,0), 100), 'Muyskerm':((245,334), 43)}
```

### Terminal Input Detection
```python
# Mouse Click Detection
terd.click()             # Returns coordinates, (-1,-1) means error in press

# Keyboard Press Detection
geky(times)
```

### Encryption
```
# Set the table
b64.Table.table_ = 'ABCDEF...XYZ...12...90...!@..._+' # Make sure it has character that will be used, special chars are also usable
b64.Table.gen('ABCDEF...XYZ...12...90...!@..._+', 32)

# Encode and decode
b64.encode(text)
b64.decode(text)
```

## Links
- [Homepage](https://pytgm.tokynblast.space/home)
- [Documentation](https://pytgm.tokynblast.space/documentation/use)
- [Source Code](https://github.com/TokynBlast/pyTGM/tree/main)
- [Bug Tracker](https://github.com/TokynBlast/pyTGM/issues)
- [Changelog](https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt)

## License
pyTGM is licensed under Bspace, created by Tokyn Blast.
