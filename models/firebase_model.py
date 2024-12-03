# models/firebase_model.py
import pyrebase

class FirebaseModel:
    def __init__(self):
        self.firebase_config = {
            "apiKey": "AIzaSyAr5AUqKB-qXEHXn8vgFX8hndpITFkncTY",
            "authDomain": "hubuide.firebaseapp.com",
            "projectId": "hubuide",
            "storageBucket": "hubuide.firebasestorage.app",
            "messagingSenderId": "767282462248",
            "appId": "767282462248:web:d27c9856a65bfe6d38ff1d",
            "databaseURL": ""
        }
        self.firebase = pyrebase.initialize_app(self.firebase_config)
        self.auth = self.firebase.auth()

    def login(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            return user
        except Exception as e:
            print("Error during login:", e)
            return None

    def signup(self, email, password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            return user
        except Exception as e:
            print("Error during signup:", e)
            return None
