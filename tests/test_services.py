import unittest
from models.firebase_model import FirebaseModel

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth = FirebaseModel()

    def test_login(self):
        result = self.auth.login("anperezcue@uide.edu.ec", "123456")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()