import flet as ft
from views.login_view import login_view
from views.home_view import home_view
from views.settings_view import settings_view

def main(page: ft.Page):
    page.title = "HubUide"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Navegación entre vistas
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(login_view(page))
        elif page.route == "/home":
            page.views.append(home_view(page))
        elif page.route == "/settings":
            page.views.append(settings_view(page))
        page.update()

    page.on_route_change = route_change
    page.go("/")  # Comienza en la pantalla de login

ft.app(target=main)
