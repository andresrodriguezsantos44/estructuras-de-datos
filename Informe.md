# Sistema de Gestión de Biblioteca (Prototipo con Estructuras de Datos Lineales, No Lineales y Árboles Binarios)

**Portada**  
**Curso:** Estructura de Datos
**Proyecto:** Modelar las interacciones entre los usuarios y los libros [Refinamiento 2]
**Autor:** Andres Alfonso Rodriguez Santos
**Profesor:** William Ruiz
**Universidad:** Corporación Universitaria Iberoamericana
**Carrera:** Ingeniería de Software
**Fecha:** Noviembre 08, 2025

## Introducción

Este documento presenta el análisis, diseño e implementación de un prototipo de sistema de gestión de biblioteca que utiliza **estructuras de datos lineales** —arreglos (listas), listas enlazadas, pilas y colas— para almacenar y administrar libros, usuarios y préstamos. El objetivo es **comunicar los parámetros de los datos a almacenar** y **elegir estructuras congruentes con los requisitos**, cumpliendo los resultados de aprendizaje de la unidad.

## Requerimientos del sistema

### Requerimientos Funcionales

#### 1. Gestión de Libros

| Requerimiento | Proceso | Salida |
|--------------|---------|--------|
| **RF1.1: Registrar libro** | 1. Capturar datos del libro (ISBN, título, autor, año, ejemplares)<br>2. Validar que el ISBN no exista<br>3. Crear instancia de libro<br>4. Almacenar en estructura ArrayList | Confirmación de registro exitoso<br>Libro añadido al catálogo |
| **RF1.2: Listar libros** | 1. Recorrer la colección de libros<br>2. Formatear datos para presentación | Lista de libros con detalles (ISBN, título, autor, disponibilidad) |
| **RF1.3: Buscar libro** | 1. Capturar ISBN a buscar<br>2. Realizar búsqueda binaria en ArrayList<br>3. Recuperar datos del libro | Detalles del libro encontrado o mensaje de "no encontrado" |
| **RF1.4: Actualizar libro** | 1. Buscar libro por ISBN<br>2. Capturar nuevos datos<br>3. Actualizar atributos<br>4. Reordenar si cambia ISBN | Confirmación de actualización exitosa |
| **RF1.5: Eliminar libro** | 1. Buscar libro por ISBN<br>2. Eliminar de la colección<br>3. Eliminar reservas asociadas | Confirmación de eliminación exitosa |

#### 2. Gestión de Usuarios

| Requerimiento | Proceso | Salida |
|--------------|---------|--------|
| **RF2.1: Registrar usuario** | 1. Capturar datos del usuario (ID, nombre, email)<br>2. Validar que el ID no exista<br>3. Crear instancia de usuario<br>4. Insertar al inicio de la lista enlazada | Confirmación de registro exitoso |
| **RF2.2: Listar usuarios** | 1. Recorrer la lista enlazada de usuarios<br>2. Formatear datos para presentación | Lista de usuarios con detalles (ID, nombre, email) |
| **RF2.3: Buscar usuario** | 1. Capturar ID a buscar<br>2. Recorrer la lista enlazada<br>3. Comparar IDs hasta encontrar coincidencia | Detalles del usuario encontrado o mensaje de "no encontrado" |
| **RF2.4: Eliminar usuario** | 1. Buscar usuario por ID<br>2. Eliminar de la lista enlazada | Confirmación de eliminación exitosa |

#### 3. Gestión de Préstamos y Reservas

| Requerimiento | Proceso | Salida |
|--------------|---------|--------|
| **RF3.1: Prestar libro** | 1. Verificar existencia de libro y usuario<br>2. Verificar disponibilidad de ejemplares<br>3. Decrementar contador de disponibles<br>4. Crear registro de préstamo<br>5. Calcular fecha de devolución | ID de préstamo generado o mensaje de "no disponible" |
| **RF3.2: Devolver libro** | 1. Buscar préstamo por ID<br>2. Marcar como devuelto<br>3. Incrementar contador de disponibles<br>4. Verificar cola de reservas<br>5. Asignar automáticamente al siguiente en cola si hay | Confirmación de devolución exitosa |
| **RF3.3: Reservar libro** | 1. Verificar existencia de libro y usuario<br>2. Encolar ID de usuario en la cola de reservas del libro<br>3. Marcar libro como "tiene reservas" | Confirmación de reserva exitosa |
| **RF3.4: Listar préstamos activos** | 1. Filtrar préstamos por estado "no devuelto"<br>2. Formatear datos para presentación | Lista de préstamos activos con detalles (ID, usuario, libro, fecha vencimiento) |

