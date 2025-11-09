# Sistema de Gestión de Biblioteca

Implementación de un sistema de gestión bibliotecaria utilizando diferentes estructuras de datos en Python.

## Guía Rápida

### Requisitos

- Python 3.9+

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/usuario/estructuras-de-datos.git
cd estructuras-de-datos
```

### Ejecución

```bash
# Ejecutar la aplicación principal
python3 app.py

# Ejecutar pruebas unitarias
python3 -m unittest tests/tests_unittest.py -v  # Pruebas de estructuras lineales
python3 -m unittest tests/tests_arboles.py -v   # Pruebas de árboles binarios
```

## Estructura del Proyecto

```
estructuras-de-datos/
├── app.py                  # Aplicación principal con menú CLI
├── Informe.md              # Análisis técnico y requerimientos
├── DOCUMENTACION.md        # Decisiones de diseño y desafíos
├── README.md               # Este archivo (guía de uso)
├── src/                    # Código fuente
│   ├── estructuras/        # Implementaciones de estructuras de datos
│   ├── modelos/            # Entidades del dominio
│   ├── servicios/          # Lógica de negocio
│   └── persistencia/       # Manejo de datos
├── tests/                  # Pruebas unitarias
└── data/                   # Archivos de datos JSON
```

## Funcionalidades Principales

### Gestión de Biblioteca (Estructuras Lineales)

- **Libros**: Registrar, buscar, actualizar, eliminar y listar
- **Usuarios**: Registrar, buscar, eliminar y listar
- **Préstamos**: Prestar, devolver y listar préstamos activos
- **Reservas**: Gestión automática de reservas cuando no hay disponibilidad

### Búsquedas Avanzadas (Árboles Binarios)

- **Editoriales**: Búsqueda, listado, inserción y actualización
- **Géneros**: Búsqueda, listado, inserción y actualización

## Navegación del Menú

1. **Gestión de Libros** - Administración del catálogo
2. **Gestión de Usuarios** - Registro y búsqueda de usuarios
3. **Préstamos/Reservas** - Control de préstamos y devoluciones
4. **Editoriales y Géneros** - Búsquedas avanzadas con árboles binarios
9. **Ver última acción** - Historial de operaciones (pila)
0. **Salir** - Finalizar programa

## Documentación Adicional

- **Informe.md**: Análisis técnico, requerimientos y estructuras de datos utilizadas
- **DOCUMENTACION.md**: Decisiones de diseño, desafíos enfrentados y soluciones implementadas

## Autor

Andres Alfonso Rodriguez Santos - Ingeniería de Software - Corporación Universitaria Iberoamericana
