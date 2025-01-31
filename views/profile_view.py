import flet as ft
from controllers.profile_controller import ProfileController
import os

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
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
    )

ft.app(target=lambda page: profile_view(page, "GUeE4UPyoqYcgt7zwkpRC3E5c4H3"))  # Reemplazar con user_id dinámico
