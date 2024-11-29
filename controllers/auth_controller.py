# controllers/auth_controller.py
from models.auth_model import authenticate_user

def login_controller(page, email, password, message_label):
    """Controlador que maneja la interacción para hacer login."""
    user = authenticate_user(email, password)
    if user:
        message_label.value = f"Bienvenido {user.email}!"
    else:
        message_label.value = "Error: Usuario no encontrado o contraseña incorrecta."
    page.update()
