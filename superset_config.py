import os

# --- SEGURIDAD ---
SECRET_KEY = os.getenv("SECRET_KEY")

# --- BASE DE DATOS METADATA (Postgres de Railway) ---
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

# --- CACHÉ CON REDIS (Para evitar errores de memoria) ---
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": os.getenv("REDIS_URL")
}

# --- PERMISOS PARA EMBEBER (SoulArt) ---
ENABLE_PROXY_FIX = True
TALISMAN_ENABLED = False
WTF_CSRF_ENABLED = False 

ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "resources": ["*"],
    "origins": ["*"] 
}

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}
