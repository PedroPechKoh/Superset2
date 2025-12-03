 import os



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



FEATURE_FLAGS = {

    "EMBEDDED_SUPERSET": True

}



# --- COOKIE FIX (CRUCIAL PARA IFRAMES EN RAILWAY) ---

# Esto permite que la sesión de invitado no sea bloqueada por Chrome/Edge

SESSION_COOKIE_SAMESITE = "None"

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True



# --- ROL DE INVITADO ---
GUEST_TOKEN_JWT_AUDIENCE = "https://superset2-production.up.railway.app/"
# Esto asegura que el invitado use el rol 'Public' como base

GUEST_ROLE_NAME = "Public"

FEATURE_FLAGS = {

    "EMBEDDED_SUPERSET": True

}

