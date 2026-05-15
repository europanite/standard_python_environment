---
layout: page
title: "🇮🇳 हिन्दी"
permalink: /hi/
lang: hi
---

# [Standard Python Environment](https://github.com/europanite/standard_python_environment "Standard Python Environment")

[![Python](https://img.shields.io/badge/python-3.9|%203.10%20|%203.11|%203.12|%203.13-blue)](https://www.python.org/)
![OS](https://img.shields.io/badge/OS-Linux%20%7C%20macOS%20%7C%20Windows-blue)

[![CI](https://github.com/europanite/standard_python_environment/actions/workflows/ci.yml/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/ci.yml)
[![Python Lint](https://github.com/europanite/standard_python_environment/actions/workflows/lint.yml/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/lint.yml)
[![Pytest](https://github.com/europanite/standard_python_environment/actions/workflows/pytest.yml/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/pytest.yml)
[![pages-build-deployment](https://github.com/europanite/standard_python_environment/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/pages/pages-build-deployment)
[![CodeQL Advanced](https://github.com/europanite/standard_python_environment/actions/workflows/codeql.yml/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/codeql.yml)

![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?logo=pytest&logoColor=2f9fe3)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?logo=jupyter&logoColor=white)

<p align="right">
  <a href="https://europanite.github.io/standard_python_environment/">🇺🇸 English</a> |
  <a href="https://europanite.github.io/standard_python_environment/hi/">🇮🇳 हिंदी</a> |
  <a href="https://europanite.github.io/standard_python_environment/ja/">🇯🇵 日本語</a> |
  <a href="https://europanite.github.io/standard_python_environment/zh-CN/">🇨🇳 简体中文</a> |
  <a href="https://europanite.github.io/standard_python_environment/es/">🇪🇸 Español</a> |
  <a href="https://europanite.github.io/standard_python_environment/pt-BR/">🇧🇷 Português (Brasil)</a> |
  <a href="https://europanite.github.io/standard_python_environment/ko/">🇰🇷 한국어</a> |
  <a href="https://europanite.github.io/standard_python_environment/de/">🇩🇪 Deutsch</a> |
  <a href="https://europanite.github.io/standard_python_environment/fr/">🇫🇷 Français</a>
</p>

**Docker Compose** से बनाया गया एक मानक **Python** वातावरण।

!["image"](./assets/images/image.png)

---

## विशेषताएँ

- **पुनरुत्पादनयोग्यता**: डिपेंडेंसीज़ कंटेनर के अंदर लॉक रहती हैं
- **सरलता**: केवल docker compose कमांड से चलाएँ
- **पोर्टेबिलिटी**: Linux, macOS, और Windows पर काम करता है
- **pip ready**: Python पैकेज आसानी से इंस्टॉल और मैनेज करें
- **JupyterLab support**: (वैकल्पिक) कंटेनर के अंदर notebooks चलाएँ
- **X11 forwarding**: (वैकल्पिक) GUI-आधारित Python ऐप्स चलाएँ

---


## आवश्यकताएँ

- [Docker Compose](https://docs.docker.com/compose/)

---

## शुरू करना

### Linux

```bash
# Clone this repository
git clone https://github.com/europanite/standard_python_environment.git
cd standard_python_environment

# Export host UID/GID
export HOST_UID=$(id -u) 
export HOST_GID=$(id -g)

# Build and run
docker compose build
docker compose up -d
docker compose exec service bash
```

### Windows

```powershell
# Clone this repository
git clone https://github.com/europanite/standard_python_environment.git
cd standard_python_environment

# Build and run
docker compose build
docker compose up -d
docker compose exec service bash
```

अब आप Python कंटेनर के अंदर हैं 🎉

यदि आप JupyterLab का उपयोग करते हैं, तो आपको बस http://localhost:8888 खोलना है

---

### टेस्ट

```bash
# pytest
docker compose \
-f docker-compose.test.yml run \
--rm \
--entrypoint /bin/sh service_test \
-lc 'pytest'

# Lint
docker compose \
-f docker-compose.test.yml run \
--rm \
--entrypoint /bin/sh service_test \
-lc 'ruff check /app /tests'
```

## लाइसेंस
- Apache License 2.0
