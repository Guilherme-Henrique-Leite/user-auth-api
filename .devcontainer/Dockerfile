FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash vscode \
    && mkdir -p /home/vscode/.vscode-server

RUN pip install uv

RUN mkdir -p /workspace && chown vscode:vscode /workspace

WORKDIR /workspace

USER vscode

CMD ["sleep", "infinity"]