import flet as ft
from controllers.auth_controller import AuthController
from datetime import datetime

# Definición global de colores
PRIMARY_COLOR = "#25523E"
SECONDARY_COLOR = "#6D4318"
ACCENT_COLOR = "#F7AC5E"
BACKGROUND_COLOR = "#FCFAFA"

def login_view(page):
    page.title = "Cokhi - Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def handle_login(email, password):
        controller = AuthController()
        if controller.login_user(email, password):
            page.snack_bar = ft.SnackBar(ft.Text("Inicio de sesión exitoso"), bgcolor=PRIMARY_COLOR)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Credenciales inválidas"), bgcolor="red")
        page.snack_bar.open = True
        page.update()

    def show_signup_view():
        page.controls.clear()
        signup_view(page)
        page.update()

    # UI del login
    email_input = ft.TextField(
        label="Correo Electrónico",
        hint_text="tu@email.com",
        prefix_icon=ft.icons.EMAIL,
        border_color=PRIMARY_COLOR,
    )
    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        hint_text="Ingresa tu contraseña",
        prefix_icon=ft.icons.LOCK,
        border_color=PRIMARY_COLOR,
    )
    login_button = ft.ElevatedButton(
        "Iniciar Sesión",
        bgcolor=PRIMARY_COLOR,
        color="white",
        style=ft.ButtonStyle(
            overlay_color={"hovered": ACCENT_COLOR, "pressed": PRIMARY_COLOR}
        ),
        on_click=lambda _: handle_login(email_input.value, password_input.value),
    )
    signup_button = ft.TextButton(
        "¿No tienes una cuenta? Regístrate.",
        on_click=lambda _: show_signup_view(),
        style=ft.ButtonStyle(color=ACCENT_COLOR),
    )

    # Layout principal
    login_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Cokhi", size=32, weight="bold", color=PRIMARY_COLOR),
                ft.Text("Cuidado de Mascotas", size=16, color=SECONDARY_COLOR),
                email_input,
                password_input,
                login_button,
                signup_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=20,
        width=400,
        border_radius=10,
        bgcolor=BACKGROUND_COLOR,
        shadow=ft.BoxShadow(blur_radius=15, spread_radius=5, color="rgba(0,0,0,0.1)"),
    )

    # Añadir contenedor al page
    page.add(
        ft.Container(
            content=ft.Row(
                [login_container],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=BACKGROUND_COLOR,
            expand=True,
        )
    )

def signup_view(page):
    def handle_signup():
        controller = AuthController()
        
        # Prepare user data dictionary con los nuevos campos
        usuario_data = {
            'email': email_input.value,
            'nombre': nombre_input.value,
            'apellido': apellido_input.value,
            'telefono': telefono_input.value,
            'ciudad': ciudad_input.value,
            'codigoPostal': codigo_postal_input.value,
            'fechaRegistro': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Formato de fecha
        }

        # Validar campos
        if not all([
            email_input.value, 
            password_input.value, 
            nombre_input.value, 
            apellido_input.value, 
            telefono_input.value,
            ciudad_input.value,
            codigo_postal_input.value
        ]):
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, complete todos los campos"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        if controller.signup_user(usuario_data, password_input.value):
            page.snack_bar = ft.SnackBar(ft.Text("Cuenta creada con éxito"), bgcolor=PRIMARY_COLOR)
            show_login_view()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al crear la cuenta"), bgcolor="red")
        page.snack_bar.open = True
        page.update()

    def show_login_view():
        page.controls.clear()
        login_view(page)
        page.update()

    def show_cuidador_signup_view():
        page.controls.clear()
        cuidador_signup_view(page)
        page.update()

    # Campos de registro extendidos con los nuevos datos
    email_input = ft.TextField(
        label="Correo Electrónico",
        hint_text="tu@email.com",
        prefix_icon=ft.icons.EMAIL,
        border_color=PRIMARY_COLOR,
    )
    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        hint_text="Crea una contraseña segura",
        prefix_icon=ft.icons.LOCK,
        border_color=PRIMARY_COLOR,
    )
    nombre_input = ft.TextField(
        label="Nombre",
        hint_text="Ingresa tu nombre",
        border_color=PRIMARY_COLOR,
    )
    apellido_input = ft.TextField(
        label="Apellido",
        hint_text="Ingresa tu apellido",
        border_color=PRIMARY_COLOR,
    )
    telefono_input = ft.TextField(
        label="Teléfono",
        hint_text="Ingresa tu teléfono",
        border_color=PRIMARY_COLOR,
    )
    ciudad_input = ft.TextField(
        label="Ciudad",
        hint_text="Ingresa tu ciudad",
        border_color=PRIMARY_COLOR,
    )
    codigo_postal_input = ft.TextField(
        label="Código Postal",
        hint_text="Ingresa tu código postal",
        border_color=PRIMARY_COLOR,
    )
    
    signup_button = ft.ElevatedButton(
        "Registrarse",
        bgcolor=PRIMARY_COLOR,
        color="white",
        style=ft.ButtonStyle(
            overlay_color={"hovered": ACCENT_COLOR, "pressed": PRIMARY_COLOR}
        ),
        on_click=lambda _: handle_signup(),
    )

    # Buttons for login and caregiver registration
    login_button = ft.TextButton(
        "¿Ya tienes una cuenta? Inicia Sesión.",
        on_click=lambda _: show_login_view(),
        style=ft.ButtonStyle(color=ACCENT_COLOR),
    )
    caregiver_button = ft.TextButton(
        "¿Eres cuidador? Regístrate como cuidador.",
        on_click=lambda _: show_cuidador_signup_view(),
        style=ft.ButtonStyle(color=SECONDARY_COLOR),
    )

    signup_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Cokhi", size=32, weight="bold", color=PRIMARY_COLOR),
                ft.Text("Regístrate para continuar", size=16, color=SECONDARY_COLOR),
                email_input,
                password_input,
                nombre_input,
                apellido_input,
                telefono_input,
                ciudad_input,
                codigo_postal_input,
                signup_button,
                ft.Column(  # Wrap buttons in a Column to stack them
                    [
                        login_button,
                        caregiver_button
                    ],
                    spacing=10,  # Add some space between buttons
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=20,
        width=500,
        border_radius=10,
        bgcolor=BACKGROUND_COLOR,
        shadow=ft.BoxShadow(blur_radius=15, spread_radius=5, color="rgba(0,0,0,0.1)"),
    )

    page.add(
        ft.Container(
            content=ft.Row([signup_container], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=BACKGROUND_COLOR,
            expand=True,
        )
    )

import flet as ft
from controllers.auth_controller import AuthController
from datetime import datetime

# Definición global de colores
PRIMARY_COLOR = "#25523E"
SECONDARY_COLOR = "#6D4318"
ACCENT_COLOR = "#F7AC5E"
BACKGROUND_COLOR = "#FCFAFA"

def cuidador_signup_view(page):
    page.title = "Cokhi - Registro Cuidador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def handle_cuidador_signup():
        controller = AuthController()

        # Datos del cuidador
        cuidador_data = {
            'nombre': nombre_input.value,
            'apellido': apellido_input.value,
            'cedula': cedula_input.value,
            'email': email_input.value,
            'telefono': telefono_input.value,
            'fechaRegistro': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

        # Validación de los campos
        if not all([
            email_input.value, 
            password_input.value, 
            nombre_input.value, 
            apellido_input.value, 
            cedula_input.value,
            telefono_input.value
        ]):
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, complete todos los campos"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        # Intentar registrar al cuidador
        if controller.signup_caregiver(cuidador_data, password_input.value):
            page.snack_bar = ft.SnackBar(ft.Text("Cuenta de cuidador creada con éxito"), bgcolor=PRIMARY_COLOR)
            show_login_view()  # Cambiar a vista de login
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al crear la cuenta de cuidador"), bgcolor="red")
        page.snack_bar.open = True
        page.update()

    def show_login_view():
        page.controls.clear()
        login_view(page)
        page.update()

    # UI del registro del cuidador
    email_input = ft.TextField(
        label="Correo Electrónico",
        hint_text="tu@email.com",
        prefix_icon=ft.icons.EMAIL,
        border_color=PRIMARY_COLOR,
    )
    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        hint_text="Crea una contraseña segura",
        prefix_icon=ft.icons.LOCK,
        border_color=PRIMARY_COLOR,
    )
    nombre_input = ft.TextField(
        label="Nombre",
        hint_text="Ingresa tu nombre",
        border_color=PRIMARY_COLOR,
    )
    apellido_input = ft.TextField(
        label="Apellido",
        hint_text="Ingresa tu apellido",
        border_color=PRIMARY_COLOR,
    )
    cedula_input = ft.TextField(
        label="Cédula",
        hint_text="Ingresa tu cédula",
        border_color=PRIMARY_COLOR,
    )
    telefono_input = ft.TextField(
        label="Teléfono",
        hint_text="Ingresa tu teléfono",
        border_color=PRIMARY_COLOR,
    )

    signup_button = ft.ElevatedButton(
        "Registrarse como Cuidador",
        bgcolor=PRIMARY_COLOR,
        color="white",
        style=ft.ButtonStyle(
            overlay_color={"hovered": ACCENT_COLOR, "pressed": PRIMARY_COLOR}
        ),
        on_click=lambda _: handle_cuidador_signup(),
    )

    login_button = ft.TextButton(
        "¿Ya tienes una cuenta? Inicia Sesión.",
        on_click=lambda _: show_login_view(),
        style=ft.ButtonStyle(color=ACCENT_COLOR),
    )

    # Contenedor principal del registro de cuidador
    signup_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Cokhi", size=32, weight="bold", color=PRIMARY_COLOR),
                ft.Text("Regístrate como Cuidador", size=16, color=SECONDARY_COLOR),
                email_input,
                password_input,
                nombre_input,
                apellido_input,
                cedula_input,
                telefono_input,
                signup_button,
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=20,
        width=500,
        border_radius=10,
        bgcolor=BACKGROUND_COLOR,
        shadow=ft.BoxShadow(blur_radius=15, spread_radius=5, color="rgba(0,0,0,0.1)"),
    )

    page.add(
        ft.Container(
            content=ft.Row([signup_container], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=BACKGROUND_COLOR,
            expand=True,
        )
    )