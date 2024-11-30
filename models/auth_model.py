# models/auth_model.py

from firebase_admin import auth

def authenticate_user(email: str, password: str):
    """Función para autenticar al usuario con su correo y contraseña."""
    try:

        user = auth.get_user_by_email(email)
        return user
    except auth.AuthError as e:
        return None
