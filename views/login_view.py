import flet as ft
from controllers import auth_controller
def login_view(page):
    # Crear campos de texto y botón como variables locales dentro de `login_view`
    email_field = ft.TextField(
        label="Correo Electrónico",
        hint_text="Ingresa tu correo",
        width=300
    )
    password_field = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa tu contraseña",
        password=True,
        width=300
    )

    def handle_login(e):
        # Usar las variables locales `email_field` y `password_field` para acceder a los valores
        email = email_field.value
        password = password_field.value

        if not email or not password:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, llena todos los campos."),
                bgcolor=ft.colors.RED
            )
            page.snack_bar.open = True
            page.update()
            return

        # Llamar al controlador para autenticar
        result = AuthController().login_user(email, password)
        page.snack_bar = ft.SnackBar(
            ft.Text(result["message"]),
            bgcolor=ft.colors.GREEN if result["status"] == "success" else ft.colors.RED
        )
        page.snack_bar.open = True
        page.update()

    # Crear logo
    logo = ft.Image(
        src="static/logo.png",
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN
    )

    # Botón de login
    login_button = ft.ElevatedButton(
        text="Iniciar Sesión",
        width=300,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=handle_login
    )

    # Footer con enlace
    footer = ft.Row(
        [
            ft.Text("¿No tienes una cuenta?"),
            ft.TextButton(
                "Regístrate aquí",
                on_click=lambda e: page.snack_bar.show(ft.Text("Función de registro no implementada."))
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Contenedor principal
    page.add(
        ft.Column(
            [
                logo,
                ft.Text("Bienvenido a HubUIDE", size=24, weight="bold", text_align="center"),
                email_field,
                password_field,
                login_button,
                footer
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
