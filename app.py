import flet as ft
from views.login_view import login_view
from views.main_view import main_view

def main(page: ft.Page):
    page.title = "HubUIDE - Login"
    page.window.width = 400
    page.window.height = 600
    main_view(page)

    # Llamar a la vista del login
     # login_view(page)
     

ft.app(target=main)