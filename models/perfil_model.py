from models import FirebaseModel

class PerfilModel:
    def __init__(self, firebase_config):
        self.firebase_model = FirebaseModel(firebase_config)

    def obtener_datos_usuario(self, user_id):
        # Obtenemos los datos del usuario desde Firebase usando el ID
        return self.firebase_model.get_user_data(user_id)

    def actualizar_datos_usuario(self, user_id, nuevos_datos):
        # Actualizamos los datos del usuario en Firebase
        return self.firebase_model.update_user_data(user_id, nuevos_datos)
