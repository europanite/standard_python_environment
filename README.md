# Standard Python Environment

A standard Python environment built with Docker Compose

This repository provides a standard Python execution environment using **Docker Compose**.  
It is useful when you want to ensure consistency across different machines without installing Python or dependencies directly on your host.

---

## Features

- **Reproducibility**: Dependencies are locked inside the container
- **Simplicity**: Run with just `docker compose up` or `docker compose run`
- **Portability**: Works on Linux, macOS, and Windows
- **pip ready**: Install and manage Python packages easily
- **JupyterLab support**: Run notebooks inside the container
- **X11 forwarding**: (Optional) Run GUI-based Python apps

---


## Prerequisites

- Docker (Docker Desktop, etc.)
- Docker Compose v2 (`docker compose` command available)

---

## Getting Started

```bash

# Clone this repository
git clone https://github.com/skinner-repository/standard_python_environment.git
cd standard_python_environment

# Export host UID/GID
export HOST_UID=$(id -u) 
export HOST_GID=$(id -g)

# Build and run
docker compose --env-file ./service/.env build
docker compose --env-file ./service/.env up -d
docker compose --env-file ./service/.env exec service bash

```
Now you are inside the Python container 🎉

If you use JupyterLab, just you need to access http://localhost:8888

---

## License
- MIT