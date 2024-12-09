import flet as ft

from views.auth_view import login_view

def main(page: ft.Page):
    page.title = "HubUIDE - Login"
    page.window.width = 600
    page.window.height = 900

    #usuario_view
    login_view(page)

ft.app(target=main)