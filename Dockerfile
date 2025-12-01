FROM apache/superset:latest

USER root

# 1. Instalar dependencias del sistema Y TAMBIÉN 'python3-pip' (El Fix)
# Agregamos 'python3-pip' a la lista para forzar su instalación
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libsasl2-dev \
    libldap2-dev \
    default-libmysqlclient-dev \
    python3-pip \
    && apt-get clean

# 2. Copiar archivos de configuración
COPY requirements.txt .
COPY superset_config.py /app/pythonpath/superset_config.py

# 3. Instalar las librerías usando el pip que acabamos de instalar
# Usamos 'pip3' y el flag '--break-system-packages' por si acaso Debian se queja
RUN pip3 install --no-cache-dir -r requirements.txt

USER superset
