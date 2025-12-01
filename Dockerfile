FROM apache/superset:latest

USER root

# Instalar dependencias del sistema para mysqlclient
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar config y requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY superset_config.py /app/pythonpath/superset_config.py

USER superset