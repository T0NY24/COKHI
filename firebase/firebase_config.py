import firebase_admin
from firebase_admin import credentials, auth
import pyrebase

# Configuración para Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Configuración para Pyrebase (frontend)
firebase_config = {
    "apiKey": "TU_API_KEY",
    "authDomain": "TU_PROYECTO.firebaseapp.com",
    "databaseURL": "https://TU_PROYECTO.firebaseio.com",
    "projectId": "TU_PROYECTO",
    "storageBucket": "TU_PROYECTO.appspot.com",
    "messagingSenderId": "TU_MESSAGING_ID",
    "appId": "TU_APP_ID"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
