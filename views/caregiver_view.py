import flet as ft
from controllers.caregiver_controller import CaregiverController

def caregiver_view(page: ft.Page):
    page.title = "Gestión de Cuidadores"
    controller = CaregiverController()

    # 📌 Función para registrar un cuidador
    def register_caregiver(e):
        success = controller.create_caregiver(
            nombre_input.value, apellido_input.value, 
            cedula_input.value, email_input.value, 
            telefono_input.value
        )
        page.dialog = ft.AlertDialog(title=ft.Text("Cuidador registrado con éxito" if success else "Error al registrar cuidador"))
        page.dialog.open = True
        page.update()

    # 📌 Función para buscar un cuidador
    def search_caregiver(e):
        caregiver_data = controller.get_caregiver(caregiver_id_input.value)
        if caregiver_data:
            result_text.value = f"Nombre: {caregiver_data['Nombre']}\nApellido: {caregiver_data['Apellido']}\nCorreo: {caregiver_data['Email']}"
        else:
            result_text.value = "Cuidador no encontrado"
        page.update()

    # 📌 Función para actualizar un cuidador
    def update_caregiver(e):
        updated_data = {
            "Telefono": telefono_input.value
        }
        success = controller.update_caregiver(caregiver_id_input.value, updated_data)
        result_text.value = "Cuidador actualizado correctamente" if success else "Error al actualizar cuidador"
        page.update()

    # 📌 Función para eliminar un cuidador
    def delete_caregiver(e):
        success = controller.delete_caregiver(caregiver_id_input.value)
        result_text.value = "Cuidador eliminado correctamente" if success else "Error al eliminar cuidador"
        page.update()

    # 📝 Elementos de la UI
    caregiver_id_input = ft.TextField(label="ID de Cuidador", hint_text="Ingrese el ID")
    nombre_input = ft.TextField(label="Nombre")
    apellido_input = ft.TextField(label="Apellido")
    cedula_input = ft.TextField(label="Cédula")
    email_input = ft.TextField(label="Correo Electrónico")
    telefono_input = ft.TextField(label="Teléfono")
    result_text = ft.Text("")

    # 📌 Botones CRUD
    register_button = ft.ElevatedButton(text="Registrar Cuidador", on_click=register_caregiver)
    search_button = ft.ElevatedButton(text="Buscar Cuidador", on_click=search_caregiver)
    update_button = ft.ElevatedButton(text="Actualizar Cuidador", on_click=update_caregiver)
    delete_button = ft.ElevatedButton(text="Eliminar Cuidador", on_click=delete_caregiver)

    # 📌 Agregar elementos a la UI
    page.add(
        ft.Column([
            caregiver_id_input, nombre_input, apellido_input, 
            cedula_input, email_input, telefono_input, 
            register_button, search_button, update_button, delete_button,
            result_text
        ])
    )

ft.app(target=caregiver_view)
