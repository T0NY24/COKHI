import flet as ft
from controllers.caregiver_controller import CaregiverController
from controllers.reservas_controller import ReservasController

def main_page(page: ft.Page):
    page.title = "Encuentra tu Cuidador"
    caregiver_controller = CaregiverController()
    reserva_controller = ReservasController()

    caregivers = caregiver_controller.get_caregivers()
    current_index = 0

    if not caregivers:
        page.add(ft.Text("No hay cuidadores disponibles.", size=20, color="red"))
        return

    # 📌 Función para actualizar el cuidador mostrado
    def update_caregiver():
        if current_index >= len(caregivers):
            return
        
        caregiver = caregivers[current_index]
        caregiver_image.src = caregiver.get("image", "https://th.bing.com/th/id/OIP.u0a0SBvdAMONiNqQBmTVWAHaLF?rs=1&pid=ImgDetMain")  # Si no hay imagen, mostrar placeholder
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
    accept_button = ft.ElevatedButton(text="❤️ Aceptar", on_click=accept_caregiver)
    info_button = ft.ElevatedButton(text="ℹ️ Info", on_click=show_info)

    result_text = ft.Text(value="", size=18, color="green")

    # 📌 Modal para información del cuidador
    modal_content = ft.Column()
    modal = ft.AlertDialog(content=modal_content, modal=True)

    # 📌 Cargar el primer cuidador
    update_caregiver()

    # 📌 Agregar elementos a la UI
    page.add(
        ft.Column([
            caregiver_image,
            caregiver_name,
            caregiver_cedula,
            caregiver_email,
            caregiver_phone,
            caregiver_registration,
            ft.Row([reject_button, info_button, accept_button], alignment=ft.MainAxisAlignment.CENTER),
            result_text
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
    )

    # 📌 Agregar el modal
    page.dialog = modal

ft.app(target=main_page)
