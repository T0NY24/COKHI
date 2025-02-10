import flet as ft
from controllers.user_controller import UserController


def user_view(page: ft.Page):
    page.title = "Gestión de Usuarios"
    controller = UserController()

    # 📌 Función para registrar un usuario
    def register_user(e):
        success = controller.create_user(
            email_input.value,
            password_input.value,
            nombre_input.value,
            apellido_input.value,
            telefono_input.value,
            ciudad_input.value,
            codigo_postal_input.value,
        )
        if success:
            page.dialog = ft.AlertDialog(title=ft.Text("Usuario registrado con éxito"))
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Error al registrar usuario"))
        page.dialog.open = True
        page.update()

    # 📌 Función para buscar un usuario
    def search_user(e):
        user_data = controller.get_user(user_id_input.value)
        if user_data:
            result_text.value = f"Nombre: {user_data['Nombre']}\nApellido: {user_data['Apellido']}\nCorreo: {user_data['CorreoElectronico']}"
        else:
            result_text.value = "Usuario no encontrado"
        page.update()

    # 📌 Función para actualizar un usuario
    def update_user(e):
        updated_data = {
            "Telefono": telefono_input.value,
            "Ciudad": ciudad_input.value,
            "CodigoPostal": codigo_postal_input.value,
        }
        success = controller.update_user(user_id_input.value, updated_data)
        result_text.value = (
            "Usuario actualizado correctamente"
            if success
            else "Error al actualizar usuario"
        )
        page.update()

    # 📌 Función para eliminar un usuario
    def delete_user(e):
        success = controller.delete_user(user_id_input.value)
        result_text.value = (
            "Usuario eliminado correctamente"
            if success
            else "Error al eliminar usuario"
        )
        page.update()

    # 📝 Elementos de la UI
    user_id_input = ft.TextField(label="ID de Usuario", hint_text="Ingrese el ID")
    email_input = ft.TextField(label="Correo Electrónico")
    password_input = ft.TextField(label="Contraseña", password=True)
    nombre_input = ft.TextField(label="Nombre")
    apellido_input = ft.TextField(label="Apellido")
    telefono_input = ft.TextField(label="Teléfono")
    ciudad_input = ft.TextField(label="Ciudad")
    codigo_postal_input = ft.TextField(label="Código Postal")
    result_text = ft.Text("")

    # 📌 Botones CRUD
    register_button = ft.ElevatedButton(
        text="Registrar Usuario", on_click=register_user
    )
    search_button = ft.ElevatedButton(text="Buscar Usuario", on_click=search_user)
    update_button = ft.ElevatedButton(text="Actualizar Usuario", on_click=update_user)
    delete_button = ft.ElevatedButton(text="Eliminar Usuario", on_click=delete_user)

    # 📌 Agregar elementos a la UI
    page.add(
        ft.Column(
            [
                user_id_input,
                email_input,
                password_input,
                nombre_input,
                apellido_input,
                telefono_input,
                ciudad_input,
                codigo_postal_input,
                register_button,
                search_button,
                update_button,
                delete_button,
                result_text,
            ]
        )
    )


ft.app(target=user_view)
