from models.firebase_model import FirebaseModel
from datetime import datetime


class AuthController:
    def __init__(self):
        self.firebase_model = FirebaseModel()

    # Función para el login de usuario
    def login_user(self, email, password):
        user = self.firebase_model.login(email, password)
        if user:
            print(f"Welcome back, {email}")
            return True
        else:
            print("Login failed. Please check your credentials.")
            return False

    # Función para el signup (registro de usuario)
    def signup_user(self, usuario_data, password):
        # Extraer datos del diccionario
        email = usuario_data.get("email")
        nombre = usuario_data.get("nombre")
        apellido = usuario_data.get("apellido")
        telefono = usuario_data.get("telefono")
        ciudad = usuario_data.get("ciudad")
        codigo_postal = usuario_data.get("codigoPostal")
        fecha_registro = usuario_data.get(
            "fechaRegistro", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        # Primero, registramos al usuario en Firebase Authentication
        user = self.firebase_model.signup(email, password)
        if user:
            print(f"Account created successfully for {email}")

            # Ahora guardamos los datos adicionales en Firestore
            user_id = user["localId"]  # Obtén el ID del usuario creado

            # Guardamos los datos del usuario en Firestore
            self.firebase_model.save_user_data(
                user_id,
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                ciudad=ciudad,
                codigo_postal=codigo_postal,
                correo_electronico=email,
                fecha_registro=fecha_registro,
            )

            print(f"User {nombre} {apellido} registered in Firestore successfully.")
            return True
        else:
            print("Signup failed.")
            return False

    # Función para el signup de cuidadores
    def signup_caregiver(self, cuidador_data, password):
        # Extraer datos del diccionario
        email = cuidador_data.get("email")
        nombre = cuidador_data.get("nombre")
        apellido = cuidador_data.get("apellido")
        cedula = cuidador_data.get("cedula")
        telefono = cuidador_data.get("telefono")
        fecha_registro = cuidador_data.get(
            "fechaRegistro", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        # Primero, registramos al cuidador en Firebase Authentication (sin guardar la contraseña en Firestore)
        user = self.firebase_model.signup(email, password)
        if user:
            print(f"Account created successfully for caregiver {email}")

            # Ahora guardamos los datos adicionales del cuidador en Firestore (sin la contraseña)
            caregiver_id = user["localId"]  # Obtén el ID del cuidador creado

            # Guardamos los datos del cuidador en Firestore, ahora incluyendo 'email'
            self.firebase_model.save_caregiver_data(
                caregiver_id,
                nombre=nombre,
                apellido=apellido,
                cedula=cedula,
                telefono=telefono,
                fecha_registro=fecha_registro,
                email=email,  # Agregar el parámetro 'email'
            )

            print(
                f"Caregiver {nombre} {apellido} registered in Firestore successfully."
            )
            return True
        else:
            print("Signup for caregiver failed.")
            return False
