import pyrebase
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, auth

# Cargar las variables de entorno desde .env
load_dotenv()
cred = credentials.Certificate("HubUIDE\serviceAccountKey.json")
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
firebase_admin.initialize_app(cred)
def get_auth():
    return auth