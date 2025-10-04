
from __future__ import annotations
from typing import Dict, Optional, List
from datetime import date, timedelta
from models import Book, User, Loan
from ds_linear import ArrayList, SinglyLinkedList, Stack, Queue

class LibraryService:
    """
    Capa de servicio que maneja las estructuras de datos y reglas de negocio.
    - Libros: ArrayList ordenado por ISBN (permite búsqueda binaria).
    - Usuarios: Lista Enlazada Simple (inserción/eliminación eficientes en cabecera).
    - Reservas por libro: Cola de user_id.
    - Historial: Pila de operaciones (pila LIFO) para auditoría sencilla.
    """
    def __init__(self) -> None:
        self.libros = ArrayList[Book](key_fn=lambda b: b.isbn)  # almacenados ordenados
        self.usuarios = SinglyLinkedList[User]()
        self.prestamos: Dict[str, Loan] = {}  # loan_id -> Loan
        self.reservas_por_libro: Dict[str, Queue[str]] = {}  # isbn -> cola de user_id
        self.historial = Stack[str]()

    # ---------------------- Libros ----------------------
    def agregar_libro(self, libro: Book) -> None:
        # Insertamos y mantenemos ordenado por ISBN
        self.libros.append(libro)
        self.libros.sort_inplace()
        self.historial.push(f"ADD_BOOK {libro.isbn}")

    def _buscar_indice_libro_por_isbn(self, isbn: str) -> int:
        return self.libros.binary_search_index(isbn)

    def obtener_libro(self, isbn: str) -> Optional[Book]:
        idx = self._buscar_indice_libro_por_isbn(isbn)
        if idx == -1:
            return None
        return self.libros.get(idx)

    def actualizar_libro(self, isbn: str, **kwargs) -> bool:
        idx = self._buscar_indice_libro_por_isbn(isbn)
        if idx == -1:
            return False
        libro = self.libros.get(idx)
        for k, v in kwargs.items():
            if hasattr(libro, k):
                setattr(libro, k, v)
        # Si cambia ISBN, reordenamos
        if "isbn" in kwargs:
            self.libros.sort_inplace()
        self.historial.push(f"UPDATE_BOOK {isbn}")
        return True

    def eliminar_libro(self, isbn: str) -> bool:
        idx = self._buscar_indice_libro_por_isbn(isbn)
        if idx == -1:
            return False
        self.libros.remove_at(idx)
        self.reservas_por_libro.pop(isbn, None)
        self.historial.push(f"DELETE_BOOK {isbn}")
        return True

    def listar_libros(self) -> List[Book]:
        return self.libros.to_list()

    # ---------------------- Usuarios ----------------------
    def registrar_usuario(self, user: User) -> None:
        self.usuarios.push_front(user)
        self.historial.push(f"ADD_USER {user.user_id}")

    def obtener_usuario(self, user_id: str) -> Optional[User]:
        return self.usuarios.find_first(lambda u: u.user_id == user_id)

    def eliminar_usuario(self, user_id: str) -> bool:
        removed = self.usuarios.remove_first(lambda u: u.user_id == user_id)
        if removed:
            self.historial.push(f"DELETE_USER {user_id}")
            return True
        return False

    def listar_usuarios(self) -> List[User]:
        return list(self.usuarios)

    # ---------------------- Reservas ----------------------
    def _cola_reservas(self, isbn: str) -> Queue[str]:
        if isbn not in self.reservas_por_libro:
            self.reservas_por_libro[isbn] = Queue[str]()
        return self.reservas_por_libro[isbn]

    def reservar_libro(self, isbn: str, user_id: str) -> bool:
        libro = self.obtener_libro(isbn)
        usuario = self.obtener_usuario(user_id)
        if not libro or not usuario:
            return False
        cola = self._cola_reservas(isbn)
        cola.enqueue(user_id)
        libro.tiene_reservas = True
        self.historial.push(f"RESERVE {isbn} by {user_id}")
        return True

    # ---------------------- Préstamos ----------------------
    def prestar_libro(self, isbn: str, user_id: str, dias: int = 7) -> Optional[str]:
        libro = self.obtener_libro(isbn)
        usuario = self.obtener_usuario(user_id)
        if not libro or not usuario:
            return None

        # Si no hay ejemplares disponibles, encolar reserva automáticamente
        if libro.ejemplares_disponibles <= 0:
            self.reservar_libro(isbn, user_id)
            return None

        libro.ejemplares_disponibles -= 1
        loan_id = f"L{len(self.prestamos)+1:05d}"
        prestamo = Loan(
            loan_id=loan_id,
            user_id=user_id,
            isbn=isbn,
            fecha_prestamo=date.today(),
            fecha_devolucion_estimada=date.today() + timedelta(days=dias),
        )
        self.prestamos[loan_id] = prestamo
        self.historial.push(f"LOAN {loan_id}")
        return loan_id

    def devolver_libro(self, loan_id: str) -> bool:
        prestamo = self.prestamos.get(loan_id)
        if not prestamo or prestamo.devuelto:
            return False
        prestamo.marcar_devuelto()

        libro = self.obtener_libro(prestamo.isbn)
        if libro:
            libro.ejemplares_disponibles += 1
            # Atender la primera reserva si existe
            cola = self._cola_reservas(libro.isbn)
            if not cola.is_empty():
                siguiente_user = cola.dequeue()
                # Asignar préstamo inmediato al siguiente en la cola (si hay stock)
                if libro.ejemplares_disponibles > 0:
                    libro.ejemplares_disponibles -= 1
                    nuevo_id = f"L{len(self.prestamos)+1:05d}"
                    nuevo_prestamo = Loan(
                        loan_id=nuevo_id,
                        user_id=siguiente_user,
                        isbn=libro.isbn,
                        fecha_prestamo=date.today(),
                        fecha_devolucion_estimada=date.today() + timedelta(days=7),
                    )
                    self.prestamos[nuevo_id] = nuevo_prestamo
                    self.historial.push(f"AUTO_LOAN_FROM_QUEUE {nuevo_id}")
                # actualizar bandera reservas
                libro.tiene_reservas = not cola.is_empty()
            else:
                libro.tiene_reservas = False

        self.historial.push(f"RETURN {loan_id}")
        return True

    def listar_prestamos_activos(self) -> List[Loan]:
        return [p for p in self.prestamos.values() if not p.devuelto]

    def obtener_prestamo(self, loan_id: str) -> Optional[Loan]:
        return self.prestamos.get(loan_id)

    # ---------------------- Auditoría ----------------------
    def ver_top_historial(self) -> Optional[str]:
        return self.historial.peek() if len(self.historial) > 0 else None
