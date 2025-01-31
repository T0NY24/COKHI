import flet as ft
from views.auth_view import login_view, signup_view, cuidador_signup_view  # Vistas de autenticación
from views.main_page import main_page  # Pantalla principal (tipo Tinder)
from views.user_view import user_view  # Gestión de usuarios
from views.caregiver_view import caregiver_view  # Gestión de cuidadores
from views.reservas_view import reservas_view  # Gestión de reservas
from views.profile_view import profile_view  # Perfil de usuario

def route_change(page: ft.Page):
    """📌 Maneja el cambio de rutas en la app."""

    page.views.clear()  # Limpia la vista actual
    route = page.route if page.route else "/"

    # Diccionario de rutas y sus vistas asociadas
    routes = {
        "/": lambda p: login_view(p),
        "/register": lambda p: signup_view(p),
        "/register_cuidador": lambda p: cuidador_signup_view(p),
        "/main": lambda p: main_page(p),
        "/usuarios": lambda p: user_view(p),
        "/cuidadores": lambda p: caregiver_view(p),
        "/reservas": lambda p: reservas_view(p),
        "/perfil": lambda p: profile_view(p, "tcp4dtDtjYV8hCCACDNfunjmdYt1"),  # ⚠️ ID dinámico
    }

    # Agregar la vista si la ruta existe, de lo contrario ir a login
    if route in routes:
        page.views.append(ft.View(route, controls=[routes[route](page)]))
    else:
        page.views.append(ft.View("/", controls=[login_view(page)]))
        page.go("/")  # Redirigir a login si la ruta no es válida

    page.update()
