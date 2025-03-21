# tests/test_main.py

import unittest
from main import saludo

class TestSaludo(unittest.TestCase):
    def test_saludo_mundo(self):
        resultado = saludo("Mundo")
        self.assertEqual(resultado, "Hola, Mundo!")

    def test_saludo_personalizado(self):
        nombre_prueba = "ChatGPT"
        resultado = saludo(nombre_prueba)
        self.assertNotEqual(resultado, "Hola, ChatGPT!")

if __name__ == '__main__':
    unittest.main()
