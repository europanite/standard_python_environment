FROM python:3.12-bookworm

# Faster Python stdout/stderr & safer pip defaults
ENV PYTHONUNBUFFERED=1

ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies (add more as needed)
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        ca-certificates \
        sudo \
        x11-apps; \
    rm -rf /var/lib/apt/lists/*

# Python dependencies  
WORKDIR /root
COPY requirements.txt /root/requirements.txt
RUN set -eux; \
    python -m pip install --upgrade pip setuptools wheel; \
    if [ -s /root/requirements.txt ]; then \
        pip install --no-cache-dir -r /root/requirements.txt; \
    fi

# receive environment values
ARG HOST_USERNAME
ARG HOST_GROUPNAME
ARG HOST_UID
ARG HOST_GID

# set variables
ENV HOST_USERNAME=${HOST_USERNAME}
ENV HOST_GROUPNAME=${HOST_GROUPNAME}
ENV HOST_UID=${HOST_UID}
ENV HOST_GID=${HOST_GID}

# Create user/group
RUN groupadd -g $HOST_GID $HOST_GROUPNAME && \
    useradd -m -s /bin/bash -u $HOST_UID -g $HOST_GID $HOST_USERNAME && \
    usermod -aG sudo $HOST_USERNAME && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# App workspace
WORKDIR /app
COPY . /app

# User
USER $HOST_USERNAME

# Default command can be overridden by docker compose
CMD ["python", "--version"]