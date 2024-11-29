# firebase_config.py
import firebase_admin
from firebase_admin import credentials

# Inicializa Firebase usando el archivo de claves
cred = credentials.Certificate("path/to/your/firebase-adminsdk-key.json")
firebase_admin.initialize_app(cred)
