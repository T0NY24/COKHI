import flet as ft
from controllers.auth_controller import AuthController
from datetime import datetime

# 🎨 Definición de colores
PRIMARY_COLOR = "#25523E"
SECONDARY_COLOR = "#6D4318"
ACCENT_COLOR = "#F7AC5E"
BACKGROUND_COLOR = "#FCFAFA"

def login_view(page):
    """📌 Vista de Login"""
    page.title = "Cokhi - Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    controller = AuthController()

    email_input = ft.TextField(label="Correo Electrónico", hint_text="tu@email.com", prefix_icon=ft.icons.EMAIL, border_color=PRIMARY_COLOR)
    password_input = ft.TextField(label="Contraseña", password=True, hint_text="Ingresa tu contraseña", prefix_icon=ft.icons.LOCK, border_color=PRIMARY_COLOR)
    error_text = ft.Text("", color="red")

    def handle_login(e):
        user = controller.login_user(email_input.value, password_input.value)
        if user:
            page.go("/main")  # Redirigir a la pantalla principal
        else:
            error_text.value = "❌ Credenciales inválidas"
            page.update()

    login_button = ft.ElevatedButton("Iniciar Sesión", bgcolor=PRIMARY_COLOR, color="white", on_click=handle_login)
    signup_button = ft.TextButton("¿No tienes cuenta? Regístrate.", on_click=lambda _: page.go("/register"))

    return ft.Column([
        ft.Text("Bienvenido a Cokhi 🐶", size=24, weight="bold"),
        email_input,
        password_input,
        login_button,
        signup_button,
        error_text
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

def signup_view(page):
    """📌 Registro de Usuario"""
    page.title = "Registro - Usuario"
    controller = AuthController()

    email_input = ft.TextField(label="Correo Electrónico", hint_text="tu@email.com", prefix_icon=ft.icons.EMAIL, border_color=PRIMARY_COLOR)
    password_input = ft.TextField(label="Contraseña", password=True, hint_text="Crea una contraseña segura", prefix_icon=ft.icons.LOCK, border_color=PRIMARY_COLOR)
    nombre_input = ft.TextField(label="Nombre", hint_text="Ingresa tu nombre", border_color=PRIMARY_COLOR)
    apellido_input = ft.TextField(label="Apellido", hint_text="Ingresa tu apellido", border_color=PRIMARY_COLOR)
    telefono_input = ft.TextField(label="Teléfono", hint_text="Ingresa tu teléfono", border_color=PRIMARY_COLOR)
    ciudad_input = ft.TextField(label="Ciudad", hint_text="Ingresa tu ciudad", border_color=PRIMARY_COLOR)
    error_text = ft.Text("", color="red")

    def handle_signup(e):
        usuario_data = {
            'email': email_input.value,
            'nombre': nombre_input.value,
            'apellido': apellido_input.value,
            'telefono': telefono_input.value,
            'ciudad': ciudad_input.value,
            'fechaRegistro': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

        if controller.signup_user(usuario_data, password_input.value):
            page.go("/")  # Redirigir al login
        else:
            error_text.value = "❌ Error al registrar usuario"
            page.update()

    signup_button = ft.ElevatedButton("Registrarse", bgcolor=PRIMARY_COLOR, color="white", on_click=handle_signup)
    login_button = ft.TextButton("¿Ya tienes una cuenta? Inicia Sesión.", on_click=lambda _: page.go("/"))

    return ft.Column([
        ft.Text("Registro de Usuario", size=24, weight="bold"),
        email_input,
        password_input,
        nombre_input,
        apellido_input,
        telefono_input,
        ciudad_input,
        signup_button,
        login_button,
        error_text
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

def cuidador_signup_view(page):
    """📌 Registro de Cuidador"""
    page.title = "Registro - Cuidador"
    controller = AuthController()

    email_input = ft.TextField(label="Correo Electrónico", hint_text="tu@email.com", prefix_icon=ft.icons.EMAIL, border_color=PRIMARY_COLOR)
    password_input = ft.TextField(label="Contraseña", password=True, hint_text="Crea una contraseña segura", prefix_icon=ft.icons.LOCK, border_color=PRIMARY_COLOR)
    nombre_input = ft.TextField(label="Nombre", hint_text="Ingresa tu nombre", border_color=PRIMARY_COLOR)
    apellido_input = ft.TextField(label="Apellido", hint_text="Ingresa tu apellido", border_color=PRIMARY_COLOR)
    cedula_input = ft.TextField(label="Cédula", hint_text="Ingresa tu cédula", border_color=PRIMARY_COLOR)
    telefono_input = ft.TextField(label="Teléfono", hint_text="Ingresa tu teléfono", border_color=PRIMARY_COLOR)
    error_text = ft.Text("", color="red")

    def handle_cuidador_signup(e):
        cuidador_data = {
            'nombre': nombre_input.value,
            'apellido': apellido_input.value,
            'cedula': cedula_input.value,
            'email': email_input.value,
            'telefono': telefono_input.value,
            'fechaRegistro': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

        if controller.signup_caregiver(cuidador_data, password_input.value):
            page.go("/")  # Redirigir al login
        else:
            error_text.value = "❌ Error al registrar cuidador"
            page.update()

    signup_button = ft.ElevatedButton("Registrarse como Cuidador", bgcolor=PRIMARY_COLOR, color="white", on_click=handle_cuidador_signup)
    login_button = ft.TextButton("¿Ya tienes una cuenta? Inicia Sesión.", on_click=lambda _: page.go("/"))

    return ft.Column([
        ft.Text("Registro de Cuidador", size=24, weight="bold"),
        email_input,
        password_input,
        nombre_input,
        apellido_input,
        cedula_input,
        telefono_input,
        signup_button,
        login_button,
        error_text
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
