from models.firebase_model import FirebaseModel

class AdminController:
    def __init__(self):
        self.firebase = FirebaseModel()

    

    def get_all_users(self):
        """Obtiene la lista de usuarios registrados."""
        return self.firebase.get_all_users()

    def get_all_caregivers(self):
        """Obtiene la lista de cuidadores registrados."""
        return self.firebase.get_all_caregivers()

    def delete_user(self, user_id):
        """Elimina un usuario."""
        return self.firebase.delete_user(user_id)

    def delete_caregiver(self, caregiver_id):
        """Elimina un cuidador."""
        return self.firebase.delete_caregiver(caregiver_id)
