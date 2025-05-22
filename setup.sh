#!/bin/bash

# Emojis
E_S="🔧"; E_P="🐍"; E_I="📦"; E_U="⬆️"; E_D="🧰"; E_C="🛠️"; E_O="✅"; E_R="🚀"; E_X="❌"

# Detect system language and map to internal codes
case "${LANG%%.*}" in
  ja*) L=2 ;;  # Japanese
  zh*) L=3 ;;  # Chinese
  es*) L=4 ;;  # Spanish
  *)   L=1 ;;  # Default to English
esac

# Language messages (English fallback is always used if missing)
[[ $L == 1 ]] && T=( "Starting pyTGM setup" "Checking Python..." "Python3 not found."
  "Checking pip..." "pip3 not found." "Upgrading pip..." "Install dev tools too? (y/n)"
  "Installing dev packages..." "Installing required packages..." "Setup complete!" "To run:"
)
[[ $L == 2 ]] && T=( "pyTGM セットアップ開始" "Pythonを確認中..." "Python3が見つかりません。"
  "pipを確認中..." "pip3が見つかりません。" "pipをアップグレード中..." "開発ツールもインストールしますか？ (y/n)"
  "開発パッケージをインストール中..." "必要なパッケージをインストール中..." "セットアップ完了！" "実行方法:"
)
[[ $L == 3 ]] && T=( "开始设置 pyTGM" "检查 Python..." "未找到 Python3。"
  "检查 pip..." "未找到 pip3。" "正在升级 pip..." "是否也安装开发工具？(y/n)"
  "正在安装开发依赖..." "正在安装所需依赖..." "设置完成！" "运行命令："
)
[[ $L == 4 ]] && T=( "Iniciando configuración de pyTGM" "Verificando Python..." "No se encontró Python3."
  "Verificando pip..." "No se encontró pip3." "Actualizando pip..." "¿Instalar herramientas de desarrollo también? (y/n)"
  "Instalando paquetes de desarrollo..." "Instalando paquetes necesarios..." "¡Configuración completada!" "Para ejecutar:"
)

# Start
echo "$E_S ${T[0]}"
echo "$E_P ${T[1]}"
command -v python3 &>/dev/null || { echo "$E_X ${T[2]}"; exit 1; }

echo "$E_I ${T[3]}"
command -v pip3 &>/dev/null || { echo "$E_X ${T[4]}"; exit 1; }

# Upgrade pip only if outdated
pip list --outdated --disable-pip-version-check 2>/dev/null | grep -q '^pip' && {
  echo "$E_U ${T[5]}"
  pip install --upgrade pip --disable-pip-version-check
}

# Ask for dev tool install (if file exists)
[ -f requirements-dev.txt ] && { echo "$E_D ${T[6]}"; read -r dev; }

# Install path: use --user unless in venv
[[ -z "$VIRTUAL_ENV" ]] && INSTALL_ARGS="--user" || INSTALL_ARGS=""

# Install main requirements
echo "$E_I ${T[8]}"
PIP_NO_BUILD_ISOLATION=1 pip install $INSTALL_ARGS --prefer-binary -r requirements.txt

# Install dev requirements (if chosen)
[[ "$dev" == [yY] ]] && {
  echo "$E_C ${T[7]}"
  PIP_NO_BUILD_ISOLATION=1 pip install $INSTALL_ARGS --prefer-binary -r requirements-dev.txt
}

# Done
echo "$E_O ${T[9]}"
echo "$E_R ${T[10]} python3 -m pyTGM"
