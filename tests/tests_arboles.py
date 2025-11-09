import unittest
import sys
import os

# Agregar el directorio raíz al path para poder importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.estructuras.arboles import ArbolBinarioBusqueda

class TestArbolBinarioBusqueda(unittest.TestCase):
    def setUp(self):
        # Crear un árbol para las pruebas
        self.arbol = ArbolBinarioBusqueda()
        
    def test_insercion(self):
        """Prueba la inserción de nodos en el árbol."""
        self.arbol.insertar("B", "Valor B")
        self.arbol.insertar("A", "Valor A")
        self.arbol.insertar("C", "Valor C")
        
        # Verificar que el árbol tiene la estructura correcta
        self.assertEqual(self.arbol.raiz.clave, "B")
        self.assertEqual(self.arbol.raiz.izquierdo.clave, "A")
        self.assertEqual(self.arbol.raiz.derecho.clave, "C")
        
    def test_busqueda_exitosa(self):
        """Prueba la búsqueda exitosa de un nodo existente."""
        self.arbol.insertar("B", "Valor B")
        self.arbol.insertar("A", "Valor A")
        self.arbol.insertar("C", "Valor C")
        
        # Buscar nodos existentes
        self.assertEqual(self.arbol.buscar("A"), "Valor A")
        self.assertEqual(self.arbol.buscar("B"), "Valor B")
        self.assertEqual(self.arbol.buscar("C"), "Valor C")
        
    def test_busqueda_fallida(self):
        """Prueba la búsqueda fallida de un nodo inexistente."""
        self.arbol.insertar("B", "Valor B")
        self.arbol.insertar("A", "Valor A")
        self.arbol.insertar("C", "Valor C")
        
        # Buscar un nodo que no existe
        self.assertIsNone(self.arbol.buscar("D"))
        
    def test_recorrido_inorden(self):
        """Prueba el recorrido inorden que devuelve los datos en orden alfabético."""
        # Insertar nodos en un orden específico
        self.arbol.insertar("C", "Valor C")
        self.arbol.insertar("A", "Valor A")
        self.arbol.insertar("B", "Valor B")
        self.arbol.insertar("E", "Valor E")
        self.arbol.insertar("D", "Valor D")
        
        # El recorrido inorden debe devolver los valores ordenados por clave
        valores = self.arbol.recorrer_inorden()
        claves_esperadas = ["Valor A", "Valor B", "Valor C", "Valor D", "Valor E"]
        
        self.assertEqual(valores, claves_esperadas)

if __name__ == "__main__":
    unittest.main()
