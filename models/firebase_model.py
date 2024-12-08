import pyrebase
from datetime import datetime

class FirebaseModel:
    def __init__(self):
        self.firebase_config = {
            "apiKey": "AIzaSyAr5AUqKB-qXEHXn8vgFX8hndpITFkncTY",
            "authDomain": "hubuide.firebaseapp.com",
            "projectId": "hubuide",
            "storageBucket": "hubuide.firebasestorage.app",
            "messagingSenderId": "767282462248",
            "appId": "1:767282462248:web:d27c9856a65bfe6d38ff1d",
            "databaseURL": ""
        }
        self.firebase = pyrebase.initialize_app(self.firebase_config)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()  # Conexión con la base de datos (Firestore)

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
            self.db.child("Usuarios").child(user_id).set(user_data)
            print(f"User {nombre} {apellido} saved in Firestore.")
            return True
        except Exception as e:
            print(f"Error saving user data: {e}")
            return False

    # Función para obtener los datos de un usuario
    def get_user_data(self, user_id):
        try:
            user_data = self.db.child("Usuarios").child(user_id).get()
            return user_data.val()  # Devuelve los datos del usuario
        except Exception as e:
            print(f"Error retrieving user data: {e}")
            return None

    # Función para actualizar los datos de un usuario
    def update_user_data(self, user_id, updated_data):
        try:
            self.db.child("Usuarios").child(user_id).update(updated_data)
            print(f"User {user_id} data updated.")
            return True
        except Exception as e:
            print(f"Error updating user data: {e}")
            return False

    # Función para eliminar un usuario
    def delete_user(self, user_id):
        try:
            self.db.child("Usuarios").child(user_id).remove()
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
                "Email": email,
                "Telefono": telefono,
                "FechaRegistro": fecha_registro
            }
            # Guardar los datos del cuidador en Firestore bajo el ID del cuidador
            self.db.child("Cuidadores").child(caregiver_id).set(caregiver_data)
            print(f"Caregiver {nombre} {apellido} saved in Firestore.")
            return True
        except Exception as e:
            print(f"Error saving caregiver data: {e}")
            return False

    # Función para obtener los datos de un cuidador
    def get_caregiver_data(self, caregiver_id):
        try:
            caregiver_data = self.db.child("Cuidadores").child(caregiver_id).get()
            return caregiver_data.val()  # Devuelve los datos del cuidador
        except Exception as e:
            print(f"Error retrieving caregiver data: {e}")
            return None
