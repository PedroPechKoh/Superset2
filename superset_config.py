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

# 🛑 CORRECCIÓN 1: Habilitar la autenticación JWT para el Guest Token
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "GUEST_TOKEN_JWT_AUTH": True
}

# --- COOKIE FIX (CRUCIAL PARA IFRAMES EN RAILWAY) ---
# Esto permite que la sesión de invitado no sea bloqueada por Chrome/Edge
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

# --- ROL DE INVITADO ---
# 🛑 CORRECCIÓN 2: Usar 'Gamma' (o el rol que tiene permisos de lectura de datos)
# Si tu Rol con permisos es 'Gamma', ¡debe estar aquí!
GUEST_ROLE_NAME = "Gamma"
