from flet import Page, Column, Text, Image, IconButton, icons, Row, Container, padding

def perfil_view(page: Page, datos_usuario):
    """Renderiza la interfaz del perfil de usuario."""
    page.title = "Perfil de Usuario"
    page.add(
        Column(
            [
                # Cabecera de Perfil
                Column(
                    [
                        Container(
                            Image(src=datos_usuario.get("foto", "/placeholder.jpg"), width=120, height=120),
                            padding=padding.all(16),
                        ),
                        Text(datos_usuario.get("Nombre", "Nombre no disponible"), size=24, weight="bold"),
                        Text(f"Rol: {datos_usuario.get('Rol', 'N/A')}"),
                    ],
                    alignment="center",
                ),
                # Información Personal
                Column(
                    [
                        Row([Text("Teléfono: "), Text(datos_usuario.get("Telefono", "N/A"))]),
                        Row([Text("Ciudad: "), Text(datos_usuario.get("Ciudad", "N/A"))]),
                        IconButton(icons.EDIT, on_click=lambda _: print("Editar perfil")),
                    ]
                ),
                # Mascotas
                Column(
                    [
                        Text("Mis Mascotas", size=20, weight="bold"),
                        # Aquí se puede agregar una lista dinámica de mascotas
                        Row([Text("Luna - Labrador"), IconButton(icons.EDIT)]),
                        Row([Text("Milo - Siamés"), IconButton(icons.EDIT)]),
                    ]
                ),
            ],
        )
    )
