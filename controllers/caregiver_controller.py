from models.firebase_model import FirebaseModel


class CaregiverController:
    def __init__(self):
        self.firebase = FirebaseModel()

    def create_caregiver(
        self,
        nombre,
        apellido,
        cedula,
        email,
        telefono,
        ciudad,
        experiencia,
        rating,
        precio,
    ):
        """Registra un nuevo cuidador en Firestore con más información relevante."""
        caregiver_id = f"{nombre.lower()}_{apellido.lower()}_{cedula}"  # Generar ID basado en nombre y cédula
        success = self.firebase.save_caregiver_data(
            caregiver_id,
            nombre,
            apellido,
            cedula,
            email,
            telefono,
            ciudad,
            experiencia,
            rating,
            precio,
        )
        return success


class CaregiverController:
    def __init__(self):
        self.firebase = FirebaseModel()

    def get_caregivers(self):
        """Obtiene la lista de cuidadores desde Firestore."""
        caregivers = self.firebase.get_all_caregivers()
        if caregivers is None:
            caregivers = []  # Evitar error si la consulta falla
        return caregivers

    def get_caregiver(self, caregiver_id):
        """Obtiene la información de un cuidador desde Firestore."""
        return self.firebase.get_caregiver_data(caregiver_id)

    def update_caregiver(self, caregiver_id, updated_data):
        """Actualiza los datos de un cuidador en Firestore."""
        return self.firebase.update_caregiver_data(
            caregiver_id, updated_data
        )  # Se usa la función correcta

    def delete_caregiver(self, caregiver_id):
        """Elimina un cuidador de Firestore."""
        return self.firebase.delete_caregiver(
            caregiver_id
        )  # Se usa la función correcta

    def get_all_caregivers(self):
        """Obtiene la lista de todos los cuidadores desde Firestore."""
        return self.firebase.get_all_caregivers()
