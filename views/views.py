import flet as ft
from controllers.auth_controller import AuthController
from controllers.caregiver_controller import CaregiverController
from controllers.profile_controller import ProfileController
from controllers.reservas_controller import ReservasController
from controllers.admin_controller import AdminController

import os
from datetime import datetime

# 🎨 Definición de colores
PRIMARY_COLOR = "#25523E"
SECONDARY_COLOR = "#6D4318"
ACCENT_COLOR = "#F7AC5E"
BACKGROUND_COLOR = "#FCFAFA"

# 📌 Correo del Administrador
ADMIN_EMAIL = "anperezcue@uide.edu.ec"

def main(page):
    page.title = "Cokhi - Cuidado de Mascotas"
    page.theme_mode = ft.ThemeMode.LIGHT  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    auth_controller = AuthController()
    caregiver_controller = CaregiverController()
    profile_controller = ProfileController()
    reserva_controller = ReservasController()
    admin_controller = AdminController()

    content = ft.Column(expand=True)

    def update_view(view_name):
        """Actualiza dinámicamente la vista en la misma página"""
        content.controls.clear()

        if view_name == "login":
            content.controls.append(login_view())
        elif view_name == "admin_dashboard":
            content.controls.append(admin_dashboard())  # ❌ SE CORRIGIÓ, AHORA NO PASA ARGUMENTOS
        elif view_name == "signup":
            content.controls.append(signup_view())
        elif view_name == "signup_cuidador":
            content.controls.append(cuidador_signup_view())
        elif view_name == "main":
            content.controls.append(main_view())
        elif view_name == "profile":
            content.controls.append(profile_view("GUeE4UPyoqYcgt7zwkpRC3E5c4H3"))
        else:
            content.controls.append(ft.Text("Página no encontrada", size=20, color="red"))

        page.update()

    def login_view():
        email_input = ft.TextField(
            label="Correo Electrónico",
            hint_text="tu@email.com",
            border_color=PRIMARY_COLOR,
            cursor_color=PRIMARY_COLOR
        )
        password_input = ft.TextField(
            label="Contraseña",
            password=True,
            hint_text="Ingresa tu contraseña",
            border_color=PRIMARY_COLOR,
            cursor_color=PRIMARY_COLOR
        )
        error_text = ft.Text("", color="red")
        loading_indicator = ft.ProgressRing(visible=False, width=16, height=16)

        def handle_login(e):
            """Maneja el inicio de sesión"""
            loading_indicator.visible = True
            error_text.value = ""
            page.update()

            try:
                # Validaciones básicas
                if not email_input.value or not password_input.value:
                    error_text.value = "❌ Por favor completa todos los campos"
                    loading_indicator.visible = False
                    page.update()
                    return

                # Intenta el login
                user = auth_controller.login_user(email_input.value, password_input.value)

                if user:
                    error_text.color = "green"
                    error_text.value = "✅ Inicio de sesión exitoso"
                    page.update()

                    # 📌 Verificar si es el administrador
                    if email_input.value == ADMIN_EMAIL:
                        update_view("admin_dashboard")
                        return  # ⬅ SE AGREGA RETURN PARA QUE NO SIGA A "main"

                    # Si no es admin, redirigir a la vista normal
                    update_view("main")
                else:
                    error_text.value = "❌ Correo electrónico o contraseña incorrectos"
                    loading_indicator.visible = False
                    page.update()
                    
            except Exception as e:
                error_text.value = f"❌ Error al iniciar sesión: {str(e)}"
                loading_indicator.visible = False
                page.update()

        return ft.Column([
            ft.Text("Bienvenido a Cokhi 🐶", size=24, weight="bold"),
            email_input,
            password_input,
            ft.Row([
                ft.ElevatedButton(
                    "Iniciar Sesión",
                    bgcolor=PRIMARY_COLOR,
                    color="white",
                    on_click=handle_login
                ),
                loading_indicator
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.TextButton(
                "¿No tienes cuenta? Regístrate.",
                on_click=lambda _: update_view("signup")
            ),
            error_text
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    def admin_dashboard():
        """📌 Vista del panel de administración"""
        page.title = "Panel de Administración"

        # 📂 Obtener listas de usuarios y cuidadores
        users = admin_controller.get_all_users()
        caregivers = admin_controller.get_all_caregivers()

        # 📌 Función para eliminar usuario
        def delete_user(e):
            user_id = e.control.data
            if admin_controller.delete_user(user_id):
                page.dialog = ft.AlertDialog(title=ft.Text("✅ Usuario eliminado con éxito"))
                page.update()
            else:
                page.dialog = ft.AlertDialog(title=ft.Text("⚠️ Error al eliminar usuario"))
            page.update()

        # 📌 Función para eliminar cuidador
        def delete_caregiver(e):
            caregiver_id = e.control.data
            if admin_controller.delete_caregiver(caregiver_id):
                page.dialog = ft.AlertDialog(title=ft.Text("✅ Cuidador eliminado con éxito"))
                page.update()
            else:
                page.dialog = ft.AlertDialog(title=ft.Text("⚠️ Error al eliminar cuidador"))
            page.update()

        # 📌 Tabla de usuarios
        users_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Email")),
                ft.DataColumn(ft.Text("Acciones"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(user.get("Nombre", "Sin Nombre"))),
                        ft.DataCell(ft.Text(user.get("CorreoElectronico", "Sin Email"))),
                        ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, on_click=delete_user, data=user.get("id")))
                    ]
                ) for user in users
            ]
        )

        # 📌 Tabla de cuidadores
        caregivers_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Cédula")),
                ft.DataColumn(ft.Text("Email")),
                ft.DataColumn(ft.Text("Teléfono")),
                ft.DataColumn(ft.Text("Acciones"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(caregiver.get("Nombre", "Sin Nombre"))),
                        ft.DataCell(ft.Text(caregiver.get("Cedula", "Sin Cédula"))),
                        ft.DataCell(ft.Text(caregiver.get("Email", "Sin Email"))),
                        ft.DataCell(ft.Text(caregiver.get("Telefono", "Sin Teléfono"))),
                        ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, on_click=delete_caregiver, data=caregiver.get("id")))
                    ]
                ) for caregiver in caregivers
            ]
        )

        return ft.Column([
            ft.Text("📋 Lista de Usuarios", size=20, weight="bold"),
            users_table,
            ft.Text("📋 Lista de Cuidadores", size=20, weight="bold"),
            caregivers_table
        ], spacing=20)

    # 📌 Configurar la página principal
    page.add(content)

    # 📌 Iniciar con la vista de login
    update_view("login")


    def signup_view():
        email_input = ft.TextField(label="Correo Electrónico", hint_text="tu@email.com")
        password_input = ft.TextField(label="Contraseña", password=True, hint_text="Crea una contraseña segura")
        nombre_input = ft.TextField(label="Nombre", hint_text="Ingresa tu nombre")
        apellido_input = ft.TextField(label="Apellido", hint_text="Ingresa tu apellido")
        telefono_input = ft.TextField(label="Teléfono", hint_text="Ingresa tu teléfono")
        ciudad_input = ft.TextField(label="Ciudad", hint_text="Ingresa tu ciudad")
        codigo_postal_input = ft.TextField(label="Código Postal", hint_text="Ingresa tu código postal")
        error_text = ft.Text("", color="red")

        def handle_signup(e):
            try:
                # Validaciones básicas
                if not all([
                    email_input.value,
                    password_input.value,
                    nombre_input.value,
                    apellido_input.value,
                    telefono_input.value,
                    ciudad_input.value,
                    codigo_postal_input.value
                ]):
                    error_text.value = "❌ Por favor completa todos los campos"
                    page.update()
                    return

                user_data = {
                    "email": email_input.value,
                    "nombre": nombre_input.value,
                    "apellido": apellido_input.value,
                    "telefono": telefono_input.value,
                    "ciudad": ciudad_input.value,
                    "codigoPostal": codigo_postal_input.value,
                    "fechaRegistro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                if auth_controller.signup_user(user_data, password_input.value):
                    error_text.color = "green"
                    error_text.value = "✅ Registro exitoso"
                    page.update()
                    update_view("login")
                else:
                    error_text.value = "❌ Error al registrar usuario"
                    page.update()
            except Exception as e:
                error_text.value = f"❌ Error: {str(e)}"
                page.update()

        return ft.Column([
            ft.Text("Registro de Usuario", size=24, weight="bold"),
            email_input,
            password_input,
            nombre_input,
            apellido_input,
            telefono_input,
            ciudad_input,
            codigo_postal_input,
            ft.ElevatedButton(
                "Registrarse",
                bgcolor=PRIMARY_COLOR,
                color="white",
                on_click=handle_signup
            ),
            ft.TextButton(
                "¿Ya tienes cuenta? Inicia Sesión.",
                on_click=lambda _: update_view("login")
            ),
            ft.TextButton(
                "¿Eres cuidador? Regístrate como cuidador.",
                on_click=lambda _: update_view("signup_cuidador")
            ),
            error_text
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    def cuidador_signup_view():
        email_input = ft.TextField(label="Correo Electrónico", hint_text="tu@email.com")
        password_input = ft.TextField(label="Contraseña", password=True, hint_text="Crea una contraseña segura")
        nombre_input = ft.TextField(label="Nombre", hint_text="Ingresa tu nombre")
        apellido_input = ft.TextField(label="Apellido", hint_text="Ingresa tu apellido")
        cedula_input = ft.TextField(label="Cédula", hint_text="Ingresa tu cédula")
        telefono_input = ft.TextField(label="Teléfono", hint_text="Ingresa tu teléfono")
        error_text = ft.Text("", color="red")

        def handle_cuidador_signup(e):
            try:
                # Validaciones básicas
                if not all([
                    email_input.value,
                    password_input.value,
                    nombre_input.value,
                    apellido_input.value,
                    cedula_input.value,
                    telefono_input.value
                ]):
                    error_text.value = "❌ Por favor completa todos los campos"
                    page.update()
                    return

                cuidador_data = {
                    "nombre": nombre_input.value,
                    "apellido": apellido_input.value,
                    "cedula": cedula_input.value,
                    "email": email_input.value,
                    "telefono": telefono_input.value,
                    "fechaRegistro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                if auth_controller.signup_caregiver(cuidador_data, password_input.value):
                    error_text.color = "green"
                    error_text.value = "✅ Registro exitoso"
                    page.update()
                    update_view("login")
                else:
                    error_text.value = "❌ Error al registrar cuidador"
                    page.update()
            except Exception as e:
                error_text.value = f"❌ Error: {str(e)}"
                page.update()

        return ft.Column([
            ft.Text("Registro de Cuidador", size=24, weight="bold"),
            email_input,
            password_input,
            nombre_input,
            apellido_input,
            cedula_input,
            telefono_input,
            ft.ElevatedButton(
                "Registrarse como Cuidador",
                bgcolor=PRIMARY_COLOR,
                color="white",
                on_click=handle_cuidador_signup
            ),
            ft.TextButton(
                "¿Ya tienes cuenta? Inicia Sesión.",
                on_click=lambda _: update_view("login")
            ),
            error_text
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    def main_view():
        caregivers = caregiver_controller.get_caregivers()
        current_index = 0

        if not caregivers:
            return ft.Text("No hay cuidadores disponibles.", size=20, color="red")

        # 📌 Función para actualizar el cuidador mostrado
        def update_caregiver():
            if current_index >= len(caregivers):
                return
            
            caregiver = caregivers[current_index]
            caregiver_image.src = caregiver.get("image", "https://th.bing.com/th/id/OIP.u0a0SBvdAMONiNqQBmTVWAHaLF?rs=1&pid=ImgDetMain")
            caregiver_name.value = f"{caregiver.get('Nombre', 'Desconocido')} {caregiver.get('Apellido', '')}"
            caregiver_cedula.value = f"📄 Cédula: {caregiver.get('Cedula', 'No disponible')}"
            caregiver_email.value = f"📧 Email: {caregiver.get('Email', 'No disponible')}"
            caregiver_phone.value = f"📞 Teléfono: {caregiver.get('Telefono', 'No disponible')}"
            caregiver_registration.value = f"📅 Registrado el: {caregiver.get('FechaRegistro', 'Fecha desconocida')}"
            page.update()

        # 📌 Función para rechazar un cuidador
        def reject_caregiver(e):
            nonlocal current_index
            if current_index < len(caregivers) - 1:
                current_index += 1
                update_caregiver()
            else:
                result_text.value = "No hay más cuidadores disponibles"
                page.update()

        # 📌 Función para aceptar un cuidador y crear una reserva
        def accept_caregiver(e):
            caregiver = caregivers[current_index]
            reservation_id = reserva_controller.crear_reserva(
                usuario_id="user_123",  # ID de usuario de prueba
                cuidador_id=caregiver["id"],
                fecha_inicio="2025-02-01",
                fecha_fin="2025-02-07",
                mascota={"nombre": "Firulais", "tipo": "Perro"}
            )
            result_text.value = "Reserva creada correctamente" if reservation_id else "Error al crear reserva"
            page.update()

        # 📌 Función para cerrar el modal
        def close_modal(e):
            modal.open = False
            page.update()

        # 📌 Función para mostrar información en un modal
        def show_info(e):
            caregiver = caregivers[current_index]
            modal_content.controls.clear()
            modal_content.controls.append(ft.Column([
                ft.Image(src=caregiver.get("image", "https://via.placeholder.com/300"), width=250, height=250),
                ft.Text(f"{caregiver.get('Nombre', 'Desconocido')} {caregiver.get('Apellido', '')}", size=22, weight="bold"),
                ft.Text(f"📄 Cédula: {caregiver.get('Cedula', 'No disponible')}", size=18),
                ft.Text(f"📧 Email: {caregiver.get('Email', 'No disponible')}", size=18),
                ft.Text(f"📞 Teléfono: {caregiver.get('Telefono', 'No disponible')}", size=18),
                ft.Text(f"📅 Registrado el: {caregiver.get('FechaRegistro', 'Fecha desconocida')}", size=18),
                ft.ElevatedButton("Cerrar", on_click=close_modal),
            ]))
            modal.open = True
            page.dialog = modal
            page.update()

        # 📌 Elementos de UI
        caregiver_image = ft.Image(src="https://via.placeholder.com/300", width=300, height=300)
        caregiver_name = ft.Text(value="", size=24, weight="bold")
        caregiver_cedula = ft.Text(value="", size=18)
        caregiver_email = ft.Text(value="", size=18)
        caregiver_phone = ft.Text(value="", size=18)
        caregiver_registration = ft.Text(value="", size=18)

        reject_button = ft.ElevatedButton(text="❌ Rechazar", on_click=reject_caregiver)
        accept_button = ft.ElevatedButton(text="❤️ Aceptar", on_click=accept_caregiver
                                          )
        info_button = ft.ElevatedButton(text="ℹ️ Info", on_click=show_info)

        result_text = ft.Text(value="", size=18, color="green")

        # 📌 Modal para información del cuidador
        modal_content = ft.Column()
        modal = ft.AlertDialog(content=modal_content, modal=True)

        # 📌 Cargar el primer cuidador
        update_caregiver()

        # 📌 Crear la columna principal con todos los elementos
        main_column = ft.Column([
            caregiver_image,
            caregiver_name,
            caregiver_cedula,
            caregiver_email,
            caregiver_phone,
            caregiver_registration,
            ft.Row([reject_button, info_button, accept_button], alignment=ft.MainAxisAlignment.CENTER),
            result_text
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

        # 📌 Configurar el modal
        page.dialog = modal

        return main_column

    # Configurar la página principal
    page.add(content)
    
    # Iniciar con la vista de login
    update_view("login")

    def profile_view(page: ft.Page, user_id):
        page.title = "Mi Perfil"
        controller = ProfileController()

    # Obtener datos del usuario
        user_data = controller.get_user_profile(user_id)
        if not user_data:
            page.add(ft.Text("Error cargando perfil", color="red"))
            return

    # 📌 Definir imagen por defecto si no hay en Firestore
        image_path = user_data.get("FotoPerfil", "uploads/default.jpg")
        if not os.path.exists(image_path):  # Si no existe la imagen, usar un placeholder
            image_path = "https://via.placeholder.com/150"

    # 📌 Elementos de UI
        profile_picture = ft.Image(src=image_path, width=150, height=150)
        name_field = ft.TextField(value=user_data.get("Nombre", ""), label="Nombre")
        lastname_field = ft.TextField(value=user_data.get("Apellido", ""), label="Apellido")
        phone_field = ft.TextField(value=user_data.get("Telefono", ""), label="Teléfono")
        email_text = ft.Text(f"📧 {user_data.get('Email', '')}")  # Solo lectura
        city_field = ft.TextField(value=user_data.get("Ciudad", ""), label="Ciudad")

    # 📌 Función para actualizar perfil
        def update_profile(e):
            updated_data = {
                "Nombre": name_field.value,
                "Apellido": lastname_field.value,
                "Telefono": phone_field.value,
                "Ciudad": city_field.value
            }
            success = controller.update_user_profile(user_id, updated_data)
            result_text.value = "Perfil actualizado correctamente" if success else "Error actualizando perfil"
            page.update()

    # 📌 Función para subir foto de perfil
        def upload_picture(e):
            file_picker.pick_files(allow_multiple=False)

        def file_picker_result(e: ft.FilePickerResultEvent):
            if e.files:
                file_path = e.files[0].path  # Ruta del archivo subido
                new_photo_url = controller.save_profile_picture(user_id, file_path)
                if new_photo_url:
                    profile_picture.src = new_photo_url
                    result_text.value = "Foto de perfil actualizada correctamente"
                else:
                    result_text.value = "Error subiendo la foto"
            page.update()

        file_picker = ft.FilePicker(on_result=file_picker_result)

        update_button = ft.ElevatedButton("Guardar cambios", on_click=update_profile)
        upload_button = ft.ElevatedButton("Subir foto de perfil", on_click=upload_picture)
        result_text = ft.Text(value="", color="green")

    # 📌 Agregar elementos a la UI
        page.overlay.append(file_picker)
        page.add(
            ft.Column([
                profile_picture,
                upload_button,
                name_field,
                lastname_field,
                phone_field,
                email_text,
                city_field,
                update_button,
                result_text
            ],  alignment=ft.MainAxisAlignment.CENTER, spacing=10)
        )

    

if __name__ == "__main__":
    ft.app(target=main)