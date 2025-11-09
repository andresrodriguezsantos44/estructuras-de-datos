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

## Estructura del Proyecto

```
estructuras-de-datos/
├── app.py                  # Aplicación principal con menú CLI
├── Informe.md              # Documentación del proyecto
├── README.md               # Este archivo
├── src/                    # Código fuente
│   ├── __init__.py          # Inicialización del paquete
│   ├── estructuras/         # Estructuras de datos
│   │   ├── __init__.py      # Inicialización del paquete
│   │   ├── ds_linear.py     # Estructuras lineales (ArrayList, LinkedList, Stack, Queue)
│   │   └── arboles.py       # Árbol Binario de Búsqueda genérico
│   ├── modelos/            # Modelos de datos
│   │   ├── __init__.py      # Inicialización del paquete
│   │   └── models.py        # Clases Book, User, Loan, Editorial, Genero
│   ├── servicios/          # Servicios de negocio
│   │   ├── __init__.py      # Inicialización del paquete
│   │   ├── library_service.py # Servicio de biblioteca (estructuras lineales)
│   │   └── search_service.py # Servicio de búsqueda (árboles)
│   └── persistencia/       # Manejo de persistencia
│       ├── __init__.py      # Inicialización del paquete
│       └── persistencia.py   # Funciones para guardar/cargar datos JSON
├── tests/                 # Pruebas unitarias
│   ├── __init__.py          # Inicialización del paquete
│   ├── tests_unittest.py    # Pruebas para estructuras lineales
│   └── tests_arboles.py     # Pruebas para árboles
└── data/                  # Archivos de datos
    ├── editoriales.json     # Datos de editoriales
    └── generos.json         # Datos de géneros
```

### Etapa 1: Estructuras Lineales

Implementación de estructuras de datos lineales para la gestión de biblioteca:

- Arreglos dinámicos (ArrayList) para almacenar libros
- Listas enlazadas (SinglyLinkedList) para usuarios
- Pilas (Stack) para historial de operaciones
- Colas (Queue) para reservas de libros

### Etapa 2: Árboles Binarios

Implementación de estructuras no lineales para búsquedas eficientes:

- Árbol Binario de Búsqueda genérico
- Servicio de búsqueda para editoriales y géneros
- Persistencia de datos en archivos JSON

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
