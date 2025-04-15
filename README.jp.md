# Workflow Status

<!-- Eventually, will be |linting|security|築く|です -->
| **Linting** | [![C++ Lint](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml) | [![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml) | [![Isort](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml)
|-----------|----------|----------|----------|
| **Security** | [![Safety Linting](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml) | [![SHA256 Generate そして Update](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml) | |
| **築く** |[![築く C++](https://github.com/TokynBlast/pyTGM/actions/workflows/compile.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/compile.yml)| | |

> [!warning]
> それsource code under heavy developmentです。<br>most 時間 errorsです.

> [!warning]
> わたし学ぶ日本語。<br>和文たぶんミス！<br>Heavy use of「・」is for 僕 そして・あなた

## Installing
run ```pip install pyTGM``` install<br>
before 5.0.0 must be  from source。<br>
あなた need cmake、 setuptools、 wheel<br>
また Python.h<br>
あなた can get it from python3-dev<br><br>
macOS 築く from sourceです<br><br>
some things can be　remove after 築く<br>
Run ```setup.sh```　to install the materials for です。<br><br>

windows need Visual Studio 2017 or later。<br>
for Python、enable:
- Add Python to PATH
- Customize installation > Development Tools

リナックスcommand changes:<br>
```
bash -c 'if command -v apt-get >/dev/null; then sudo apt-get update && sudo apt-get install -y python3-dev elif command -v dnf >/dev/null; then sudo dnf install -y python3-devel elif command -v pacman >/dev/null; then sudo pacman -Sy --noconfirm python elif command -v zypper >/dev/null; then sudo zypper install -y python3-devel elif command -v brew >/dev/null; then brew install python elif command -v pkg >/dev/null; then sudo pkg install -y python elif command -v emerge >/dev/null; then sudo emerge --ask dev-lang/python elif command -v apk >/dev/null; then sudo apk add --no-cache python3-dev else echo "Unsupported package manager. Install Python dev headers manually." exit 1 fi'
```

# pyTGM【Python・Terminal・Game・Maker】

pyTGM simple alternative Pygame, priority ASCII そして ANSI game development, contained in terminal、です<br>
has encryption、markup、sound playing、servers、またmore。

## Bugs・そして・Features
bug [ここ](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=)<br>
feature [ここ](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=)<br>
築くerror/warning、[ここ](https://github.com/TokynBlast/pyTGM/issues/new?template=compile_report.md)

## Contributing
Contributions appreciated。<br>
To 築く contribution、 築く branch[ここ](https://github.com/TokynBlast/pyTGM/branches)<br>
Then、そして/remove、to improve！<br>
我々・証・それcode safeそしてworking。<br>
or、あげますmake donation！[ここ](https://github.com/sponsors/TokynBlast)<br>
ありがとう！

# Suggestions
あなたいいえalways need everything。
```\a``` can築くbeep、called an escape sequencesです。<br>
The libraryそして　more escape sequences can combine for more control！
pyTGM uses them！pyTGM simple interface forです。

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

# Systematically print rectangle
rect(width, height, time=3, character=" ")
```


## Sound Support
Work・ウィンドウズ、マック、リナックス:
```python
# Play audio file
sound('../sounds/mysound.mp3')
```

## 網・Server・Support
```python
# Start serverそしてclient (PORT, message)
LocalServer(1080, {'てと':((243,332), 57)})
```
受ける・example:
```python
{'初音ミクみく':((0,0), 100), 'レモン':((245,334), 43)}
```

## Encryption

### b64:
```python
# Set the table
encrypt.b64.Table.table = 'あいうえお...わをん...12...90...!@..._+'
encrypt.b64.Table.generate('あいうえお...わをん...12...90...!@..._+', 32)  # (table: str, times: int)

# Encodeそしてdecode
encrypt.b64.encode(text) # encode
encrypt.b64.decode(text) # decode
```
when setting table、must have the characters in the inputです！
Extra characters increase securityそしてsize of output.
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
pyTGM licensed under Bspace, by Tokyn Blast/ときゆ/tokiyu.
