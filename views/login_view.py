# views/login_view.py
import flet as ft

def login_view(page: ft.Page, email_field, password_field, message_label, login_button):
    """Crea la vista del formulario de login."""
    page.title = "Login HubUIDE"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.add(
        ft.Column(
            [
                ft.Text("Bienvenido a HubUIDE", size=30, weight=ft.FontWeight.BOLD),
                email_field,
                password_field,
                login_button,
                message_label,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
