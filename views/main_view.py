import flet as ft
from models.user_model import UserModel

def main_view(page):
    page.title = "HubUide"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Obtenemos un usuario aleatorio
    user = UserModel.get_random_user()

    # Mostrar perfil del usuario
    photo = ft.Image(src=user.photo_url, width=200, height=200)
    name = ft.Text(user.name, size=24, weight=ft.FontWeight.BOLD)
    bio = ft.Text(user.bio, size=16)
    interests = ft.Text(", ".join(user.interests), size=14)

    # Botones de interacción (deslizar a la derecha o izquierda)
    like_button = ft.IconButton(ft.icons.THUMB_UP, on_click=lambda e: handle_like(user))
    dislike_button = ft.IconButton(ft.icons.THUMB_DOWN, on_click=lambda e: handle_dislike(user))

    page.add(
        photo,
        name,
        bio,
        interests,
        ft.Row([like_button, dislike_button], alignment=ft.MainAxisAlignment.CENTER),
    )

def handle_like(user):
    print(f"Te ha gustado {user.name}")

def handle_dislike(user):
    print(f"No te ha gustado {user.name}")
