# models/usuario_model.py
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Inicializar Firebase
cred = credentials.Certificate("HubUIDE/hubuide-firebase-adminsdk-4p82r-c015f8b288.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class UsuarioModel:
    def __init__(self):
        self.collection = db.collection("Usuarios")

    def crear_usuario(self, usuario):
        """Crea un nuevo usuario en la base de datos."""
        self.collection.document(usuario['id']).set(usuario)

    def obtener_usuario(self, user_id):
        """Obtiene un usuario por su ID."""
        doc_ref = self.collection.document(user_id)
        doc = doc_ref.get()
        return doc.to_dict() if doc.exists else None

    def actualizar_usuario(self, user_id, data):
        """Actualiza datos específicos de un usuario."""
        self.collection.document(user_id).update(data)

    def eliminar_usuario(self, user_id):
        """Elimina un usuario por su ID."""
        self.collection.document(user_id).delete()

    def obtener_todos_usuarios(self):
        """Obtiene todos los usuarios de la colección."""
        return [doc.to_dict() for doc in self.collection.stream()]
