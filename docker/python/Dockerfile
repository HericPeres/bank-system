FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primeiro (para cache)
COPY python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código Python
COPY python/ /app/python/

# Criar diretório compartilhado
RUN mkdir -p /shared_data

# Expor portas
EXPOSE 8000
EXPOSE 8501

WORKDIR /app/python