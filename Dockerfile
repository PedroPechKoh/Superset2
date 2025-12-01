FROM apache/superset:latest

USER root

# 1. Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libsasl2-dev \
    libldap2-dev \
    default-libmysqlclient-dev \
    && apt-get clean

# 2. Copiar archivos
COPY requirements.txt .
COPY superset_config.py /app/pythonpath/superset_config.py

# 3. EL FIX: Usamos 'python -m pip' en lugar de llamar a pip directamente
# Esto obliga a usar el pip que vive dentro del Python de Superset
RUN /app/.venv/bin/python -m pip install --no-cache-dir -r requirements.txt

USER superset
