import flet as ft
from views.login_view import login_view
from views.auth_view import login_view
from views.usuario_view import usuario_view

def main(page: ft.Page):
    page.title = "HubUIDE - Login"
    page.window.width = 600
    page.window.height = 800

    
    login_view(page)

ft.app(target=main)