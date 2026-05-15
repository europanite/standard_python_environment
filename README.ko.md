---
layout: page
title: "🇰🇷 한국어"
permalink: /ko/
lang: ko
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

**Docker Compose**로 구성된 표준 **Python** 환경입니다.

!["image"](./assets/images/image.png)

---

## 기능

- **재현성**: 의존성이 컨테이너 내부에 고정됩니다
- **단순성**: docker compose 명령만으로 실행할 수 있습니다
- **이식성**: Linux, macOS, Windows에서 동작합니다
- **pip ready**: Python 패키지를 쉽게 설치하고 관리할 수 있습니다
- **JupyterLab support**: (선택 사항) 컨테이너 안에서 notebooks를 실행할 수 있습니다
- **X11 forwarding**: (선택 사항) GUI 기반 Python 앱을 실행할 수 있습니다

---


## 요구 사항

- [Docker Compose](https://docs.docker.com/compose/)

---

## 시작하기

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

이제 Python 컨테이너 안에 있습니다 🎉

JupyterLab을 사용하는 경우 http://localhost:8888 에 접속하기만 하면 됩니다

---

### 테스트

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

## 라이선스
- Apache License 2.0
