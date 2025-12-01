import os

# Clave secreta (Llenaremos esto en las variables de Railway)
SECRET_KEY = os.getenv("SECRET_KEY")

# Permitir que Superset se ejecute detrás del proxy de Railway
ENABLE_PROXY_FIX = True

# Desactivar protección estricta contra iFrames para permitir incrustar
TALISMAN_ENABLED = False 

# Habilitar CORS para tu dominio de Railway y Frontend
ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "resources": ["*"],
    "origins": ["*"] # O pon aquí tu dominio: ["https://soulart-production.up.railway.app"]
}

# Feature Flags: ¡IMPORTANTE para Dashboards embebidos!
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}

# Configuración de Base de Datos (Railway usa Postgres para la metadata de Superset)
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")