import os
from datetime import timedelta

# --- SEGURIDAD ---
SECRET_KEY = os.getenv("SECRET_KEY")

# --- BASE DE DATOS METADATA ---
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

# --- CACHÉ ---
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": os.getenv("REDIS_URL")
}
RATELIMIT_STORAGE_URI = os.getenv("REDIS_URL")

# --- PERMISOS DE EMBEBIDO (SOULART) ---
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

# 🛑 FEATURE FLAGS (Corregido y Unificado)
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "GUEST_TOKEN_JWT_AUTH": True
}

# 🛑 CONFIGURACIÓN DE AUDIENCIA (AUD)
# Esto anula el valor 0.0.0.0:8080.
GUEST_TOKEN_JWT_AUDIENCE = "https://superset2-production.up.railway.app/" 


# --- COOKIE FIX ---
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

# --- ROL DE INVITADO ---
# Sincronizado con el rol que tiene permisos de lectura de datos.
GUEST_ROLE_NAME = "Gamma"
