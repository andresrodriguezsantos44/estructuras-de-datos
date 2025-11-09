# Sistema de Gestión de Biblioteca (Prototipo con Estructuras de Datos Lineales)

**Portada**  
**Curso:** Estructura de Datos
**Proyecto:** Sistema de Gestión de Biblioteca (Etapa 1)
**Autor:** Andres Alfonso Rodriguez Santos
**Profesor:** William Ruiz
**Universidad:** Corporación Universitaria Iberoamericana
**Carrera:** Ingeniería de Software
**Fecha:** October 04, 2025

## Introducción

Este documento presenta el análisis, diseño e implementación de un prototipo de sistema de gestión de biblioteca que utiliza **estructuras de datos lineales** —arreglos (listas), listas enlazadas, pilas y colas— para almacenar y administrar libros, usuarios y préstamos. El objetivo es **comunicar los parámetros de los datos a almacenar** y **elegir estructuras congruentes con los requisitos**, cumpliendo los resultados de aprendizaje de la unidad.

## Requerimientos del sistema

### Funcionales

- Registrar, listar, buscar, actualizar y eliminar **libros**.
- Registrar, listar, buscar y eliminar **usuarios**.
- **Prestar** y **devolver** libros con control de disponibilidad.
- Gestionar **reservas** mediante **colas** cuando no haya ejemplares disponibles.
- Mostrar un **historial** básico de operaciones mediante **pila**.
- Listar **préstamos activos**.

### No funcionales

- Prototipo ejecutable por **línea de comandos (CLI)**.
- Código legible y modular, con **buenas prácticas** (nombres claros, comentarios básicos, separación por capas).
- **Pruebas unitarias** sobre 2–3 casos críticos.
- Persistencia **no requerida** para la etapa (el enfoque está en las estructuras en memoria).

## Selección de estructuras de datos (enfoque)

### Libros

* **Estructura:** `ArrayList` (arreglo dinámico) ordenado por ISBN
* **Justificación:** Permite acceso e iteración rápida; mantener el orden por clave facilita localizar libros por ISBN.


### Usuarios

* **Estructura:** `Lista Enlazada Simple`
* **Justificación:** Inserción y eliminación eficientes en la cabecera; adecuado para volúmenes pequeños y medios.

### Reservas por libro

* **Estructura:** `Cola (Queue)`
* **Justificación:** Modelo **FIFO**, útil para atender en orden al primer usuario que realizó la reserva.

### Historial de acciones

* **Estructura:** `Pila (Stack)`
* **Justificación:** Modelo **LIFO** (última operación primero), ideal para auditorías o inspecciones rápidas.

### Préstamos activos

* **Estructura:** `Dict` (id→objeto) + listas derivadas
* **Justificación:** Permite búsqueda directa por ID y facilita filtrar activos.
  *Nota:* Aunque un diccionario no es lineal, aquí se usa como auxiliar; las operaciones clave del proyecto dependen de las estructuras lineales mencionadas.

## Diseño de datos (parametrización)

**Libro**  
`isbn: str`, `titulo: str`, `autor: str`, `anio_publicacion: int`, `ejemplares_totales: int`, `ejemplares_disponibles: int`, `tiene_reservas: bool`

**Usuario**  
`user_id: str`, `nombre: str`, `email: str`

**Préstamo**  
`loan_id: str`, `user_id: str`, `isbn: str`, `fecha_prestamo: date`, `fecha_devolucion_estimada: date`, `fecha_devolucion_real: Optional[date]`, `devuelto: bool`

## Implementación (resumen)

### Estructura del Proyecto

El proyecto se ha organizado en una estructura modular de carpetas para mejorar la mantenibilidad y escalabilidad:

```
estructuras-de-datos/
├── app.py                  # Aplicación principal con menú CLI
├── src/                    # Código fuente
│   ├── estructuras/         # Estructuras de datos
│   │   ├── ds_linear.py     # Estructuras lineales
│   │   └── arboles.py       # Árbol Binario de Búsqueda
│   ├── modelos/            # Modelos de datos
│   │   └── models.py        # Clases de entidades
│   ├── servicios/          # Servicios de negocio
│   │   ├── library_service.py # Servicio de biblioteca
│   │   └── search_service.py # Servicio de búsqueda
│   └── persistencia/       # Manejo de persistencia
│       └── persistencia.py   # Funciones JSON
├── tests/                 # Pruebas unitarias
│   ├── tests_unittest.py    # Pruebas lineales
│   └── tests_arboles.py     # Pruebas árboles
└── data/                  # Archivos de datos
    ├── editoriales.json     # Datos de editoriales
    └── generos.json         # Datos de géneros
```

### Componentes Principales

- `src/estructuras/ds_linear.py`: implementa **ArrayList**, **Lista Enlazada Simple**, **Stack**, **Queue** (lineales).
- `src/modelos/models.py`: dataclasses para **Book**, **User**, **Loan**, **Editorial**, **Genero**.
- `src/servicios/library_service.py`: reglas de negocio; ordena libros por ISBN, usa cola de reservas y pila de historial.
- `src/servicios/search_service.py`: servicio de búsqueda con árboles binarios para editoriales y géneros.
- `app.py`: **menú CLI** con opciones de gestión, préstamos, reservas y búsquedas.
- `tests/tests_unittest.py`: **unittest** de registro/búsqueda de libro, flujo prestar/devolver y reservas automáticas.
- `tests/tests_arboles.py`: **unittest** para verificar el funcionamiento de los árboles binarios de búsqueda.

