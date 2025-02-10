import unittest
import flet as ft
from views.views import main

class TestMainView(unittest.TestCase):
    def test_ui_render(self):
        try:
            main(ft.Page())  # Intenta ejecutar la UI con un objeto Page simulado
            success = True
        except Exception as e:
            print(f"Error en UI: {e}")
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
