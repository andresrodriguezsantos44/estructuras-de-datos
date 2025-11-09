
import unittest
import sys
import os

# Agregar el directorio raíz al path para poder importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modelos.models import Book, User
from src.servicios.library_service import LibraryService

class TestBibliotecaLineal(unittest.TestCase):
    def setUp(self):
        self.svc = LibraryService()
        # Datos base
        self.svc.agregar_libro(Book("978-1", "Estructuras", "Ayala", 2020, 3, 3))
        self.svc.agregar_libro(Book("978-2", "Algoritmos", "Fritelli", 2020, 1, 1))
        self.svc.registrar_usuario(User("U1", "Ana", "ana@example.com"))
        self.svc.registrar_usuario(User("U2", "Luis", "luis@example.com"))

    def test_registro_y_busqueda_libro(self):
        b = self.svc.obtener_libro("978-1")
        self.assertIsNotNone(b)
        self.assertEqual(b.titulo, "Estructuras")
        self.assertEqual(b.ejemplares_disponibles, 3)

    def test_prestar_y_devolver(self):
        loan_id = self.svc.prestar_libro("978-1", "U1", dias=5)
        self.assertIsNotNone(loan_id)
        libro = self.svc.obtener_libro("978-1")
        self.assertEqual(libro.ejemplares_disponibles, 2)
        # Devolver
        ok = self.svc.devolver_libro(loan_id)
        self.assertTrue(ok)
        libro = self.svc.obtener_libro("978-1")
        self.assertEqual(libro.ejemplares_disponibles, 3)

    def test_reserva_cuando_no_hay_disponibles(self):
        # Solo 1 ejemplar, prestamos a U1 y U2 intenta
        lid = self.svc.prestar_libro("978-2", "U1")
        self.assertIsNotNone(lid)
        lid2 = self.svc.prestar_libro("978-2", "U2")
        self.assertIsNone(lid2)  # Se encola reserva
        # Al devolver, debe generarse préstamo automático a U2
        self.assertTrue(self.svc.devolver_libro(lid))
        # Debe existir un préstamo activo para U2 del ISBN 978-2
        activos = self.svc.listar_prestamos_activos()
        self.assertTrue(any(p.user_id == "U2" and p.isbn == "978-2" for p in activos))

if __name__ == "__main__":
    unittest.main()
