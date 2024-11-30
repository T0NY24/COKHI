class UserModel:
    def __init__(self, id, name, photo_url, bio, interests):
        self.id = id
        self.name = name
        self.photo_url = photo_url
        self.bio = bio
        self.interests = interests

    # Método para simular obtener un usuario aleatorio
    @staticmethod
    def get_random_user():
        # Aquí iría la lógica para obtener un usuario de la base de datos.
        return UserModel(
            id=1,
            name="Juan Pérez",
            photo_url="https://example.com/photo.jpg",
            bio="Amante del fútbol y la tecnología",
            interests=["Deportes", "Tecnología", "Música"]
        )
