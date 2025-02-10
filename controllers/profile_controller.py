from models.firebase_model import FirebaseModel


class ProfileController:
    def __init__(self):
        """Inicializa el controlador con FirebaseModel."""
        self.firebase = FirebaseModel()

    def get_user_profile(self, user_id):
        """📤 Obtiene los datos del usuario desde Firebase Firestore."""
        if not user_id:
            print("❌ Error: ID de usuario no proporcionado.")
            return None

        user_data = self.firebase.get_user_profile(user_id)
        if user_data:
            return user_data
        else:
            print(f"⚠️ Advertencia: Usuario {user_id} no encontrado en Firebase.")
            return None

    def update_user_profile(self, user_id, updated_data):
        """🔄 Actualiza la información del usuario en Firebase Firestore."""
        if not user_id or not updated_data:
            print("❌ Error: Falta el ID de usuario o los datos a actualizar.")
            return False

        success = self.firebase.update_user_profile(user_id, updated_data)
        if success:
            print(f"✅ Perfil del usuario {user_id} actualizado correctamente.")
        else:
            print(f"⚠️ Error al actualizar el perfil de {user_id}.")
        return success

    def save_profile_picture(self, user_id, file_path):
        """📤 Guarda la imagen localmente y actualiza Firestore."""
        if not user_id or not file_path:
            print("❌ Error: ID de usuario o ruta del archivo no proporcionados.")
            return None

        new_photo_url = self.firebase.save_profile_picture(user_id, file_path)
        if new_photo_url:
            print(f"✅ Foto de perfil de {user_id} guardada en {new_photo_url}.")
            return new_photo_url
        else:
            print(f"⚠️ Error al guardar la foto de perfil de {user_id}.")
            return None
