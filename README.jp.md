# Workflow Status

<!-- Eventually, will be |linting|security|築く|です -->
| **《Linting》** | [![C++ Lint](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml) | [![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml) | [![Isort](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml)
|-----------|----------|----------|----------|
| **《Security》** | [![Safety Linting](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml) | [![SHA256 Generate そして Update](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml) | |
| **《築く》** |[![《築く》 C++](https://github.com/TokynBlast/pyTGM/actions/workflows/compile.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/compile.yml)| | |

> [!warning]
> それsourceコードunder developmentです。<br>most時間errorsです.

> [!warning]
> 私は日本語を学んている。<br>和文たぶんミス！<br>「・」is for僕そしてお兄ちゃん<br>そして・ジスブ・鬼マークドーン <br>いいえ柄。<br>くヘルプださい。僕ミス

## Installing
走る ```pip install pyTGM```<br>
before 5.0.0要らます、築くsource。<br>
お兄ちゃん要らます ```cmake、setuptools、wheel```<br>
また ```Python.h```<br>
お兄ちゃんできるget from python3-devです<br><br>
macOS築くfrom sourceです<br>
走る ```setup.sh``` to install materials forです。<br><br>

windows要らますVisual Studio 2017 or later。<br>
for Python、enable:
- Add Python to PATH
- Customize installation > Development Tools

リナックスcommand changes:<br>
```
bash -c 'if command -v apt-get >/dev/null; then sudo apt-get update && sudo apt-get install -y python3-dev elif command -v dnf >/dev/null; then sudo dnf install -y python3-devel elif command -v pacman >/dev/null; then sudo pacman -Sy --noconfirm python elif command -v zypper >/dev/null; then sudo zypper install -y python3-devel elif command -v brew >/dev/null; then brew install python elif command -v pkg >/dev/null; then sudo pkg install -y python elif command -v emerge >/dev/null; then sudo emerge --ask dev-lang/python elif command -v apk >/dev/null; then sudo apk add --no-cache python3-dev else echo "Unsupported package manager. Install Python dev headers manually." exit 1 fi'
```

# ピトグム【Python・Terminal・遊び・生み出す】

ピトグムsimple alternative to Pygame, focus on ASCIIそしてANSI遊び生み出す, contained中terminal、です<br>
has encryption、markup、sound playing、servers、また・もっと。

## Bugs・そして・Features
bug [《ここ》](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=)<br>
feature [《ここ》](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=)<br>
築くerror/warning、[《ここ》](https://github.com/TokynBlast/pyTGM/issues/new?template=compile_report.md)

## 養う
養うappreciated。<br>
to築くcontribution、築くbranch[《ここ》](https://github.com/TokynBlast/pyTGM/branches)<br>
then、add/remove、to 養う！<br>
我々・証・それコードsafeそしてworking。<br>
or、養う！[《ここ》](https://github.com/sponsors/TokynBlast)<br>
ありがとう！

# Suggestions
お兄ちゃんはいいえalways need everything。
```\a```できる築くbeep、それ逃sequencesです。<br>
図書館そして・もっと逃sequences共もっとcontrol！
ピトグムuses them！ピトグムsimple interface forです。

# 特色

## Terminal
```python
# Clear screen
terminal.cls()

# 色 text (赤, green, 青)
terminal.color(0, 255, 0)  # (R, G, B)
terminal.RESET             # Reset色

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
共・ウィンドウズ、マック、リナックス:
```python
# Play audio file
sound('../sounds/mysound.mp3')
```

## 網 <!--Find a way to say "server"　or a word used for it by Japanese dev-->
```python
# Start 網そしてclient (PORT, message)
LocalServer(1080, {'てと':((243,332), 57)})
```
受ける・example:
```python
{'初音ミクみ':((0,0), 100), 'レモン':((245,334), 43)}
```

## Encryption

### ブ64:
```python
# Set 一覧表
encrypt.b64.Table.table = 'あいうえお...わをん...12...90...!@..._+'
encrypt.b64.Table.generate('あいうえお...わをん...12...90...!@..._+', 32)  # (table: str, times: int)

# Encode・そして・decode
encrypt.b64.encode(text) # encode
encrypt.b64.decode(text) # decode
```
時間setting table、要らます字中inputです！
Extra字increase securityそしてsize of output.
```python
encrypt.sha256(text)
```


### フク512:
```python
encrypt.hk512.encode(data, key)
encrypt.hk512.decode(data, key)
```

## Links
- [Homepage](https://pyTGM.tokynblast.space/home)
- [手引書](https://pyTGM.tokynblast.space/documentation/use)
- [Source・コード](https://github.com/TokynBlast/pyTGM/tree/main)
- [Bug Tracker](https://github.com/TokynBlast/pyTGM/issues)
- [Changelog](https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt)

## License
pyTGM licensed under Bspace, by Tokyn Blast/ときゆ/tokiyu.


「木を隠すなら森の中」
