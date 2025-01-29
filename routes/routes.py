import flet as ft
from views.auth_view import login_view
from views.main_view import main_view

def views_handler(page):
    return {
        "/": ft.View(  # Ruta inicial que carga el login
            route="/",
            controls=[login_view(page)]
        ),
        "/login_view": ft.View(
            route="/login_view",
            controls=[login_view(page)]
        ),
        "/profile": ft.View(
            route="/profile",
            controls=[
                main_view(page, page.route.split("=")[1]) if "=" in page.route else ft.Text("Error: ID de usuario no especificado.")
            ]
        )
    }
