FROM apache/superset:latest

USER root

# 1. Instalar librerías del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libsasl2-dev \
    libldap2-dev \
    default-libmysqlclient-dev \
    && apt-get clean

# 2. Copiar los archivos de configuración
COPY requirements.txt .
COPY superset_config.py /app/pythonpath/superset_config.py

# 3. TRUCO DE MAGIA: Instalar DIRECTAMENTE en el entorno virtual de Superset
# Usamos '/app/.venv/bin/pip' para asegurar que las librerías queden donde el servidor las busca
RUN /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

USER superset
