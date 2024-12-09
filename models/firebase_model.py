import pyrebase
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseModel:
    def __init__(self):
        # Configuración de Firebase para Pyrebase (Autenticación)
        self.firebase_config = {
            "apiKey": "AIzaSyAr5AUqKB-qXEHXn8vgFX8hndpITFkncTY",
            "authDomain": "hubuide.firebaseapp.com",
            "projectId": "hubuide",
            "storageBucket": "hubuide.firebasestorage.app",
            "messagingSenderId": "767282462248",
            "appId": "1:767282462248:web:d27c9856a65bfe6d38ff1d",
            "databaseURL": ""  # No necesario para Firestore
        }
        
        # Inicializar la conexión con Firebase (Autenticación)
        self.firebase = pyrebase.initialize_app(self.firebase_config)
        self.auth = self.firebase.auth()

        # Inicializar Firebase Admin SDK para Firestore
        cred = credentials.Certificate("HubUIDE/hubuide-firebase-adminsdk-4p82r-c015f8b288.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()  # Conexión a Firestore

    # Función de login
    def login(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            return user
        except Exception as e:
            print("Error during login:", e)
            return None

    # Función de signup (registrar usuario)
    def signup(self, email, password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            return user
        except Exception as e:
            print("Error during signup:", e)
            return None

    # Función para guardar los datos del usuario en Firestore
    def save_user_data(self, user_id, nombre, apellido, telefono, ciudad, codigo_postal, correo_electronico, fecha_registro):
        try:
            user_data = {
                "Nombre": nombre,
                "Apellido": apellido,
                "Telefono": telefono,
                "Ciudad": ciudad,
                "CodigoPostal": codigo_postal,
                "CorreoElectronico": correo_electronico,
                "FechaRegistro": fecha_registro
            }
            # Guardar los datos del usuario en Firestore bajo el ID del usuario
            self.db.collection("Usuarios").document(user_id).set(user_data)
            print(f"User {nombre} {apellido} saved in Firestore.")
            return True
        except Exception as e:
            print(f"Error saving user data: {e}")
            return False

    # Función para obtener los datos de un usuario
    def get_user_data(self, user_id):
        try:
            user_data = self.db.collection("Usuarios").document(user_id).get()
            return user_data.to_dict()  # Devuelve los datos del usuario como un diccionario
        except Exception as e:
            print(f"Error retrieving user data: {e}")
            return None

    # Función para actualizar los datos de un usuario
    def update_user_data(self, user_id, updated_data):
        try:
            self.db.collection("Usuarios").document(user_id).update(updated_data)
            print(f"User {user_id} data updated.")
            return True
        except Exception as e:
            print(f"Error updating user data: {e}")
            return False

    # Función para eliminar un usuario
    def delete_user(self, user_id):
        try:
            self.db.collection("Usuarios").document(user_id).delete()
            print(f"User {user_id} deleted.")
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    # Función para guardar los datos del cuidador en Firestore
    def save_caregiver_data(self, caregiver_id, nombre, apellido, cedula, email, telefono, fecha_registro):
        try:
            caregiver_data = {
                "Nombre": nombre,
                "Apellido": apellido,
                "Cedula": cedula,
                "Email": email,  # Asegúrate de que se incluya el email
                "Telefono": telefono,
                "FechaRegistro": fecha_registro
            }
            # Guardar los datos del cuidador en Firestore bajo el ID del cuidador
            self.db.collection("Cuidadores").document(caregiver_id).set(caregiver_data)
            print(f"Caregiver {nombre} {apellido} saved in Firestore.")
            return True
        except Exception as e:
            print(f"Error saving caregiver data: {e}")
            return False

    # Función para obtener los datos de un cuidador
    def get_caregiver_data(self, caregiver_id):
        try:
            caregiver_data = self.db.collection("Cuidadores").document(caregiver_id).get()
            return caregiver_data.to_dict()  # Devuelve los datos del cuidador como un diccionario
        except Exception as e:
            print(f"Error retrieving caregiver data: {e}")
            return None
