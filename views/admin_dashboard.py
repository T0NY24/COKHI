import flet as ft
from controllers.admin_controller import AdminController

def admin_dashboard(page: ft.Page):
    page.title = "Panel de Administración"
    controller = AdminController()

    # 📂 Obtener listas de usuarios y cuidadores
    users = controller.get_all_users()
    caregivers = controller.get_all_caregivers()

    # 📌 Función para eliminar usuario
    def delete_user(e):
        user_id = e.control.data
        if controller.delete_user(user_id):
            page.dialog = ft.AlertDialog(title=ft.Text("✅ Usuario eliminado con éxito"))
            page.update()
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("⚠️ Error al eliminar usuario"))
        page.update()

    # 📌 Función para eliminar cuidador
    def delete_caregiver(e):
        caregiver_id = e.control.data
        if controller.delete_caregiver(caregiver_id):
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

    # 📌 Tabla de cuidadores (corregida con los datos reales de Firestore)
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

    # 📌 Agregar componentes a la página
    page.add(
        ft.Column([
            ft.Text("📋 Lista de Usuarios", size=20, weight="bold"),
            users_table,
            ft.Text("📋 Lista de Cuidadores", size=20, weight="bold"),
            caregivers_table
        ], spacing=20)
    )

ft.app(target=admin_dashboard)
