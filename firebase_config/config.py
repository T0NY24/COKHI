import firebase_admin
from firebase_admin import credentials

# Ruta completa al archivo JSON
cred = credentials.Certificate(r'hubuide-firebase-adminsdk-4p82r-a64a881b58.json')

# Inicializa la app de Firebase
firebase_admin.initialize_app(cred)
