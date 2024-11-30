class MainController:
    def __init__(self):
        # Inicializamos cualquier cosa necesaria
        pass

    def like_user(self, user):
        # Lógica para cuando un usuario le da like
        print(f"Match con {user.name}")
        # Aquí puedes actualizar la base de datos para registrar el like.

    def dislike_user(self, user):
        # Lógica para cuando un usuario le da dislike
        print(f"No match con {user.name}")
        # Aquí puedes actualizar la base de datos para registrar el dislike.
