import flet as ft
from controllers.auth_controller import login_user

def login_view(page):
    email = ft.TextField(label="Correo electrónico")
    password = ft.TextField(label="Contraseña", password=True)
    error_msg = ft.Text(color=ft.colors.RED)

    def on_login(e):
        result = login_user(email.value, password.value)
        if result == "success":
            page.go("/home")
        else:
            error_msg.value = result
            page.update()

    return ft.View(
        "/",
        controls=[
            ft.Text("Login", size=30),
            email,
            password,
            ft.ElevatedButton("Iniciar sesión", on_click=on_login),
            error_msg,
        ],
    )
