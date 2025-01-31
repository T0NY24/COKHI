import flet as ft
from views.views import main  # ✅ Importa `main`
#from views.main_page import main_page
#from views.profile_view import profile_view
#from views.user_view import user_view
#from views.admin_dashboard import admin_dashboard
if __name__ == "__main__":
    ft.app(target=main)  # ✅ Llama a `main`
