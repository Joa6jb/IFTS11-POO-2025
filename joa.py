import unittest
from hola import Perro, UsuarioAdoptante

class TestPerro(unittest.TestCase):
    def setUp(self):
        # Crear un objeto Perro para usar en las pruebas
        self.perro = Perro(
            nombre="Max",
            raza="Labrador",
            edad=5,
            tamaño="Grande",
            peso=30,
            estado_salud="Saludable",
            vacunado=True,
            estado="disponible",
            temperamento="Juguetón",
            id=1
        )

    def test_inicializacion(self):
        # Verificar que los atributos se inicializan correctamente
        self.assertEqual(self.perro.nombre, "Max")
        self.assertEqual(self.perro.raza, "Labrador")
        self.assertEqual(self.perro.edad, 5)
        self.assertEqual(self.perro.tamaño, "Grande")
        self.assertEqual(self.perro.estado, "disponible")

    def test_cambiar_estado_valido(self):
        # Probar cambiar el estado a un valor válido
        self.perro.cambiar_estado("adoptado")
        self.assertEqual(self.perro.estado, "adoptado")

    def test_cambiar_estado_invalido(self):
        # Probar cambiar el estado a un valor inválido
        with self.assertRaises(ValueError):
            self.perro.cambiar_estado("inexistente")

    def test_mostrar_informacion(self):
        # Probar que mostrar_informacion no lanza errores
        self.perro.mostrar_informacion()

class TestUsuarioAdoptante(unittest.TestCase):
    def setUp(self):
        # Crear un objeto UsuarioAdoptante para usar en las pruebas
        self.usuario = UsuarioAdoptante(
            nombre="Juan",
            dni="12345678",
            email="juan@example.com",
            preferencias={"raza": "Labrador", "edad": "Joven", "tamaño": "Grande"},
            historial_adopciones=[]
        )

    def test_inicializacion(self):
        # Verificar que los atributos se inicializan correctamente
        self.assertEqual(self.usuario.nombre, "Juan")
        self.assertEqual(self.usuario.dni, "12345678")
        self.assertEqual(self.usuario.email, "juan@example.com")
        self.assertEqual(self.usuario.preferencias["raza"], "Labrador")

    def test_modificar_preferencias(self):
        # Probar la modificación de preferencias
        self.usuario.preferencias["edad"] = "Adulto"
        self.assertEqual(self.usuario.preferencias["edad"], "Adulto")

    def test_historial_adopciones(self):
        # Probar que el historial de adopciones se actualiza correctamente
        self.usuario.historial_adopciones.append("Max")
        self.assertIn("Max", self.usuario.historial_adopciones)

if __name__ == "__main__":
    unittest.main()