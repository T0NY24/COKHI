# main.py
import flet as ft
from views.login_view import login_view
from controllers.auth_controller import login_controller

# Inicializar Firebase con la configuración
import firebase_config  # Esto carga las configuraciones de Firebase

def main(page: ft.Page):
    # Definir los campos y el botón
    email_field = ft.TextField(label="Correo electrónico", autofocus=True)
    password_field = ft.PasswordField(label="Contraseña")
    message_label = ft.Text("", color="red")

    login_button = ft.ElevatedButton("Iniciar sesión", on_click=lambda e: login_controller(page, email_field.value, password_field.value, message_label))

    # Llamamos a la vista de login
    login_view(page, email_field, password_field, message_label, login_button)

# Ejecutar la app
ft.app(target=main)
