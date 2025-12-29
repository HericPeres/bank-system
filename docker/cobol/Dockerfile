FROM ubuntu:22.04

# Instalar COBOL e dependências
RUN apt-get update && apt-get install -y \
    gnucobol \
    cobc \
    build-essential \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app/cobol

# Copiar scripts
COPY scripts/ ./scripts/
RUN chmod +x scripts/*.sh