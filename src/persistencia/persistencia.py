import json
from typing import List, Dict, Any, Type, TypeVar, Callable
from dataclasses import asdict

T = TypeVar('T')

def guardar_a_json(objetos: List[Any], ruta_archivo: str) -> None:
    """
    Guarda una lista de objetos en un archivo JSON.
    
    Args:
        objetos: Lista de objetos a guardar
        ruta_archivo: Ruta del archivo JSON donde guardar los datos
    """
    # Convertir objetos a diccionarios
    datos = [asdict(obj) for obj in objetos]
    
    # Guardar en archivo JSON
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_desde_json(ruta_archivo: str, clase: Type[T], constructor: Callable[[Dict[str, Any]], T] = None) -> List[T]:
    """
    Carga datos desde un archivo JSON y los convierte en objetos de la clase especificada.
    
    Args:
        ruta_archivo: Ruta del archivo JSON a cargar
        clase: Clase a la que convertir los datos
        constructor: Función opcional para construir objetos (si no se proporciona, se usa la clase directamente)
        
    Returns:
        Lista de objetos de la clase especificada
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        
        # Convertir diccionarios a objetos
        if constructor:
            return [constructor(item) for item in datos]
        else:
            return [clase(**item) for item in datos]
    except FileNotFoundError:
        # Si el archivo no existe, devolver lista vacía
        return []
    except json.JSONDecodeError:
        # Si hay error en el formato JSON, devolver lista vacía
        print(f"Error: El archivo {ruta_archivo} no tiene un formato JSON válido.")
        return []
