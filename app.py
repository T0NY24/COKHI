import flet as ft
#from views.auth_view import login_view
#from models.caregiver_model import caregiver_data
#from controllers.caregiver_controller import on_info, on_accept, on_reject
#from views.main_page import main_page
#from views.user_view import user_view
#from views.caregiver_view import caregiver_view
#from views.reservas_view import reservas_view
from views.profile_view import profile_view

"""
def main(page: ft.Page):
    page.title = "HubUIDE - Login"
    page.window.width = 600
    page.window.height = 900

    #usuario_view
    login_view(page)

ft.app(target=main)
"""

"""
def main(page: ft.Page):
    page.title = "HubUIDE - Main"
    page.window.width = 600
    page.window.height = 900
    # Pasa los datos del primer cuidador y las funciones de callback
    main_view(page, caregiver_data[0], on_info, on_accept, on_reject)

ft.app(target=main)
"""

def main(page: ft.Page):
    profile_view(page)