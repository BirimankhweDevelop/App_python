name: Compilar APK Android

on:
  workflow_dispatch:
  push:
    branches:
      - principal

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Obter código
        uses: actions/checkout@v4

      - name: Preparar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Preparar Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'

      - name: Instalar dependências
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git zip unzip autoconf automake libtool pkg-config \
            zlib1g-dev libncurses5-dev libncursesw5-dev \
            cmake libffi-dev libssl-dev libltdl-dev

      - name: Instalar Buildozer
        run: |
          python -m pip install --upgrade pip
          pip install buildozer cython==0.29.36

      - name: Aceitar licenças e instalar ferramentas Android
        run: |
          SDKMANAGER="$HOME/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager"
          if [ ! -x "$SDKMANAGER" ]; then
            SDKMANAGER="$HOME/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager"
          fi
          if [ ! -x "$SDKMANAGER" ]; then
            echo "sdkmanager ainda não foi instalado pelo Buildozer."
            exit 1
          fi
          yes | "$SDKMANAGER" --licenses || true
          "$SDKMANAGER" "platform-tools" "platforms;android-35" "build-tools;35.0.0"

      - name: Compilar APK
        run: |
          yes | buildozer -v android debug

      - name: Disponibilizar APK
        uses: actions/upload-artifact@v4
        with:
          name: meu-apk-android
          path: bin/*.apk
          if-no-files-found: error
