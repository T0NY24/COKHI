from firebase_admin import auth
from controllers.firebase_manager import FirebaseManager

class LoginController:
    def __init__(self):
        self.firebase_manager = FirebaseManager()

    def login_user(self, email, password):
        """
        Simula un inicio de sesión usando Firebase Admin.
        Firebase Admin no permite validar contraseñas directamente.
        Por lo tanto, aquí verificamos si el email existe como usuario registrado.
        """
        try:
            # Verificar si el usuario existe
            user = auth.get_user_by_email(email)
            # Por ahora no podemos verificar la contraseña con Firebase Admin
            # Necesitarás agregar lógica adicional en el backend o usar Firebase JS SDK para el frontend
            return {
                "status": "success",
                "message": f"Bienvenido, {user.display_name or user.email}!"
            }
        except auth.UserNotFoundError:
            return {
                "status": "error",
                "message": "Usuario no encontrado. Verifica tu correo."
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error: {str(e)}"
            }

    def register_user(self, email, password, display_name=None):
        """
        Registra un nuevo usuario en Firebase Authentication.
        """
        try:
            user = auth.create_user(
                email=email,
                password=password,
                display_name=display_name
            )
            return {
                "status": "success",
                "message": f"Usuario {user.email} registrado exitosamente."
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error al registrar usuario: {str(e)}"
            }