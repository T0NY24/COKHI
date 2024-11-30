import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirebaseManager:
    def __init__(self):
        self.initialize_firebase()

    def initialize_firebase(self):
        # Check if the default Firebase app has already been initialized
        if not firebase_admin._apps:
            # Inicializa Firebase con las credenciales del archivo serviceAccountKey.json
            cred = credentials.Certificate('HubUIDE\serviceAccountKey.json')
            firebase_admin.initialize_app(cred, {
                'projectId': 'your-project-id',
            })

        # Obtén una referencia a Firestore
        self.db = firestore.client()

        