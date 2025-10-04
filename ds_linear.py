
"""
Implementaciones de Estructuras de Datos Lineales:
- ArrayList (envoltura de list)
- SinglyLinkedList (Lista Enlazada Simple)
- Stack (Pila)
- Queue (Cola)
Estas implementaciones son simples y adecuadas para un prototipo académico.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Generic, Iterable, Iterator, Optional, TypeVar, List

T = TypeVar("T")

class ArrayList(Generic[T]):
    """
    Envoltura ligera sobre list de Python para enfatizar su uso como 'arreglo dinámico'.
    Incluye búsqueda binaria opcional cuando la lista está ordenada por una clave (key_fn).
    """
    def __init__(self, iterable: Optional[Iterable[T]] = None, key_fn: Optional[Callable[[T], Any]] = None):
        self._data: List[T] = list(iterable) if iterable is not None else []
        self._key_fn = key_fn

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)

    def get(self, index: int) -> T:
        return self._data[index]

    def set(self, index: int, value: T) -> None:
        self._data[index] = value

    def append(self, value: T) -> None:
        self._data.append(value)

    def remove_at(self, index: int) -> T:
        return self._data.pop(index)

    def remove_first(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for i, x in enumerate(self._data):
            if predicate(x):
                return self._data.pop(i)
        return None

    def find_first(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for x in self._data:
            if predicate(x):
                return x
        return None

    def to_list(self) -> List[T]:
        return list(self._data)

    def sort_inplace(self) -> None:
        if self._key_fn:
            self._data.sort(key=self._key_fn)
        else:
            self._data.sort()

    def binary_search_index(self, key_value: Any) -> int:
        """Devuelve el índice del primer elemento cuyo key_fn(x)==key_value, o -1 si no existe.
        Requiere que el arreglo esté ordenado por esa clave.
        """
        if not self._key_fn:
            raise ValueError("binary_search_index requiere key_fn definido")
        lo, hi = 0, len(self._data) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            k = self._key_fn(self._data[mid])
            if k == key_value:
                return mid
            elif k < key_value:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


@dataclass
class _Node(Generic[T]):
    value: T
    next: Optional["_Node[T]"] = None

class SinglyLinkedList(Generic[T]):
    """Lista enlazada simple con operaciones básicas."""
    def __init__(self) -> None:
        self.head: Optional[_Node[T]] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def push_front(self, value: T) -> None:
        node = _Node(value=value, next=self.head)
        self.head = node
        self._size += 1

    def remove_first(self, predicate: Callable[[T], bool]) -> Optional[T]:
        prev: Optional[_Node[T]] = None
        cur = self.head
        while cur:
            if predicate(cur.value):
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                self._size -= 1
                return cur.value
            prev, cur = cur, cur.next
        return None

    def find_first(self, predicate: Callable[[T], bool]) -> Optional[T]:
        cur = self.head
        while cur:
            if predicate(cur.value):
                return cur.value
            cur = cur.next
        return None


class Stack(Generic[T]):
    """Pila con lista subyacente (LIFO)."""
    def __init__(self) -> None:
        self._data: List[T] = []

    def push(self, value: T) -> None:
        self._data.append(value)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> T:
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)


class Queue(Generic[T]):
    """Cola simple (FIFO) basada en lista. Para prototipo académico es suficiente."""
    def __init__(self) -> None:
        self._data: List[T] = []

    def enqueue(self, value: T) -> None:
        self._data.append(value)

    def dequeue(self) -> T:
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.pop(0)

    def peek(self) -> T:
        if not self._data:
            raise IndexError("peek from empty queue")
        return self._data[0]

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0
