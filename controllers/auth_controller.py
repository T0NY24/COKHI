from firebase_config.config import auth_service

def login_user(email, password):
    try:
        user = auth_service.get_user_by_email(email)
        # Simular autenticación (Firebase Admin no maneja contraseñas directamente)
        if password == "correct_password":  # Reemplaza con lógica real
            return "success"
        return "Contraseña incorrecta"
    except Exception as e:
        return f"Error: {str(e)}"
