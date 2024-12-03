# views/auth_view.py
import flet as ft
from controllers.auth_controller import AuthController

def login_view(page):
    page.title = "HubUide - Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Elementos de la UI
    email_input = ft.TextField(label="Email", autofocus=True)
    password_input = ft.TextField(label="Password", password=True)
    login_button = ft.ElevatedButton("Login", on_click=lambda e: handle_login(email_input.value, password_input.value))
    signup_button = ft.TextButton("Don't have an account? Sign up.", on_click=lambda e: show_signup_view(page))

    page.add(email_input, password_input, login_button, signup_button)

    def handle_login(email, password):
        controller = AuthController()
        if controller.login_user(email, password):
            page.add(ft.Text("Login successful"))
        else:
            page.add(ft.Text("Invalid credentials"))

def signup_view(page):
    page.title = "HubUide - Sign Up"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Elementos de la UI
    email_input = ft.TextField(label="Email", autofocus=True)
    password_input = ft.TextField(label="Password", password=True)
    signup_button = ft.ElevatedButton("Sign Up", on_click=lambda e: handle_signup(email_input.value, password_input.value))
    login_button = ft.TextButton("Already have an account? Login.", on_click=lambda e: show_login_view(page))

    page.add(email_input, password_input, signup_button, login_button)

    def handle_signup(email, password):
        controller = AuthController()
        if controller.signup_user(email, password):
            page.add(ft.Text("Account created successfully"))
        else:
            page.add(ft.Text("Failed to create account"))

def show_signup_view(page):
    page.controls.clear()
    signup_view(page)

def show_login_view(page):
    page.controls.clear()
    login_view(page)
