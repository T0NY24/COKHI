import flet as ft
from controllers.usuario_controller import UsuarioController

def usuario_view(page):
    page.title = "Usuarios - Cokhi"
    page.vertical_alignment = ft.MainAxisAlignment.START

    controller = UsuarioController()

    # Contenedor principal
    contenedor = ft.Column()

    def listar_usuarios():
        """Muestra todos los usuarios registrados."""
        usuarios = controller.obtener_todos_usuarios()
        contenedor.controls.clear()  # Limpia los controles existentes
        contenedor.controls.append(ft.Text("Usuarios Registrados:", style="headlineMedium"))
        
        if usuarios:
            for usuario in usuarios:
                contenedor.controls.append(
                    ft.Text(
                        f"ID: {usuario['id']}, Nombre: {usuario['nombre']} {usuario.get('apellido', '')}, "
                        f"Correo: {usuario['correoElectronico']}, Rol: {usuario['estado']}"
                    )
                )
        else:
            contenedor.controls.append(ft.Text("No hay usuarios registrados.", color=ft.colors.RED))

        # Agrega los botones CRUD
        contenedor.controls.append(ft.ElevatedButton("Agregar Usuario", on_click=mostrar_formulario_agregar))
        contenedor.controls.append(ft.ElevatedButton("Eliminar Usuario", on_click=mostrar_formulario_eliminar))
        contenedor.controls.append(ft.ElevatedButton("Actualizar Usuario", on_click=mostrar_formulario_actualizar))

        page.update()

    def mostrar_formulario_agregar(e):
        """Muestra un formulario para agregar un nuevo usuario."""
        contenedor.controls.clear()
        contenedor.controls.append(ft.Text("Agregar Nuevo Usuario", style="headlineMedium"))
        
        # Campos de entrada
        nombre = ft.TextField(label="Nombre")
        apellido = ft.TextField(label="Apellido")
        correo = ft.TextField(label="Correo Electrónico")
        telefono = ft.TextField(label="Teléfono")
        ciudad = ft.TextField(label="Ciudad")
        codigo_postal = ft.TextField(label="Código Postal")
        
        # Botón de confirmación
        contenedor.controls.append(nombre)
        contenedor.controls.append(apellido)
        contenedor.controls.append(correo)
        contenedor.controls.append(telefono)
        contenedor.controls.append(ciudad)
        contenedor.controls.append(codigo_postal)

        contenedor.controls.append(
            ft.ElevatedButton(
                "Crear Usuario",
                on_click=lambda _: agregar_usuario(nombre, apellido, correo, telefono, ciudad, codigo_postal),
            )
        )
        page.update()

    def agregar_usuario(nombre, apellido, correo, telefono, ciudad, codigo_postal):
        """Llama al controlador para agregar un usuario."""
        controller.crear_usuario(
            correoElectronico=correo.value,
            nombre=nombre.value,
            telefono=telefono.value,
            ciudad=ciudad.value,
            codigoPostal=codigo_postal.value
        )
        listar_usuarios()

    def mostrar_formulario_eliminar(e):
        """Muestra un formulario para eliminar un usuario."""
        contenedor.controls.clear()
        contenedor.controls.append(ft.Text("Eliminar Usuario", style="headlineMedium"))
        
        # Campo de entrada para el ID del usuario
        usuario_id = ft.TextField(label="ID del Usuario", autofocus=True)
        contenedor.controls.append(usuario_id)
        
        # Botón de confirmación
        contenedor.controls.append(
            ft.ElevatedButton(
                "Eliminar",
                on_click=lambda _: eliminar_usuario(usuario_id),
            )
        )
        page.update()

    def eliminar_usuario(usuario_id):
        """Elimina un usuario por su ID."""
        controller.eliminar_usuario(usuario_id.value)
        listar_usuarios()

    def mostrar_formulario_actualizar(e):
        """Muestra un formulario para actualizar un usuario."""
        contenedor.controls.clear()
        contenedor.controls.append(ft.Text("Actualizar Usuario", style="headlineMedium"))
        
        # Campos de entrada para ID y datos a actualizar
        usuario_id = ft.TextField(label="ID del Usuario", autofocus=True)
        correo = ft.TextField(label="Correo Electrónico (opcional)")
        telefono = ft.TextField(label="Teléfono (opcional)")
        
        contenedor.controls.append(usuario_id)
        contenedor.controls.append(correo)
        contenedor.controls.append(telefono)

        # Botón de confirmación
        contenedor.controls.append(
            ft.ElevatedButton(
                "Actualizar",
                on_click=lambda _: actualizar_usuario(usuario_id, correo, telefono),
            )
        )
        page.update()

    def actualizar_usuario(usuario_id, correo, telefono):
        """Actualiza datos específicos de un usuario."""
        data = {}
        if correo.value:
            data['correoElectronico'] = correo.value
        if telefono.value:
            data['telefono'] = telefono.value

        if data:
            controller.actualizar_usuario(usuario_id.value, data)
        listar_usuarios()

    # Inicia mostrando todos los usuarios
    listar_usuarios()

    # Agregar el contenedor al page
    page.add(contenedor)
