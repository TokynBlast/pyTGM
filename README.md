# Workflow Status
## Linting
[![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml)<br>
[![Lint with Isort](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml)<br>
## Security
[![Safety Linting](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml)<br>
[![SHA3-256 Generate and Update](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml)<br>

## Other
[![Upload Python Package](https://github.com/TokynBlast/pyTGM/actions/workflows/python-publish.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/python-publish.yml)

# pyTGM (Python Terminal Game Maker)

>[!NOTE]
> There was an accidental deletion of the original pyTGM library. This is an updated version of the newest version I had on hand.
>
>This note will be deleted in the next version.

>[!NOTE]
>This will be uploaded to PyPi soon.

pyTGM is a simplified alternative to Pygame, focusing on ASCII and ANSI based game development, with utilities for encryption, randomization, markup, and more.

## Bugs and Features
To report a bug, go to [here](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=)<br>
For feature request, go [here](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=)

## Contributing
All contributions are greatly appreciated.<br>
To make a contribution, make a new branch [here](https://github.com/TokynBlast/pyTGM/branches)<br>
Then, add (or remove), to improve the repo!<br>
Then, somebody will check to make sure it complys with all the workflows, it will be uploaded!

If your modified code doesn't comply with Saftey, it will be immediatley denied.
Testing changes will occur on a VM, without Wi-fi, for security reasons.
Code will also be checked manually.

## Features

### File Operations
```python
file.mod_line(name)           # Modify a line of a file
file.read_line(name, line=0)  # Read specific line
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
LocalServer(1080, {'MarkTheMighty':((243,332), 57)})
```
An example of a returned value would be:
```python
{'LordMinion777':((0,0), 100), 'Muyskerm':((245,334), 43)}
```

### Terminal Input Detection
```python
# Mouse Click Detection
terd.click()             # Returns coordinates (-1,-1) to signal an invalid input.

# Keyboard Press Detection
terd.geky(times)
```

### Encryption
```python
# Set the table
b64.Table.table = 'ABCDEF...XYZ...12...90...!@..._+' # Make sure it has character that will be used, special chars are also usable
b64.Table.generate('ABCDEF...XYZ...12...90...!@..._+', 32)

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
