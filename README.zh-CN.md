---
layout: page
title: "🇨🇳 中文"
permalink: /zh-CN/
lang: zh-CN
---

# [Standard Python Environment](https://github.com/europanite/standard_python_environment "Standard Python Environment")

[![Python](https://img.shields.io/badge/python-3.9|%203.10%20|%203.11|%203.12|%203.13|%203.14-blue)](https://www.python.org/)
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

一个使用 **Docker Compose** 构建的标准 **Python** 环境。

!["image"](./assets/images/image.png)

---

## 功能特性

- **可复现性**：依赖项锁定在容器内部
- **简单性**：只需使用 docker compose 命令即可运行
- **可移植性**：可在 Linux、macOS 和 Windows 上运行
- **pip ready**：轻松安装和管理 Python 包
- **JupyterLab support**：（可选）在容器内运行 notebooks
- **X11 forwarding**：（可选）运行基于 GUI 的 Python 应用

---


## 要求

- [Docker Compose](https://docs.docker.com/compose/)

---

## 快速开始

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

现在你已经进入 Python 容器了 🎉

如果使用 JupyterLab，只需访问 http://localhost:8888

---

### 测试

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

## 许可证
- Apache License 2.0
