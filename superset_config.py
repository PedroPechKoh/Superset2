import os
from datetime import timedelta

# --- SEGURIDAD ---
SECRET_KEY = os.getenv("SECRET_KEY")
# ... (otras configuraciones)

# 🛑 CORRECCIÓN 1: Habilitar la autenticación JWT para el Guest Token
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "GUEST_TOKEN_JWT_AUTH": True
}

# 🛑 CORRECCIÓN FINAL: Forzar la URL de Audiencia del Token
# Esto anula el valor 0.0.0.0:8080 hardcodeado en entornos Docker/Gunicorn.
# La URL debe coincidir con la URL base de tu Railway.
GUEST_TOKEN_JWT_AUDIENCE = "https://superset2-production.up.railway.app/" 


# --- ROL DE INVITADO ---
# 🛑 CORRECCIÓN 2: Usar 'Gamma' (o el rol que tiene permisos de lectura de datos)
GUEST_ROLE_NAME = "Gamma"
