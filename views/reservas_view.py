import flet as ft
from controllers.reservas_controller import ReservasController

def reservas_view(page: ft.Page):
    page.title = "Gestión de Reservas"
    controller = ReservasController()

    # 📌 Función para crear una reserva
    def create_reservation(e):
        success = controller.crear_reserva(
            usuario_id_input.value, cuidador_id_input.value, 
            fecha_inicio_input.value, fecha_fin_input.value, 
            {"nombre": mascota_nombre_input.value, "tipo": mascota_tipo_input.value}
        )
        result_text.value = "Reserva creada correctamente" if success else "Error al crear reserva"
        page.update()

    # 📌 Función para buscar una reserva por ID
    def search_reservation(e):
        reserva = controller.obtener_reserva(reserva_id_input.value)
        if reserva:
            result_text.value = (
                f"Usuario ID: {reserva['usuario_id']}\n"
                f"Cuidador ID: {reserva['cuidador_id']}\n"
                f"Fecha Inicio: {reserva['fecha_inicio']}\n"
                f"Fecha Fin: {reserva['fecha_fin']}\n"
                f"Estado: {reserva['estado']}\n"
                f"Mascota: {reserva['mascota']['nombre']} ({reserva['mascota']['tipo']})"
            )
        else:
            result_text.value = "Reserva no encontrada"
        page.update()

    # 📌 Función para actualizar el estado de una reserva
    def update_reservation_status(e):
        success = controller.actualizar_estado_reserva(reserva_id_input.value, estado_input.value)
        result_text.value = "Estado actualizado correctamente" if success else "Error al actualizar estado"
        page.update()

    # 📌 Función para eliminar una reserva
    def delete_reservation(e):
        success = controller.eliminar_reserva(reserva_id_input.value)
        result_text.value = "Reserva eliminada correctamente" if success else "Error al eliminar reserva"
        page.update()

    # 📝 UI Elements
    reserva_id_input = ft.TextField(label="ID de la Reserva")
    usuario_id_input = ft.TextField(label="ID del Usuario")
    cuidador_id_input = ft.TextField(label="ID del Cuidador")
    fecha_inicio_input = ft.TextField(label="Fecha de Inicio (YYYY-MM-DD)")
    fecha_fin_input = ft.TextField(label="Fecha de Fin (YYYY-MM-DD)")
    mascota_nombre_input = ft.TextField(label="Nombre de la Mascota")
    mascota_tipo_input = ft.TextField(label="Tipo de Mascota")
    estado_input = ft.Dropdown(
        label="Estado de la Reserva",
        options=[
            ft.dropdown.Option("pendiente"),
            ft.dropdown.Option("aceptada"),
            ft.dropdown.Option("rechazada"),
        ]
    )

    # 📌 CRUD Buttons
    create_button = ft.ElevatedButton(text="Crear Reserva", on_click=create_reservation)
    search_button = ft.ElevatedButton(text="Buscar Reserva", on_click=search_reservation)
    update_button = ft.ElevatedButton(text="Actualizar Estado", on_click=update_reservation_status)
    delete_button = ft.ElevatedButton(text="Eliminar Reserva", on_click=delete_reservation)

    result_text = ft.Text("")

    # 📌 Agregar elementos a la UI
    page.add(
        ft.Column([
            reserva_id_input, usuario_id_input, cuidador_id_input, 
            fecha_inicio_input, fecha_fin_input, 
            mascota_nombre_input, mascota_tipo_input, 
            estado_input, 
            create_button, search_button, update_button, delete_button,
            result_text
        ])
    )

ft.app(target=reservas_view)
