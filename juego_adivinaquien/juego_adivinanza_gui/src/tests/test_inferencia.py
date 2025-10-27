import unittest
from juegoadivinanza import inferencia

class TestInferencia(unittest.TestCase):

    def setUp(self):
        self.artistas = [
            "Shakira", "Bad Bunny", "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé", "Rihanna",
            "Bruno Mars", "Lady Gaga", "Justin Bieber", "Selena Gomez", "Dua Lipa", "J Balvin", "Karol G",
            "Maluma", "Camila Cabello", "Billie Eilish", "The Weeknd", "Harry Styles", "Luis Miguel",
            "Juanes", "Rosalía", "Enrique Iglesias", "Daddy Yankee", "Ozuna", "Natti Natasha", "Anitta",
            "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande", "Jennifer Lopez", "Marc Anthony",
            "Gloria Trevi", "Alejandro Sanz", "Pablo Alborán", "Manuel Turizo", "Sebastián Yatra",
            "Carlos Vives", "Lali Espósito"
        ]

    def test_inferencia_con_respuestas_si(self):
        hechos = {
            "¿Es mujer?": "si",
            "¿Canta pop?": "si",
            "¿Canta en español?": "si"
        }
        resultado = inferencia(hechos)
        self.assertIn("Shakira", resultado)
        self.assertIn("Adele", resultado)
        self.assertIn("Selena Gomez", resultado)

    def test_inferencia_con_respuestas_no(self):
        hechos = {
            "¿Es mujer?": "no",
            "¿Canta reggaetón?": "si"
        }
        resultado = inferencia(hechos)
        self.assertIn("Bad Bunny", resultado)
        self.assertIn("J Balvin", resultado)
        self.assertNotIn("Shakira", resultado)

    def test_inferencia_con_respuestas_mixtas(self):
        hechos = {
            "¿Es mujer?": "si",
            "¿Canta reggaetón?": "no"
        }
        resultado = inferencia(hechos)
        self.assertIn("Taylor Swift", resultado)
        self.assertNotIn("Karol G", resultado)

    def test_inferencia_sin_respuestas(self):
        hechos = {}
        resultado = inferencia(hechos)
        self.assertEqual(len(resultado), len(self.artistas))

if __name__ == '__main__':
    unittest.main()