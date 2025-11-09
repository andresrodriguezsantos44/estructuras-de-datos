from typing import List, Optional, Dict, Any
from models import Editorial, Genero
from arboles import ArbolBinarioBusqueda
from persistencia import guardar_a_json, cargar_desde_json

class SearchService:
    """
    Servicio de búsqueda que utiliza árboles binarios de búsqueda para
    almacenar y buscar editoriales y géneros.
    """
    def __init__(self):
        # Árbol para editoriales, ordenado por nombre
        self.arbol_editoriales = ArbolBinarioBusqueda[str, Editorial]()
        
        # Árbol para géneros, ordenado por nombre
        self.arbol_generos = ArbolBinarioBusqueda[str, Genero]()
        
        # Rutas de archivos JSON
        self.ruta_editoriales = "editoriales.json"
        self.ruta_generos = "generos.json"
    
    def cargar_editoriales(self, editoriales: List[Editorial]) -> None:
        """Carga una lista de editoriales en el árbol."""
        for editorial in editoriales:
            self.arbol_editoriales.insertar(editorial.nombre.lower(), editorial)
    
    def cargar_generos(self, generos: List[Genero]) -> None:
        """Carga una lista de géneros en el árbol."""
        for genero in generos:
            self.arbol_generos.insertar(genero.nombre.lower(), genero)
    
    def buscar_editorial(self, nombre: str) -> Optional[Editorial]:
        """Busca una editorial por su nombre."""
        return self.arbol_editoriales.buscar(nombre.lower())
    
    def buscar_genero(self, nombre: str) -> Optional[Genero]:
        """Busca un género por su nombre."""
        return self.arbol_generos.buscar(nombre.lower())
    
    def listar_editoriales(self) -> List[Editorial]:
        """Lista todas las editoriales en orden alfabético."""
        return self.arbol_editoriales.recorrer_inorden()
    
    def listar_generos(self) -> List[Genero]:
        """Lista todos los géneros en orden alfabético."""
        return self.arbol_generos.recorrer_inorden()
    
    def insertar_editorial(self, editorial: Editorial) -> bool:
        """Inserta una nueva editorial en el árbol y actualiza el archivo JSON."""
        # Verificar si ya existe una editorial con el mismo nombre
        if self.buscar_editorial(editorial.nombre):
            return False  # Ya existe una editorial con ese nombre
        
        # Insertar en el árbol
        self.arbol_editoriales.insertar(editorial.nombre.lower(), editorial)
        
        # Actualizar el archivo JSON
        self._guardar_editoriales()
        return True
    
    def insertar_genero(self, genero: Genero) -> bool:
        """Inserta un nuevo género en el árbol y actualiza el archivo JSON."""
        # Verificar si ya existe un género con el mismo nombre
        if self.buscar_genero(genero.nombre):
            return False  # Ya existe un género con ese nombre
        
        # Insertar en el árbol
        self.arbol_generos.insertar(genero.nombre.lower(), genero)
        
        # Actualizar el archivo JSON
        self._guardar_generos()
        return True
    
    def actualizar_editorial(self, nombre_original: str, datos_actualizados: Dict[str, Any]) -> bool:
        """Actualiza una editorial existente y el archivo JSON."""
        # Buscar la editorial por su nombre
        editorial = self.buscar_editorial(nombre_original)
        if not editorial:
            return False  # No existe la editorial
        
        # Si se cambia el nombre, verificar que el nuevo nombre no exista
        if "nombre" in datos_actualizados and datos_actualizados["nombre"].lower() != nombre_original.lower():
            if self.buscar_editorial(datos_actualizados["nombre"]):
                return False  # Ya existe una editorial con el nuevo nombre
        
        # Actualizar los campos de la editorial
        for campo, valor in datos_actualizados.items():
            if hasattr(editorial, campo):
                setattr(editorial, campo, valor)
        
        # Si cambió el nombre, hay que eliminar y reinsertar con la nueva clave
        if "nombre" in datos_actualizados and datos_actualizados["nombre"].lower() != nombre_original.lower():
            # Obtener todas las editoriales excepto la actualizada
            editoriales = [e for e in self.listar_editoriales() if e.id != editorial.id]
            # Reinicializar el árbol
            self.arbol_editoriales = ArbolBinarioBusqueda[str, Editorial]()
            # Insertar todas las editoriales incluyendo la actualizada
            self.cargar_editoriales(editoriales + [editorial])
        
        # Actualizar el archivo JSON
        self._guardar_editoriales()
        return True
    
    def actualizar_genero(self, nombre_original: str, datos_actualizados: Dict[str, Any]) -> bool:
        """Actualiza un género existente y el archivo JSON."""
        # Buscar el género por su nombre
        genero = self.buscar_genero(nombre_original)
        if not genero:
            return False  # No existe el género
        
        # Si se cambia el nombre, verificar que el nuevo nombre no exista
        if "nombre" in datos_actualizados and datos_actualizados["nombre"].lower() != nombre_original.lower():
            if self.buscar_genero(datos_actualizados["nombre"]):
                return False  # Ya existe un género con el nuevo nombre
        
        # Actualizar los campos del género
        for campo, valor in datos_actualizados.items():
            if hasattr(genero, campo):
                setattr(genero, campo, valor)
        
        # Si cambió el nombre, hay que eliminar y reinsertar con la nueva clave
        if "nombre" in datos_actualizados and datos_actualizados["nombre"].lower() != nombre_original.lower():
            # Obtener todos los géneros excepto el actualizado
            generos = [g for g in self.listar_generos() if g.id != genero.id]
            # Reinicializar el árbol
            self.arbol_generos = ArbolBinarioBusqueda[str, Genero]()
            # Insertar todos los géneros incluyendo el actualizado
            self.cargar_generos(generos + [genero])
        
        # Actualizar el archivo JSON
        self._guardar_generos()
        return True
    
    def _guardar_editoriales(self) -> None:
        """Guarda todas las editoriales en el archivo JSON."""
        editoriales = self.listar_editoriales()
        guardar_a_json(editoriales, self.ruta_editoriales)
    
    def _guardar_generos(self) -> None:
        """Guarda todos los géneros en el archivo JSON."""
        generos = self.listar_generos()
        guardar_a_json(generos, self.ruta_generos)