## Menú del aplicativo (línea de comando)

- Gestión de Libros: registrar, listar, buscar, actualizar, eliminar.
- Gestión de Usuarios: registrar, listar, buscar, eliminar.
- Préstamos/Reservas: prestar, devolver, listar préstamos activos, reservar.
- Ver última acción (pila historial).

## Pruebas y depuración

Se incluyen **3 pruebas** que cubren:

1. Registro y búsqueda de libros.
2. Flujo de préstamo y devolución con actualización de disponibilidad.
3. Reserva automática cuando no hay disponibilidad y asignación al devolver.

## Conclusiones

- La elección de **estructuras lineales** adecuadas simplifica el prototipo y mantiene la **coherencia con los objetivos formativos**.
- Ordenar los libros por ISBN y usar **búsqueda binaria** aporta eficiencia en operaciones frecuentes.
- La **cola** para reservas modela naturalmente la prioridad por orden de llegada.
- La **pila** brinda una forma simple de auditoría.
- La separación por capas facilita futuras mejoras (persistencia, validaciones, reportes).

# Etapa 2: Implementación de Árboles Binarios de Búsqueda

## Introducción

En esta segunda etapa del proyecto, se ha ampliado el sistema de gestión de biblioteca para incluir estructuras de datos no lineales, específicamente árboles binarios de búsqueda. Estas estructuras permiten realizar búsquedas más eficientes que las estructuras lineales implementadas en la primera etapa.

## Nuevas Entidades

Se han agregado dos nuevas entidades al sistema:

1. **Editorial**: con atributos id, nombre, país y año de fundación.
2. **Género**: con atributos id, nombre y descripción.

Estas entidades se utilizan como base para implementar los árboles de búsqueda.

## Estructuras de Datos Implementadas

### Árbol Binario de Búsqueda (ABB)

Se ha implementado un ABB genérico que permite:

- Insertar datos con una clave y un valor.
- Buscar un nodo por clave.
- Recorrer el árbol en orden (inorden).

La implementación es independiente de las clases específicas del dominio, lo que permite su reutilización en diferentes contextos.

## Servicio de Búsqueda

Se ha creado un servicio de búsqueda que utiliza dos árboles binarios:

1. Uno para editoriales, ordenado por nombre.
2. Otro para géneros, también ordenado por nombre.

Este servicio permite:

- Cargar listas de editoriales y géneros en los árboles.
- Buscar una editorial por nombre.
- Buscar un género por nombre.
- Listar todas las editoriales y géneros en orden alfabético.

## Persistencia de Datos

Se ha implementado un sistema de persistencia que permite:

- Guardar listas de objetos en archivos JSON.
- Cargar datos desde JSON y reconstruir objetos según su clase.

Esto facilita la carga inicial de datos y su posterior recuperación.

## Análisis de Eficiencia

### Comparación entre Búsquedas Lineales y Búsquedas con Árboles Binarios

| Operación | Estructura Lineal | Árbol Binario de Búsqueda |
|------------|-------------------|-----------------------------|
| Búsqueda  | O(n)              | O(log n)                     |
| Inserción  | O(1) o O(n)*       | O(log n)                     |
| Recorrido  | O(n)              | O(n)                        |

*Depende de la estructura lineal específica y si requiere mantener un orden.

### Ventajas de los Árboles Binarios de Búsqueda

1. **Eficiencia en búsquedas**: Las búsquedas se ejecutan en tiempo promedio O(log n), lo que representa una mejora significativa respecto a las estructuras lineales (O(n)) cuando el número de elementos es grande.

2. **Ordenamiento implícito**: Los elementos se mantienen ordenados automáticamente, lo que facilita operaciones como listar elementos en orden alfabético.

3. **Balance entre inserción y búsqueda**: Ofrece un buen equilibrio entre la eficiencia de inserción y búsqueda, ambas con complejidad O(log n).

### Caso Práctico

Para una biblioteca con 1,000 editoriales:

- Búsqueda lineal: hasta 1,000 comparaciones en el peor caso.
- Búsqueda en árbol binario: aproximadamente 10 comparaciones (log₂ 1,000 ≈ 10).

Esto representa una mejora de eficiencia de aproximadamente 100 veces para el peor caso.

## Conclusiones

- La implementación de árboles binarios de búsqueda ha mejorado significativamente la eficiencia de las operaciones de búsqueda en el sistema.
- La estructura modular del código permite una fácil extensión para incluir nuevas funcionalidades.
- La persistencia con JSON proporciona una forma sencilla de almacenar y recuperar datos sin depender de bases de datos externas.
- El sistema ahora combina estructuras lineales y no lineales, aprovechando las ventajas de cada una según el caso de uso.

## Referencias (APA)
- Ayala San Martín, G. (2020). Algoritmos y programación: mejores prácticas. Fundación Universidad de las Américas Puebla (UDLAP). (Págs. 106-113).
- Fritelli, V. Guzman, A. & Tymoschuk, J. (2020). Algoritmos y estructuras de datos (2a. ed.). Jorge Sarmiento Editor - Universitas. (Págs. 95- 125, 257-299).
- Ruiz Rodríguez, R. (2009). Fundamentos de la programación orientada a objetos: una aplicación a las estructuras de datos en Java. El Cid Editor.
- Zohonero Martínez, I. & Joyanes Aguilar, L. (2008). Estructuras de datos en Java. McGraw-Hill. España.
