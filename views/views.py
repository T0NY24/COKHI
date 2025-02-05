import flet as ft
from datetime import datetime
import os
from controllers.auth_controller import AuthController
from controllers.caregiver_controller import CaregiverController
from controllers.profile_controller import ProfileController
from controllers.reservas_controller import ReservasController
from controllers.admin_controller import AdminController

# Color constants
PRIMARY_COLOR = "#25523E"     # Dark green
SECONDARY_COLOR = "#6D4318"   # Brown
ACCENT_COLOR = "#F7AC5E"      # Orange
BACKGROUND_COLOR = "#FCFAFA"  # Off-white

# Admin email
ADMIN_EMAIL = "anperezcue@uide.edu.ec"

def main(page: ft.Page):
    page.title = "Cokhi - Cuidado de Mascotas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = BACKGROUND_COLOR
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 600
    page.window_height = 900
    page.update()

    # Controllers
    auth_controller = AuthController()
    caregiver_controller = CaregiverController()
    profile_controller = ProfileController()
    reserva_controller = ReservasController()
    admin_controller = AdminController()

    # Main content container
    content = ft.Column(expand=True)

    def create_card_container(content_widget):
        return ft.Container(
            content=content_widget,
            width=400,
            padding=40,
            bgcolor=BACKGROUND_COLOR,
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.with_opacity(0.2, "black")
            )
        )

    def create_styled_button(text, on_click):
        return ft.ElevatedButton(
            content=ft.Text(text, size=16, weight=ft.FontWeight.BOLD, color="white"),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                bgcolor={
                    ft.MaterialState.DEFAULT: PRIMARY_COLOR,
                    ft.MaterialState.HOVERED: ACCENT_COLOR
                }
            ),
            width=320,
            height=45,
            on_click=on_click
        )

    def create_input_field(label, icon, password=False, hint_text=""):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=PRIMARY_COLOR),
                ft.TextField(
                    label=label,
                    password=password,
                    hint_text=hint_text,
                    border_color=PRIMARY_COLOR,
                    cursor_color=PRIMARY_COLOR,
                    color=SECONDARY_COLOR,
                    expand=True,
                    text_size=14
                )
            ], spacing=10),
            padding=ft.padding.only(bottom=20)
        )

    def login_view():
        email_input = create_input_field("Correo Electrónico", ft.icons.PERSON_OUTLINE, hint_text="tu@email.com")
        password_input = create_input_field("Contraseña", ft.icons.LOCK_OUTLINE, password=True, hint_text="Ingresa tu contraseña")
        error_text = ft.Text("", color="red", size=14, visible=False)
        loading = ft.ProgressRing(width=16, height=16, stroke_width=2, color=PRIMARY_COLOR, visible=False)

        def handle_login(e):
            loading.visible = True
            error_text.visible = False
            page.update()

            email = email_input.content.controls[1].value
            password = password_input.content.controls[1].value

            if not email or not password:
                error_text.value = "Por favor completa todos los campos"
                error_text.visible = True
                loading.visible = False
                page.update()
                return

            try:
                user = auth_controller.login_user(email, password)
                if user:
                    if email == ADMIN_EMAIL:
                        update_view("admin_dashboard")
                    else:
                        update_view("main")
                else:
                    error_text.value = "Credenciales incorrectas"
                    error_text.visible = True
            except Exception as e:
                error_text.value = f"Error: {str(e)}"
                error_text.visible = True
            finally:
                loading.visible = False
                page.update()

        login_button = create_styled_button("Iniciar Sesión", handle_login)

        header = ft.Column([
            ft.Text("Cokhi", size=32, weight=ft.FontWeight.BOLD, color=PRIMARY_COLOR, text_align=ft.TextAlign.CENTER),
            ft.Text("Cuidado de Mascotas", size=16, color=SECONDARY_COLOR, text_align=ft.TextAlign.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER)

        forgot_password = ft.Container(
            content=ft.Row([
                ft.Text("¿Olvidaste tu contraseña?", size=14, color=SECONDARY_COLOR),
                ft.TextButton(
                    "Recuperar",
                    style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.DEFAULT: ACCENT_COLOR,
                            ft.MaterialState.HOVERED: PRIMARY_COLOR
                        }
                    )
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            padding=ft.padding.only(top=20)
        )

        signup_link = ft.TextButton(
            "¿No tienes cuenta? Regístrate",
            on_click=lambda _: update_view("signup"),
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: SECONDARY_COLOR,
                    ft.MaterialState.HOVERED: PRIMARY_COLOR
                }
            )
        )

        container = create_card_container(
            ft.Column([
                header,
                email_input,
                password_input,
                login_button,
                loading,
                error_text,
                forgot_password,
                signup_link
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
        )

        return ft.Container(
            content=container,
            alignment=ft.alignment.center,
            expand=True
        )

    def signup_view():
        fields = {
            "email": create_input_field("Correo Electrónico", ft.icons.EMAIL, hint_text="tu@email.com"),
            "password": create_input_field("Contraseña", ft.icons.LOCK_OUTLINE, password=True, hint_text="Crea una contraseña segura"),
            "nombre": create_input_field("Nombre", ft.icons.PERSON_OUTLINE, hint_text="Ingresa tu nombre"),
            "apellido": create_input_field("Apellido", ft.icons.PERSON_OUTLINE, hint_text="Ingresa tu apellido"),
            "telefono": create_input_field("Teléfono", ft.icons.PHONE, hint_text="Ingresa tu teléfono"),
            "ciudad": create_input_field("Ciudad", ft.icons.LOCATION_ON, hint_text="Ingresa tu ciudad"),
            "codigo_postal": create_input_field("Código Postal", ft.icons.MAP, hint_text="Ingresa tu código postal")
        }

        error_text = ft.Text("", color="red", size=14, visible=False)
        loading = ft.ProgressRing(width=16, height=16, stroke_width=2, color=PRIMARY_COLOR, visible=False)

        def handle_signup(e):
            loading.visible = True
            error_text.visible = False
            page.update()

            values = {key: field.content.controls[1].value for key, field in fields.items()}
            
            if not all(values.values()):
                error_text.value = "Por favor completa todos los campos"
                error_text.visible = True
                loading.visible = False
                page.update()
                return

            try:
                user_data = {
                    "email": values["email"],
                    "nombre": values["nombre"],
                    "apellido": values["apellido"],
                    "telefono": values["telefono"],
                    "ciudad": values["ciudad"],
                    "codigoPostal": values["codigo_postal"],
                    "fechaRegistro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                if auth_controller.signup_user(user_data, values["password"]):
                    update_view("login")
                else:
                    error_text.value = "Error al registrar usuario"
                    error_text.visible = True
            except Exception as e:
                error_text.value = f"Error: {str(e)}"
                error_text.visible = True
            finally:
                loading.visible = False
                page.update()

        signup_button = create_styled_button("Registrarse", handle_signup)

        header = ft.Column([
            ft.Text("Registro de Usuario", size=32, weight=ft.FontWeight.BOLD, color=PRIMARY_COLOR, text_align=ft.TextAlign.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER)

        login_link = ft.TextButton(
            "¿Ya tienes cuenta? Inicia Sesión",
            on_click=lambda _: update_view("login"),
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: SECONDARY_COLOR,
                    ft.MaterialState.HOVERED: PRIMARY_COLOR
                }
            )
        )

        caregiver_link = ft.TextButton(
            "¿Eres cuidador? Regístrate como cuidador",
            on_click=lambda _: update_view("signup_cuidador"),
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: SECONDARY_COLOR,
                    ft.MaterialState.HOVERED: PRIMARY_COLOR
                }
            )
        )

        container = create_card_container(
            ft.Column(
                [header] + 
                list(fields.values()) + 
                [signup_button, loading, error_text, login_link, caregiver_link],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
        )

        return ft.Container(
            content=container,
            alignment=ft.alignment.center,
            expand=True
        )

    def signup_cuidador_view():
        fields = {
            "email": create_input_field("Correo Electrónico", ft.icons.EMAIL, hint_text="tu@email.com"),
            "password": create_input_field("Contraseña", ft.icons.LOCK_OUTLINE, password=True, hint_text="Crea una contraseña segura"),
            "nombre": create_input_field("Nombre", ft.icons.PERSON_OUTLINE, hint_text="Ingresa tu nombre"),
            "apellido": create_input_field("Apellido", ft.icons.PERSON_OUTLINE, hint_text="Ingresa tu apellido"),
            "cedula": create_input_field("Cédula", ft.icons.BADGE, hint_text="Ingresa tu cédula"),
            "telefono": create_input_field("Teléfono", ft.icons.PHONE, hint_text="Ingresa tu teléfono")
        }

        error_text = ft.Text("", color="red", size=14, visible=False)
        loading = ft.ProgressRing(width=16, height=16, stroke_width=2, color=PRIMARY_COLOR, visible=False)

        def handle_signup(e):
            loading.visible = True
            error_text.visible = False
            page.update()

            values = {key: field.content.controls[1].value for key, field in fields.items()}
            
            if not all(values.values()):
                error_text.value = "Por favor completa todos los campos"
                error_text.visible = True
                loading.visible = False
                page.update()
                return

            try:
                cuidador_data = {
                    "email": values["email"],
                    "nombre": values["nombre"],
                    "apellido": values["apellido"],
                    "cedula": values["cedula"],
                    "telefono": values["telefono"],
                    "fechaRegistro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                if auth_controller.signup_caregiver(cuidador_data, values["password"]):
                    update_view("login")
                else:
                    error_text.value = "Error al registrar cuidador"
                    error_text.visible = True
            except Exception as e:
                error_text.value = f"Error: {str(e)}"
                error_text.visible = True
            finally:
                loading.visible = False
                page.update()

        signup_button = create_styled_button("Registrarse como Cuidador", handle_signup)

        header = ft.Column([
            ft.Text("Registro de Cuidador", size=32, weight=ft.FontWeight.BOLD, color=PRIMARY_COLOR, text_align=ft.TextAlign.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER)

        login_link = ft.TextButton(
            "¿Ya tienes cuenta? Inicia Sesión",
            on_click=lambda _: update_view("login"),
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: SECONDARY_COLOR,
                    ft.MaterialState.HOVERED: PRIMARY_COLOR
                }
            )
        )

        container = create_card_container(
            ft.Column(
                [header] + 
                list(fields.values()) + 
                [signup_button, loading, error_text, login_link],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
        )

        return ft.Container(
            content=container,
            alignment=ft.alignment.center,
            expand=True
        )

    def admin_dashboard():
        users = admin_controller.get_all_users()
        caregivers = admin_controller.get_all_caregivers()

        def create_data_table(data, columns, delete_action):
            return ft.DataTable(
                border=ft.border.all(1, PRIMARY_COLOR),
                border_radius=10,
                heading_row_color=ft.colors.with_opacity(0.1, PRIMARY_COLOR),
                columns=[ft.DataColumn(ft.Text(col, color=PRIMARY_COLOR)) for col in columns],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(row.get(col.lower(), "")), color=SECONDARY_COLOR))
                            for col in columns[:-1]
                        ] + [
                            ft.DataCell(
                                ft.IconButton(
                                    ft.icons.DELETE_OUTLINE,
                                    icon_color="red",
                                    data=row.get("id"),
                                    on_click=delete_action
                                )
                            )
                        ]
                    ) for row in data
                ]
            )

        def delete_user(e):
            if admin_controller.delete_user(e.control.data):
                update_view("admin_dashboard")

        def delete_caregiver(e):
            if admin_controller.delete_caregiver(e.control.data):
                update_view("admin_dashboard")

        users_table = create_data_table(
            users,
            ["Nombre", "Email", "Acciones"],
            delete_user)

        caregivers_table = create_data_table(caregivers,
            ["Nombre", "Cédula", "Email", "Teléfono", "Acciones"],
            delete_caregiver
        )

        header = ft.Text(
            "Panel de Administración",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=PRIMARY_COLOR,
            text_align=ft.TextAlign.CENTER
        )

        container = ft.Container(
            content=ft.Column([
                header,
                ft.Text("Usuarios Registrados", size=20, color=SECONDARY_COLOR, weight=ft.FontWeight.BOLD),
                users_table,
                ft.Divider(height=40, color=PRIMARY_COLOR),
                ft.Text("Cuidadores Registrados", size=20, color=SECONDARY_COLOR, weight=ft.FontWeight.BOLD),
                caregivers_table
            ], spacing=20),
            padding=40,
            bgcolor=BACKGROUND_COLOR,
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.with_opacity(0.2, "black")
            )
        )

        return container

    def main_view():
        caregivers = caregiver_controller.get_caregivers()
        if not caregivers:
            return ft.Container(
                content=ft.Text(
                    "No hay cuidadores disponibles",
                    size=20,
                    color="red",
                    text_align=ft.TextAlign.CENTER
                ),
                alignment=ft.alignment.center
            )

        current_index = [0]  # Using list to make it mutable in nested functions

        def create_caregiver_card(caregiver):
            return ft.Container(
                content=ft.Column([
                    ft.Image(
                        src=caregiver.get("image", "https://via.placeholder.com/300"),
                        width=300,
                        height=300,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(10)
                    ),
                    ft.Text(
                        f"{caregiver.get('Nombre', '')} {caregiver.get('Apellido', '')}",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY_COLOR
                    ),
                    ft.Text(
                        f"📄 Cédula: {caregiver.get('Cedula', '')}",
                        size=16,
                        color=SECONDARY_COLOR
                    ),
                    ft.Text(
                        f"📧 Email: {caregiver.get('Email', '')}",
                        size=16,
                        color=SECONDARY_COLOR
                    ),
                    ft.Text(
                        f"📞 Teléfono: {caregiver.get('Telefono', '')}",
                        size=16,
                        color=SECONDARY_COLOR
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                padding=20,
                bgcolor=BACKGROUND_COLOR,
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.colors.with_opacity(0.2, "black")
                )
            )

        def create_action_buttons():
            def handle_reject(e):
                if current_index[0] < len(caregivers) - 1:
                    current_index[0] += 1
                    update_caregiver_display()
                else:
                    result_text.value = "No hay más cuidadores disponibles"
                    page.update()

            def handle_accept(e):
                caregiver = caregivers[current_index[0]]
                reservation_id = reserva_controller.crear_reserva(
                    usuario_id="user_123",  # Este ID debería venir de la sesión actual
                    cuidador_id=caregiver["id"],
                    fecha_inicio="2025-02-01",
                    fecha_fin="2025-02-07",
                    mascota={"nombre": "Firulais", "tipo": "Perro"}
                )
                if reservation_id:
                    result_text.value = "✅ Reserva creada exitosamente"
                else:
                    result_text.value = "❌ Error al crear la reserva"
                page.update()

            return ft.Row([
                ft.ElevatedButton(
                    content=ft.Text("❌ Rechazar", color="white"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor={
                            ft.MaterialState.DEFAULT: "red",
                            ft.MaterialState.HOVERED: "#ff6666"
                        }
                    ),
                    on_click=handle_reject
                ),
                ft.ElevatedButton(
                    content=ft.Text("ℹ️ Info", color="white"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor={
                            ft.MaterialState.DEFAULT: SECONDARY_COLOR,
                            ft.MaterialState.HOVERED: ACCENT_COLOR
                        }
                    ),
                    on_click=lambda _: show_info_dialog()
                ),
                ft.ElevatedButton(
                    content=ft.Text("✅ Aceptar", color="white"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor={
                            ft.MaterialState.DEFAULT: PRIMARY_COLOR,
                            ft.MaterialState.HOVERED: ACCENT_COLOR
                        }
                    ),
                    on_click=handle_accept
                )
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

        caregiver_display = ft.Container()
        result_text = ft.Text("", color="green", size=16, text_align=ft.TextAlign.CENTER)

        def update_caregiver_display():
            if current_index[0] >= len(caregivers):
                return
            caregiver = caregivers[current_index[0]]
            caregiver_display.content = create_caregiver_card(caregiver)
            page.update()

        def show_info_dialog():
            caregiver = caregivers[current_index[0]]
            dialog = ft.AlertDialog(
                title=ft.Text("Información del Cuidador", size=20, color=PRIMARY_COLOR),
                content=ft.Column([
                    ft.Image(
                        src=caregiver.get("image", "https://via.placeholder.com/300"),
                        width=200,
                        height=200,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(10)
                    ),
                    ft.Text(
                        f"{caregiver.get('Nombre', '')} {caregiver.get('Apellido', '')}",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY_COLOR
                    ),
                    ft.Text(f"📄 Cédula: {caregiver.get('Cedula', '')}", size=16, color=SECONDARY_COLOR),
                    ft.Text(f"📧 Email: {caregiver.get('Email', '')}", size=16, color=SECONDARY_COLOR),
                    ft.Text(f"📞 Teléfono: {caregiver.get('Telefono', '')}", size=16, color=SECONDARY_COLOR),
                    ft.Text(
                        f"📅 Registrado: {caregiver.get('FechaRegistro', '')}",
                        size=16,
                        color=SECONDARY_COLOR
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                actions=[
                ft.TextButton("Cerrar", on_click=lambda e: (setattr(page.dialog, "open", False), page.update()))
]

            )
            page.dialog = dialog
            dialog.open = True
            page.update()

        # Inicializar la vista
        update_caregiver_display()

        return ft.Container(
            content=ft.Column([
                caregiver_display,
                create_action_buttons(),
                result_text
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            padding=20
        )

    def profile_view(user_id):
        user_data = profile_controller.get_user_profile(user_id)
        if not user_data:
            return ft.Container(
                content=ft.Text(
                    "Error al cargar el perfil",
                    size=20,
                    color="red",
                    text_align=ft.TextAlign.CENTER
                ),
                alignment=ft.alignment.center
            )

        image_path = user_data.get("FotoPerfil", "https://via.placeholder.com/150")

        fields = {
            "nombre": create_input_field("Nombre", ft.icons.PERSON_OUTLINE),
            "apellido": create_input_field("Apellido", ft.icons.PERSON_OUTLINE),
            "telefono": create_input_field("Teléfono", ft.icons.PHONE),
            "ciudad": create_input_field("Ciudad", ft.icons.LOCATION_ON)
        }

        for key, field in fields.items():
            field.content.controls[1].value = user_data.get(key.capitalize(), "")

        error_text = ft.Text("", color="red", size=14, visible=False)
        success_text = ft.Text("", color="green", size=14, visible=False)

        def handle_update_profile(e):
            values = {key: field.content.controls[1].value for key, field in fields.items()}
            
            if not all(values.values()):
                error_text.value = "Por favor completa todos los campos"
                error_text.visible = True
                success_text.visible = False
                page.update()
                return

            try:
                if profile_controller.update_user_profile(user_id, values):
                    success_text.value = "✅ Perfil actualizado exitosamente"
                    success_text.visible = True
                    error_text.visible = False
                else:
                    error_text.value = "❌ Error al actualizar el perfil"
                    error_text.visible = True
                    success_text.visible = False
            except Exception as e:
                error_text.value = f"❌ Error: {str(e)}"
                error_text.visible = True
                success_text.visible = False
            page.update()

        update_button = create_styled_button("Guardar Cambios", handle_update_profile)

        container = create_card_container(
            ft.Column([
                ft.Image(
                    src=image_path,
                    width=150,
                    height=150,
                    fit=ft.ImageFit.COVER,
                    border_radius=ft.border_radius.all(75)
                ),
                *fields.values(),
                ft.Text(
                    f"📧 Email: {user_data.get('Email', '')}",
                    size=16,
                    color=SECONDARY_COLOR
                ),
                update_button,
                error_text,
                success_text
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
        )

        return ft.Container(
            content=container,
            alignment=ft.alignment.center,
            expand=True
        )

    def update_view(view_name):
        content.controls.clear()
        
        if view_name == "login":
            content.controls.append(login_view())
        elif view_name == "admin_dashboard":
            content.controls.append(admin_dashboard())
        elif view_name == "signup":
            content.controls.append(signup_view())
        elif view_name == "signup_cuidador":
            content.controls.append(signup_cuidador_view())
        elif view_name == "main":
            content.controls.append(main_view())
        elif view_name == "profile":
            content.controls.append(profile_view("tcp4dtDtjYV8hCCACDNfunjmdYt1"))  
        else:
            content.controls.append(
                ft.Text(
                    "Página no encontrada",
                    size=20,
                    color="red",
                    text_align=ft.TextAlign.CENTER
                )
            )
        
        page.update()

    # Configuración inicial
    page.add(content)
    update_view("login")

if __name__ == "__main__":
    ft.app(target=main)