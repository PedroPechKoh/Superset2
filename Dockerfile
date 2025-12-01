FROM apache/superset:latest

USER root

# 1. Instalar dependencias (Agregamos 'pkg-config' y 'curl' que son vitales)
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

# 2. Copiar archivos
COPY requirements.txt .
COPY superset_config.py /app/pythonpath/superset_config.py

# 3. CIRUGÍA: Descargar e instalar pip DENTRO del entorno virtual de Superset
# Esto arregla el error "No module named pip" dentro de la app
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && /app/.venv/bin/python get-pip.py \
    && rm get-pip.py

# 4. Instalar las librerías usando el pip de la burbuja
RUN /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

USER superset
