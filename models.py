
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional

@dataclass
class Book:
    isbn: str
    titulo: str
    autor: str
    anio_publicacion: int
    ejemplares_totales: int
    ejemplares_disponibles: int
    # La cola de reservas será gestionada en el servicio (por libro),
    # pero dejamos un flag simple para saber si hay reservas pendientes.
    tiene_reservas: bool = False

@dataclass
class User:
    user_id: str  # p. ej. documento o código institucional
    nombre: str
    email: str

@dataclass
class Loan:
    loan_id: str
    user_id: str
    isbn: str
    fecha_prestamo: date
    fecha_devolucion_estimada: date
    fecha_devolucion_real: Optional[date] = None
    devuelto: bool = False

    def marcar_devuelto(self) -> None:
        self.devuelto = True
        self.fecha_devolucion_real = date.today()

@dataclass
class Editorial:
    id: str
    nombre: str
    pais: str
    anio_fundacion: int

@dataclass
class Genero:
    id: str
    nombre: str
    descripcion: str
