# controllers/auth_controller.py
from models.firebase_model import FirebaseModel

class AuthController:
    def __init__(self):
        self.firebase_model = FirebaseModel()

    def login_user(self, email, password):
        user = self.firebase_model.login(email, password)
        if user:
            print(f"Welcome back, {email}")
            return True
        else:
            print("Login failed. Please check your credentials.")
            return False

    def signup_user(self, email, password):
        user = self.firebase_model.signup(email, password)
        if user:
            print(f"Account created successfully for {email}")
            return True
        else:
            print("Signup failed.")
            return False