#### 4. Auditoría y Búsquedas

| Requerimiento | Proceso | Salida |
|--------------|---------|--------|
| **RF4.1: Registrar historial** | 1. Crear registro de operación<br>2. Apilar en la estructura de historial | Operación registrada en historial |
| **RF4.2: Consultar última operación** | 1. Verificar si la pila no está vacía<br>2. Obtener elemento superior sin desapilar | Descripción de la última operación realizada |
| **RF4.3: Buscar editorial** | 1. Capturar nombre a buscar<br>2. Realizar búsqueda en árbol binario<br>3. Recuperar datos de la editorial | Detalles de la editorial encontrada o mensaje de "no encontrada" |
| **RF4.4: Buscar género** | 1. Capturar nombre a buscar<br>2. Realizar búsqueda en árbol binario<br>3. Recuperar datos del género | Detalles del género encontrado o mensaje de "no encontrado" |
| **RF4.5: Listar editoriales** | 1. Realizar recorrido inorden del árbol<br>2. Formatear datos para presentación | Lista ordenada alfabéticamente de editoriales |
| **RF4.6: Listar géneros** | 1. Realizar recorrido inorden del árbol<br>2. Formatear datos para presentación | Lista ordenada alfabéticamente de géneros |

### Requerimientos No Funcionales

| Requerimiento | Descripción | Criterio de Aceptación |
|--------------|-------------|------------------------|
| **RNF1: Interfaz de usuario** | Prototipo ejecutable por **línea de comandos (CLI)** con menús intuitivos y navegables | Sistema operable completamente desde terminal con menús claros y respuestas informativas |
| **RNF2: Calidad de código** | Código legible y modular, con **buenas prácticas** (nombres claros, comentarios básicos, separación por capas) | Estructura de proyecto organizada con separación clara de responsabilidades |
| **RNF3: Pruebas** | **Pruebas unitarias** sobre casos críticos del sistema | Al menos 3 casos de prueba documentados y ejecutables |
| **RNF4: Rendimiento** | Operaciones de búsqueda optimizadas mediante estructuras adecuadas | Búsquedas en tiempo O(log n) para operaciones frecuentes |
| **RNF5: Escalabilidad** | Diseño que permita incorporar nuevas funcionalidades sin modificar lo existente | Arquitectura modular con interfaces bien definidas |
| **RNF6: Documentación** | Documentación completa del diseño, estructuras utilizadas y justificación | Archivos README.md, Informe.md y DOCUMENTACION.md detallados |
| **RNF7: Manejo de errores** | Sistema robusto que maneje adecuadamente entradas inválidas | Validación de entradas y mensajes de error informativos |

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

La implementación del sistema se ha realizado siguiendo un enfoque modular y orientado a objetos, con una clara separación de responsabilidades. Los detalles de la estructura del proyecto y la organización de archivos se encuentran en el archivo README.md.

### Enfoque de Implementación

1. **Separación de Capas**: Se ha implementado una arquitectura en capas que separa:
   - Estructuras de datos (ArrayList, LinkedList, Stack, Queue, Árbol Binario)
   - Modelos de dominio (Book, User, Loan, Editorial, Genero)
   - Servicios de negocio (LibraryService, SearchService)
   - Persistencia (funciones para manejo de JSON)
   - Interfaz de usuario (menú CLI)

2. **Principios de Diseño**:
   - Responsabilidad Única: Cada clase tiene una sola responsabilidad
   - Abstracción: Las estructuras de datos están implementadas de forma genérica
   - Encapsulamiento: Los detalles de implementación están ocultos tras interfaces claras

3. **Estrategia de Pruebas**:
   - Pruebas unitarias para las estructuras de datos lineales
   - Pruebas unitarias para las estructuras de árboles binarios
   - Casos de prueba que verifican flujos completos del sistema

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
