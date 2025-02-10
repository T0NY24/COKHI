import flet as ft
from controllers.admin_controller import AdminController


def admin_dashboard(page: ft.Page):
    page.title = "Panel de Administración"
    page.bgcolor = "#FCFAFA"
    page.padding = 20
    controller = AdminController()

    users = controller.get_all_users()
    caregivers = controller.get_all_caregivers()

    def delete_user(e):
        user_id = e.control.data
        if controller.delete_user(user_id):
            page.dialog = ft.AlertDialog(
                title=ft.Text("✅ Usuario eliminado con éxito")
            )
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("⚠️ Error al eliminar usuario"))
        page.update()

    def delete_caregiver(e):
        caregiver_id = e.control.data
        if controller.delete_caregiver(caregiver_id):
            page.dialog = ft.AlertDialog(
                title=ft.Text("✅ Cuidador eliminado con éxito")
            )
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("⚠️ Error al eliminar cuidador"))
        page.update()

    users_table = ft.DataTable(
        border=ft.border.all(1, "#D1D5DB"),
        heading_row_color="#25523E10",
        columns=[
            ft.DataColumn(ft.Text("Nombre", weight="bold", color="#6D4318")),
            ft.DataColumn(ft.Text("Email", weight="bold", color="#6D4318")),
            ft.DataColumn(ft.Text("Acciones", weight="bold", color="#6D4318")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            user.get("Nombre", "Sin Nombre"), size=14, color="#6D4318"
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            user.get("CorreoElectronico", "Sin Email"),
                            size=14,
                            color="#25523E",
                        )
                    ),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            icon_color="red600",
                            on_click=delete_user,
                            data=user.get("id"),
                        )
                    ),
                ]
            )
            for user in users
        ],
    )

    caregivers_table = ft.DataTable(
        border=ft.border.all(1, "#D1D5DB"),
        heading_row_color="#25523E10",
        columns=[
            ft.DataColumn(ft.Text("Nombre", weight="bold", color="#6D4318")),
            ft.DataColumn(ft.Text("Cédula", weight="bold", color="#6D4318")),
            ft.DataColumn(ft.Text("Email", weight="bold", color="#6D4318")),
            ft.DataColumn(ft.Text("Teléfono", weight="bold", color="#6D4318")),
            ft.DataColumn(ft.Text("Acciones", weight="bold", color="#6D4318")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            caregiver.get("Nombre", "Sin Nombre"),
                            size=14,
                            color="#6D4318",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            caregiver.get("Cedula", "Sin Cédula"),
                            size=14,
                            color="#25523E",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            caregiver.get("Email", "Sin Email"),
                            size=14,
                            color="#25523E",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            caregiver.get("Telefono", "Sin Teléfono"),
                            size=14,
                            color="#25523E",
                        )
                    ),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            icon_color="red600",
                            on_click=delete_caregiver,
                            data=caregiver.get("id"),
                        )
                    ),
                ]
            )
            for caregiver in caregivers
        ],
    )

    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Text(
                        "📋 Lista de Usuarios", size=24, weight="bold", color="#6D4318"
                    ),
                    padding=10,
                ),
                users_table,
                ft.Container(
                    content=ft.Text(
                        "📋 Lista de Cuidadores",
                        size=24,
                        weight="bold",
                        color="#6D4318",
                    ),
                    padding=10,
                ),
                caregivers_table,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        )
    )


ft.app(target=admin_dashboard)
