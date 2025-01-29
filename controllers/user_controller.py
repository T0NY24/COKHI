from models.firebase_model import FirebaseModel

class UserController:
    def __init__(self):
        self.firebase = FirebaseModel()

    def create_user(self, email, password, nombre, apellido, telefono, ciudad, codigo_postal):
        """Registra un nuevo usuario y guarda sus datos en Firestore."""
        user = self.firebase.signup(email, password)
        if user:
            user_id = user['localId']
            success = self.firebase.save_user_data(user_id, nombre, apellido, telefono, ciudad, codigo_postal, email)
            return success
        return False

    def get_user(self, user_id):
        """Obtiene la información de un usuario."""
        return self.firebase.get_user_data(user_id)

    def update_user(self, user_id, updated_data):
        """Actualiza los datos de un usuario en Firestore."""
        return self.firebase.update_user_data(user_id, updated_data)

    def delete_user(self, user_id):
        """Elimina un usuario de Firestore."""
        return self.firebase.delete_user(user_id)
