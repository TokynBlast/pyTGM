# 🛠️ ワークフロー状況（Workflow Status）

<!-- Eventually, will be |linting|security|築く|です -->

| **《コードチェック》** | [![C++ Lint](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/cpplint.yml) | [![Pylint](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/pylint.yml)                                | [![Isort](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Isort.yml) |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **《セキュリティ》**  | [![Safety](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/Saftey.yml)     | [![SHA256 生成](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/generate-sha3-hashes.yml) |                                                                                                                                                        |
| **《築く》**      | [![C++ ビルド](https://github.com/TokynBlast/pyTGM/actions/workflows/compile.yml/badge.svg)](https://github.com/TokynBlast/pyTGM/actions/workflows/compile.yml)  |                                                                                                                                                                                          |                                                                                                                                                        |

> ⚠️ **注意：このプロジェクトは現在開発中です。**<br>本番環境での利用は自己責任でお願いします。

> 🧠 **補足：日本語を学習中のため、文法ミスがあるかもしれません。**<br>もしおかしい部分があれば、ぜひ教えてください！<br>「・」は僕とお兄ちゃんのための記号です。

---

## 📦 インストール方法（Installing）

### pip の場合

```sh
pip install pyTGM
```

バージョン 5.0.0 より前は、ソースコードからビルドする必要があります。

### 必要なツール

* cmake
* setuptools
* wheel
* Python 開発ヘッダー（例: python3-dev）

### macOS の場合

```sh
./setup.sh
```

### Windows の場合

Visual Studio 2017 以降が必要です。
Python インストール時に以下を有効にしてください：

* Add Python to PATH
* Customize installation > Development Tools

### Linux の場合（自動検出）

```sh
bash -c 'if command -v apt-get >/dev/null; then sudo apt-get update && sudo apt-get install -y python3-dev elif command -v dnf >/dev/null; then sudo dnf install -y python3-devel elif command -v pacman >/dev/null; then sudo pacman -Sy --noconfirm python elif command -v zypper >/dev/null; then sudo zypper install -y python3-devel elif command -v brew >/dev/null; then brew install python elif command -v pkg >/dev/null; then sudo pkg install -y python elif command -v emerge >/dev/null; then sudo emerge --ask dev-lang/python elif command -v apk >/dev/null; then sudo apk add --no-cache python3-dev else echo "対応していないパッケージマネージャです。Python 開発ヘッダーを手動でインストールしてください。"; exit 1; fi'
```

---

# 🎮 ピトグム【Python・Terminal・ゲーム作成】

ピトグム（pyTGM）は、ターミナルで動作するシンプルなゲームを作成できるライブラリです。

ASCIIやANSIアートを使って、音声・通信・暗号化などの機能も備えています。

---

## 🐞 バグ報告・機能要望

* バグ報告：[ここをクリック](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=)
* 機能提案：[ここをクリック](https://github.com/TokynBlast/pyTGM/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=)
* ビルド関連の報告：[ここをクリック](https://github.com/TokynBlast/pyTGM/issues/new?template=compile_report.md)

---

## ❤️ コントリビューション（協力）

* [ブランチを作成](https://github.com/TokynBlast/pyTGM/branches)して、変更を加えてください。
* プルリクエストを送っていただければ、確認してマージします。
* [GitHub Sponsors](https://github.com/sponsors/TokynBlast) による支援も大歓迎です！

---

## 💡 ヒント

お兄ちゃん、全部の機能が必要なわけではないよ。

```python
\a  # ビープ音（ANSIエスケープ）
```

ターミナルの制御やライブラリが提供する機能で、もっと自由に！

---

## 🌟 機能例（Examples）

### ターミナル制御

```python
terminal.cls()  # 画面をクリア
terminal.color(0, 255, 0)  # 色を指定（RGB）
print(terminal.BOLD + "太字!" + terminal.RESET)
```

### 音声再生

```python
sound('mysound.mp3')  # Windows / macOS / Linux 対応
```

### 簡易サーバー通信

```python
LocalServer(1080, {'名前': ((123, 456), 99)})
```

受信例：

```python
{'初音ミク': ((0, 0), 100), 'レモン': ((245, 334), 43)}
```

### 暗号化（Base64・SHA256・カスタム）

#### Base64（ブ64）

```python
encrypt.b64.Table.table = 'あいうえおかきくけこ...'
encrypt.b64.Table.generate('文字列セット', 32)

encrypt.b64.encode(text)
encrypt.b64.decode(text)
```

#### SHA256 ハッシュ

```python
encrypt.sha256("テキスト")
```

#### フク512（カスタム）

```python
encrypt.hk512.encode(data, key)
encrypt.hk512.decode(data, key)
```

---

## 🔗 関連リンク

* [ホームページ](https://pyTGM.tokynblast.space/home)
* [使い方ガイド](https://pyTGM.tokynblast.space/documentation/use)
* [GitHub リポジトリ](https://github.com/TokynBlast/pyTGM/tree/main)
* [バグ報告と提案](https://github.com/TokynBlast/pyTGM/issues)
* [更新履歴](https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt)

---

## 🪪 ライセンス

このプロジェクトは **Bspace License** に基づいて、Tokyn Blast（ときゆ）によって公開されています。

---

> 🌲 「木を隠すなら森の中」
