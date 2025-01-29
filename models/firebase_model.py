import os
import shutil
import pyrebase
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

UPLOAD_FOLDER = "uploads"

class FirebaseModel:
    def __init__(self):
        # Configuración de Firebase para Pyrebase (Autenticación)
        self.firebase_config = {
            "apiKey": "AIzaSyAr5AUqKB-qXEHXn8vgFX8hndpITFkncTY",
            "authDomain": "hubuide.firebaseapp.com",
            "projectId": "hubuide",
            "storageBucket": "hubuide.firebaseapp.com",
            "messagingSenderId": "767282462248",
            "appId": "1:767282462248:web:d27c9856a65bfe6d38ff1d",
            "databaseURL": ""
        }

        # 🔹 Inicializar Pyrebase
        try:
            self.firebase = pyrebase.initialize_app(self.firebase_config)
            self.auth = self.firebase.auth()
        except Exception as e:
            print(f"Error initializing Pyrebase: {e}")

        # 🔹 Inicializar Firebase Admin SDK para Firestore
        try:
            if not firebase_admin._apps:
                cred = credentials.Certificate("HubUIDE/hubuide-firebase-adminsdk-4p82r-c015f8b288.json")
                firebase_admin.initialize_app(cred)
            self.db = firestore.client()
        except Exception as e:
            print(f"Error initializing Firebase Admin SDK: {e}")
            self.db = None

        # 📂 Crear carpeta `uploads/` si no existe
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

    ### 📌 Autenticación de Usuarios ###

    def login(self, email, password):
        """🔐 Iniciar sesión con email y contraseña."""
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            return user
        except Exception as e:
            print(f"Error during login: {e}")
            return None

    def signup(self, email, password):
        """🆕 Registrar un nuevo usuario."""
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            return user
        except Exception as e:
            print(f"Error during signup: {e}")
            return None

    ### 📌 CRUD de Usuarios ###
    def get_user_profile(self, user_id):
        """Obtiene los datos del usuario desde Firebase Firestore."""
        try:
            user_doc = self.db.collection("Usuarios").document(user_id).get()
            if user_doc.exists:
                return user_doc.to_dict()
            else:
                print(f"Usuario {user_id} no encontrado.")
                return None
        except Exception as e:
            print(f"Error retrieving user profile: {e}")
            return None
    def save_user_data(self, user_id, nombre, apellido, telefono, ciudad, codigo_postal, correo_electronico):
        """📥 Guardar un nuevo usuario en Firestore."""
        try:
            user_data = {
                "Nombre": nombre,
                "Apellido": apellido,
                "Telefono": telefono,
                "Ciudad": ciudad,
                "CodigoPostal": codigo_postal,
                "CorreoElectronico": correo_electronico,
                "FechaRegistro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "FotoPerfil": f"{UPLOAD_FOLDER}/{user_id}.jpg"  # Imagen local por defecto
            }
            self.db.collection("Usuarios").document(user_id).set(user_data)
            print(f"User {nombre} {apellido} saved in Firestore.")
            return True
        except Exception as e:
            print(f"Error saving user data: {e}")
            return False

    def get_user_data(self, user_id):
        """📤 Obtener los datos de un usuario."""
        try:
            user_data = self.db.collection("Usuarios").document(user_id).get()
            return user_data.to_dict()
        except Exception as e:
            print(f"Error retrieving user data: {e}")
            return None

    def update_user_data(self, user_id, updated_data):
        """🔄 Actualizar información del usuario."""
        try:
            self.db.collection("Usuarios").document(user_id).update(updated_data)
            print(f"User {user_id} data updated.")
            return True
        except Exception as e:
            print(f"Error updating user data: {e}")
            return False

    def delete_user(self, user_id):
        """🗑️ Eliminar un usuario de Firestore."""
        try:
            self.db.collection("Usuarios").document(user_id).delete()
            print(f"User {user_id} deleted.")
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    ### 📌 CRUD de Cuidadores ###

    def save_caregiver_data(self, caregiver_id, nombre, apellido, cedula, email, telefono, ciudad):
        """📥 Guardar información de un cuidador."""
        try:
            caregiver_data = {
                "Nombre": nombre,
                "Apellido": apellido,
                "Cedula": cedula,
                "Email": email,
                "Telefono": telefono,
                "Ciudad": ciudad,
                "FechaRegistro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.db.collection("Cuidadores").document(caregiver_id).set(caregiver_data)
            print(f"Caregiver {nombre} {apellido} saved in Firestore.")
            return True
        except Exception as e:
            print(f"Error saving caregiver data: {e}")
            return False

    def get_caregiver_data(self, caregiver_id):
        """📤 Obtener datos de un cuidador."""
        try:
            caregiver_data = self.db.collection("Cuidadores").document(caregiver_id).get()
            return caregiver_data.to_dict()
        except Exception as e:
            print(f"Error retrieving caregiver data: {e}")
            return None

    ### 📌 Manejo de Imágenes de Perfil (Local) ###

    def save_profile_picture(self, user_id, file_path):
        """📤 Guardar una imagen de perfil localmente y actualizar Firestore."""
        try:
            new_filename = f"{UPLOAD_FOLDER}/{user_id}.jpg"
            shutil.copy(file_path, new_filename)  # Copia la imagen a la carpeta `uploads/`
            self.db.collection("Usuarios").document(user_id).update({"FotoPerfil": new_filename})
            return new_filename  # Retorna la ruta local de la imagen
        except Exception as e:
            print(f"Error saving profile picture: {e}")
            return None

    ### 📌 CRUD de Reservas ###

    def create_reservation(self, usuario_id, cuidador_id, fecha_inicio, fecha_fin, mascota):
        """📥 Crear una nueva reserva."""
        try:
            reserva_data = {
                "usuario_id": usuario_id,
                "cuidador_id": cuidador_id,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin,
                "estado": "pendiente",
                "mascota": mascota,
                "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            doc_ref = self.db.collection("Reservas").add(reserva_data)
            return doc_ref[1].id
        except Exception as e:
            print(f"Error creating reservation: {e}")
            return None

    def update_reservation_status(self, reserva_id, nuevo_estado):
        """🔄 Actualizar estado de una reserva."""
        try:
            self.db.collection("Reservas").document(reserva_id).update({"estado": nuevo_estado})
            return True
        except Exception as e:
            print(f"Error updating reservation status: {e}")
            return False

    def delete_reservation(self, reserva_id):
        """🗑️ Eliminar una reserva."""
        try:
            self.db.collection("Reservas").document(reserva_id).delete()
            return True
        except Exception as e:
            print(f"Error deleting reservation: {e}")
            return False
