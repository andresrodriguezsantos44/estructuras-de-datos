from __future__ import annotations
from typing import Any, Callable, Generic, Optional, TypeVar, List

T = TypeVar("T")
K = TypeVar("K")

class NodoArbol(Generic[K, T]):
    """Nodo para el Árbol Binario de Búsqueda."""
    def __init__(self, clave: K, valor: T):
        self.clave: K = clave
        self.valor: T = valor
        self.izquierdo: Optional[NodoArbol[K, T]] = None
        self.derecho: Optional[NodoArbol[K, T]] = None

class ArbolBinarioBusqueda(Generic[K, T]):
    """
    Árbol Binario de Búsqueda genérico.
    - Permite insertar datos con una clave y un valor.
    - Buscar un nodo por clave.
    - Recorrer el árbol en orden (inorden).
    """
    def __init__(self, key_fn: Optional[Callable[[T], K]] = None):
        self.raiz: Optional[NodoArbol[K, T]] = None
        self.key_fn = key_fn  # Función opcional para extraer la clave del valor

    def insertar(self, clave: K, valor: T) -> None:
        """Inserta un nuevo nodo con la clave y valor dados."""
        if self.raiz is None:
            self.raiz = NodoArbol(clave, valor)
        else:
            self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo: NodoArbol[K, T], clave: K, valor: T) -> None:
        """Método auxiliar recursivo para insertar un nodo."""
        if clave < nodo.clave:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, clave, valor)
        else:  # clave >= nodo.clave, permitimos duplicados a la derecha
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.derecho, clave, valor)

    def buscar(self, clave: K) -> Optional[T]:
        """Busca un valor por su clave. Retorna None si no lo encuentra."""
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo: Optional[NodoArbol[K, T]], clave: K) -> Optional[T]:
        """Método auxiliar recursivo para buscar un nodo."""
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo.valor
        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave)
        return self._buscar_recursivo(nodo.derecho, clave)

    def recorrer_inorden(self) -> List[T]:
        """Recorre el árbol en orden (inorden) y devuelve una lista con los valores."""
        resultado: List[T] = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo: Optional[NodoArbol[K, T]], resultado: List[T]) -> None:
        """Método auxiliar recursivo para recorrer el árbol en orden."""
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)
