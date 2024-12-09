from models.perfil_model import PerfilModel
from views.perfil_view import perfil_view

class PerfilController:
    def __init__(self, firebase_config):
        self.modelo = PerfilModel(firebase_config)

    def mostrar_perfil(self, page, user_id):
        """Mostrar el perfil del usuario con el user_id"""
        # Usamos el correo electrónico o ID para obtener los datos del usuario
        datos_usuario = self.modelo.obtener_datos_usuario(user_id)
        perfil_view(page, datos_usuario)




    def actualizar_perfil(self, user_id, nuevos_datos):
        # Llamamos al modelo para actualizar los datos del usuario
        result = self.modelo.actualizar_datos_usuario(user_id, nuevos_datos)
        return result
