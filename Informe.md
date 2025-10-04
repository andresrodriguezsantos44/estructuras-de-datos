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

- `ds_linear.py`: implementa **ArrayList**, **Lista Enlazada Simple**, **Stack**, **Queue** (lineales).
- `models.py`: dataclasses para **Book**, **User**, **Loan**.
- `library_service.py`: reglas de negocio; ordena libros por ISBN, usa cola de reservas y pila de historial.
- `app.py`: **menú CLI** con opciones de gestión, préstamos y reservas.
- `tests_unittest.py`: **unittest** de registro/búsqueda de libro, flujo prestar/devolver y reservas automáticas.

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

## Referencias (APA)
- Ayala San Martín, G. (2020). Algoritmos y programación: mejores prácticas. Fundación Universidad de las Américas Puebla (UDLAP). (Págs. 106-113).
- Fritelli, V. Guzman, A. & Tymoschuk, J. (2020). Algoritmos y estructuras de datos (2a. ed.). Jorge Sarmiento Editor - Universitas. (Págs. 95- 125, 257-299).
- Ruiz Rodríguez, R. (2009). Fundamentos de la programación orientada a objetos: una aplicación a las estructuras de datos en Java. El Cid Editor.
- Zohonero Martínez, I. & Joyanes Aguilar, L. (2008). Estructuras de datos en Java. McGraw-Hill. España.
