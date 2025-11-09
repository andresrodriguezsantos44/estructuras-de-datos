# Biblioteca (Python)

## Requisitos

- Python 3.9+

## Ejecutar CLI

```bash
python3 app.py
```

## Ejecutar pruebas

```bash
python3 -m unittest tests_unittest.py -v
python3 -m unittest tests_arboles.py -v
```

## Estructura

### Etapa 1: Estructuras Lineales

- `ds_linear.py`: estructuras lineales (ArrayList, SinglyLinkedList, Stack, Queue)
- `models.py`: dataclasses Book, User, Loan
- `library_service.py`: reglas de negocio
- `app.py`: menú por línea de comando
- `tests_unittest.py`: pruebas unitarias
- `Informe.md`: reporte con requisitos, diseño, decisiones y referencias

### Etapa 2: Árboles Binarios

- `arboles.py`: implementación de Árbol Binario de Búsqueda genérico
- `search_service.py`: servicio de búsqueda usando árboles para editoriales y géneros
- `persistencia.py`: funciones para guardar y cargar datos en formato JSON
- `tests_arboles.py`: pruebas unitarias para árboles
- `editoriales.json`: datos de editoriales en formato JSON
- `generos.json`: datos de géneros en formato JSON

## Menú de Búsquedas y Gestión

El sistema ahora incluye una nueva opción "Búsquedas y Gestión (Árboles)" que permite:

1. Buscar editorial por nombre
2. Buscar género por nombre
3. Listar todas las editoriales en orden alfabético
4. Listar todos los géneros en orden alfabético
5. Insertar nueva editorial
6. Insertar nuevo género
7. Actualizar editorial existente
8. Actualizar género existente

## Flujo de Búsqueda

1. Seleccionar opción 4 en el menú principal
2. Elegir tipo de búsqueda (editorial o género)
3. Ingresar nombre a buscar o seleccionar listar todos
4. Ver resultados ordenados alfabéticamente
