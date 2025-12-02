FROM apache/superset:latest

USER root

# 1. Instalar dependencias del sistema (Incluyendo pkg-config y curl que faltaban)
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libsasl2-dev \
    libldap2-dev \
    default-libmysqlclient-dev \
    pkg-config \
    curl \
    && apt-get clean

# 2. Copiar configuración
COPY requirements.txt .
COPY superset_config.py /app/pythonpath/superset_config.py

# 3. FIX CRÍTICO: Descargar e instalar pip dentro del entorno virtual de Superset
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && /app/.venv/bin/python get-pip.py \
    && rm get-pip.py

# 4. Instalar las librerías en el entorno correcto
RUN /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

USER superset
