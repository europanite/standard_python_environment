---
layout: page
title: "🇩🇪 Deutsch"
permalink: /de/
lang: de
---

# [Standard Python Environment](https://github.com/europanite/standard_python_environment "Standard Python Environment")

[![Python](https://img.shields.io/badge/python-3.9|%203.10%20|%203.11|%203.12|%203.13-blue)](https://www.python.org/)
![OS](https://img.shields.io/badge/OS-Linux%20%7C%20macOS%20%7C%20Windows-blue)

[![CI](https://github.com/europanite/standard_python_environment/actions/workflows/ci.yml/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/ci.yml)
[![Python Lint](https://github.com/europanite/standard_python_environment/actions/workflows/lint.yml/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/lint.yml)
[![Pytest](https://github.com/europanite/standard_python_environment/actions/workflows/pytest.yml/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/pytest.yml)
[![pages-build-deployment](https://github.com/europanite/standard_python_environment/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/pages/pages-build-deployment)
[![CodeQL Advanced](https://github.com/europanite/standard_python_environment/actions/workflows/codeql.yml/badge.svg)](https://github.com/europanite/standard_python_environment/actions/workflows/codeql.yml)

<p align="right">
  <a href="/standard_python_environment/">🇺🇸 English</a> |
  <a href="/standard_python_environment/hi/">🇮🇳 हिन्दी</a> |
  <a href="/standard_python_environment/ja/">🇯🇵 日本語</a> |
  <a href="/standard_python_environment/zh-CN/">🇨🇳 简体中文</a> |
  <a href="/standard_python_environment/es/">🇪🇸 Español</a> |
  <a href="/standard_python_environment/pt-BR/">🇧🇷 Português (Brasil)</a> |
  <a href="/standard_python_environment/ko/">🇰🇷 한국어</a> |
  <a href="/standard_python_environment/de/">🇩🇪 Deutsch</a> |
  <a href="/standard_python_environment/fr/">🇫🇷 Français</a>
</p>

Eine standardisierte **Python**-Umgebung, erstellt mit **Docker Compose**.

!["image"](./assets/images/image.png)

---

## Funktionen

- **Reproduzierbarkeit**: Abhängigkeiten sind im Container festgelegt
- **Einfachheit**: Ausführung nur mit docker compose-Befehlen
- **Portabilität**: Funktioniert unter Linux, macOS und Windows
- **pip ready**: Python-Pakete einfach installieren und verwalten
- **JupyterLab support**: (Optional) Notebooks im Container ausführen
- **X11 forwarding**: (Optional) GUI-basierte Python-Apps ausführen

---


## Anforderungen

- [Docker Compose](https://docs.docker.com/compose/)

---

## Erste Schritte

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

Jetzt befinden Sie sich im Python-Container 🎉

Wenn Sie JupyterLab verwenden, müssen Sie nur http://localhost:8888 aufrufen

---

### Test

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

## Lizenz
- Apache License 2.0
