
from typing import Optional
from models import Book, User, Editorial, Genero
from library_service import LibraryService
from search_service import SearchService
from persistencia import cargar_desde_json

def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ingrese un número válido.")

def menu_libros(svc: LibraryService):
    while True:
        print("\n--- Gestión de Libros ---")
        print("1. Registrar libro")
        print("2. Listar libros")
        print("3. Buscar libro por ISBN")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("0. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            isbn = input("ISBN: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            anio = input_int("Año de publicación: ")
            tot = input_int("Ejemplares totales: ")
            disp = input_int("Ejemplares disponibles: ")
            svc.agregar_libro(Book(isbn, titulo, autor, anio, tot, disp))
            print("Libro registrado.")
        elif op == "2":
            libros = svc.listar_libros()
            if not libros:
                print("No hay libros registrados.")
            for b in libros:
                print(f"{b.isbn} | {b.titulo} | {b.autor} | {b.anio_publicacion} | Tot:{b.ejemplares_totales} Disp:{b.ejemplares_disponibles} Reservas:{'Sí' if b.tiene_reservas else 'No'}")
        elif op == "3":
            isbn = input("ISBN a buscar: ").strip()
            b = svc.obtener_libro(isbn)
            if b:
                print(f"Encontrado: {b.isbn} - {b.titulo} ({b.autor}, {b.anio_publicacion}) Disp:{b.ejemplares_disponibles}")
            else:
                print("No encontrado.")
        elif op == "4":
            isbn = input("ISBN del libro a actualizar: ").strip()
            print("Deje en blanco si no desea cambiar un campo.")
            nuevo_titulo = input("Nuevo título: ").strip()
            nuevo_autor = input("Nuevo autor: ").strip()
            anio_str = input("Nuevo año de publicación: ").strip()
            tot_str = input("Nuevos ejemplares totales: ").strip()
            disp_str = input("Nuevos ejemplares disponibles: ").strip()
            cambios = {}
            if nuevo_titulo: cambios["titulo"] = nuevo_titulo
            if nuevo_autor: cambios["autor"] = nuevo_autor
            if anio_str: cambios["anio_publicacion"] = int(anio_str)
            if tot_str: cambios["ejemplares_totales"] = int(tot_str)
            if disp_str: cambios["ejemplares_disponibles"] = int(disp_str)
            ok = svc.actualizar_libro(isbn, **cambios)
            print("Actualizado." if ok else "No se pudo actualizar (ISBN no encontrado).")
        elif op == "5":
            isbn = input("ISBN a eliminar: ").strip()
            ok = svc.eliminar_libro(isbn)
            print("Eliminado." if ok else "No se pudo eliminar (ISBN no encontrado).")
        elif op == "0":
            return
        else:
            print("Opción inválida.")

def menu_usuarios(svc: LibraryService):
    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario por ID")
        print("4. Eliminar usuario")
        print("0. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            uid = input("ID de usuario: ").strip()
            nombre = input("Nombre completo: ").strip()
            email = input("Email: ").strip()
            svc.registrar_usuario(User(uid, nombre, email))
            print("Usuario registrado.")
        elif op == "2":
            usuarios = svc.listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            for u in usuarios:
                print(f"{u.user_id} | {u.nombre} | {u.email}")
        elif op == "3":
            uid = input("ID a buscar: ").strip()
            u = svc.obtener_usuario(uid)
            if u:
                print(f"Encontrado: {u.user_id} - {u.nombre} ({u.email})")
            else:
                print("No encontrado.")
        elif op == "4":
            uid = input("ID a eliminar: ").strip()
            ok = svc.eliminar_usuario(uid)
            print("Eliminado." if ok else "No se pudo eliminar (ID no encontrado).")
        elif op == "0":
            return
        else:
            print("Opción inválida.")

def menu_prestamos(svc: LibraryService):
    while True:
        print("\n--- Préstamos ---")
        print("1. Prestar libro")
        print("2. Devolver libro")
        print("3. Listar préstamos activos")
        print("4. Reservar libro")
        print("0. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            isbn = input("ISBN: ").strip()
            uid = input("ID usuario: ").strip()
            dias = 7
            try:
                dias = int(input("Días (por defecto 7): ") or "7")
            except ValueError:
                dias = 7
            loan_id = svc.prestar_libro(isbn, uid, dias)
            if loan_id:
                print(f"Préstamo exitoso. ID: {loan_id}")
            else:
                print("No hay disponibilidad. Usuario en cola de reservas (si libro existe).")
        elif op == "2":
            lid = input("ID de préstamo: ").strip()
            ok = svc.devolver_libro(lid)
            print("Devolución registrada." if ok else "No se pudo devolver (ID no válido o ya devuelto).")
        elif op == "3":
            activos = svc.listar_prestamos_activos()
            if not activos:
                print("No hay préstamos activos.")
            for p in activos:
                print(f"{p.loan_id} | {p.user_id} | {p.isbn} | vence {p.fecha_devolucion_estimada}")
        elif op == "4":
            isbn = input("ISBN: ").strip()
            uid = input("ID usuario: ").strip()
            ok = svc.reservar_libro(isbn, uid)
            print("Reserva creada." if ok else "No se pudo reservar (ISBN o usuario no válido).")
        elif op == "0":
            return
        else:
            print("Opción inválida.")

def ejecutar_busquedas():
    """Función para manejar las búsquedas usando árboles."""
    # Crear instancia del servicio de búsqueda
    search_svc = SearchService()
    
    # Cargar datos desde archivos JSON
    editoriales = cargar_desde_json("editoriales.json", Editorial)
    generos = cargar_desde_json("generos.json", Genero)
    
    # Cargar datos en los árboles
    search_svc.cargar_editoriales(editoriales)
    search_svc.cargar_generos(generos)
    
    while True:
        print("\n--- Búsquedas y Gestión (Árboles) ---")
        print("1. Buscar editorial")
        print("2. Buscar género")
        print("3. Listar editoriales")
        print("4. Listar géneros")
        print("5. Insertar editorial")
        print("6. Insertar género")
        print("7. Actualizar editorial")
        print("8. Actualizar género")
        print("0. Volver al menú principal")
        op = input("Opción: ").strip()
        
        if op == "1":
            nombre = input("Nombre de la editorial a buscar: ").strip()
            editorial = search_svc.buscar_editorial(nombre)
            if editorial:
                print(f"Editorial encontrada: {editorial.id} | {editorial.nombre} | {editorial.pais} | Fundada en {editorial.anio_fundacion}")
            else:
                print("Editorial no encontrada.")
                
        elif op == "2":
            nombre = input("Nombre del género a buscar: ").strip()
            genero = search_svc.buscar_genero(nombre)
            if genero:
                print(f"Género encontrado: {genero.id} | {genero.nombre}")
                print(f"Descripción: {genero.descripcion}")
            else:
                print("Género no encontrado.")
                
        elif op == "3":
            editoriales = search_svc.listar_editoriales()
            if not editoriales:
                print("No hay editoriales registradas.")
            else:
                print("\nEditoriales en orden alfabético:")
                for e in editoriales:
                    print(f"{e.id} | {e.nombre} | {e.pais} | Fundada en {e.anio_fundacion}")
                    
        elif op == "4":
            generos = search_svc.listar_generos()
            if not generos:
                print("No hay géneros registrados.")
            else:
                print("\nGéneros en orden alfabético:")
                for g in generos:
                    print(f"{g.id} | {g.nombre} | {g.descripcion}")
        
        elif op == "5":
            print("\n--- Insertar Nueva Editorial ---")
            id_editorial = input("ID de la editorial: ").strip()
            nombre = input("Nombre: ").strip()
            pais = input("País: ").strip()
            try:
                anio = int(input("Año de fundación: ").strip())
            except ValueError:
                print("Error: El año debe ser un número entero.")
                continue
                
            editorial = Editorial(id=id_editorial, nombre=nombre, pais=pais, anio_fundacion=anio)
            if search_svc.insertar_editorial(editorial):
                print("Editorial insertada correctamente.")
            else:
                print("Error: Ya existe una editorial con ese nombre.")
        
        elif op == "6":
            print("\n--- Insertar Nuevo Género ---")
            id_genero = input("ID del género: ").strip()
            nombre = input("Nombre: ").strip()
            descripcion = input("Descripción: ").strip()
                
            genero = Genero(id=id_genero, nombre=nombre, descripcion=descripcion)
            if search_svc.insertar_genero(genero):
                print("Género insertado correctamente.")
            else:
                print("Error: Ya existe un género con ese nombre.")
        
        elif op == "7":
            print("\n--- Actualizar Editorial ---")
            nombre_original = input("Nombre de la editorial a actualizar: ").strip()
            editorial = search_svc.buscar_editorial(nombre_original)
            
            if not editorial:
                print("Editorial no encontrada.")
                continue
                
            print(f"Editorial actual: {editorial.id} | {editorial.nombre} | {editorial.pais} | Fundada en {editorial.anio_fundacion}")
            print("Deje en blanco los campos que no desea modificar.")
            
            nuevo_id = input(f"Nuevo ID [{editorial.id}]: ").strip()
            nuevo_nombre = input(f"Nuevo nombre [{editorial.nombre}]: ").strip()
            nuevo_pais = input(f"Nuevo país [{editorial.pais}]: ").strip()
            nuevo_anio_str = input(f"Nuevo año de fundación [{editorial.anio_fundacion}]: ").strip()
            
            datos_actualizados = {}
            if nuevo_id: datos_actualizados["id"] = nuevo_id
            if nuevo_nombre: datos_actualizados["nombre"] = nuevo_nombre
            if nuevo_pais: datos_actualizados["pais"] = nuevo_pais
            if nuevo_anio_str:
                try:
                    datos_actualizados["anio_fundacion"] = int(nuevo_anio_str)
                except ValueError:
                    print("Error: El año debe ser un número entero.")
                    continue
            
            if search_svc.actualizar_editorial(nombre_original, datos_actualizados):
                print("Editorial actualizada correctamente.")
            else:
                print("Error al actualizar la editorial.")
        
        elif op == "8":
            print("\n--- Actualizar Género ---")
            nombre_original = input("Nombre del género a actualizar: ").strip()
            genero = search_svc.buscar_genero(nombre_original)
            
            if not genero:
                print("Género no encontrado.")
                continue
                
            print(f"Género actual: {genero.id} | {genero.nombre}")
            print(f"Descripción: {genero.descripcion}")
            print("Deje en blanco los campos que no desea modificar.")
            
            nuevo_id = input(f"Nuevo ID [{genero.id}]: ").strip()
            nuevo_nombre = input(f"Nuevo nombre [{genero.nombre}]: ").strip()
            nueva_descripcion = input(f"Nueva descripción [{genero.descripcion}]: ").strip()
            
            datos_actualizados = {}
            if nuevo_id: datos_actualizados["id"] = nuevo_id
            if nuevo_nombre: datos_actualizados["nombre"] = nuevo_nombre
            if nueva_descripcion: datos_actualizados["descripcion"] = nueva_descripcion
            
            if search_svc.actualizar_genero(nombre_original, datos_actualizados):
                print("Género actualizado correctamente.")
            else:
                print("Error al actualizar el género.")
                    
        elif op == "0":
            return
            
        else:
            print("Opción inválida.")

def main():
    svc = LibraryService()
    while True:
        print("\n===== Sistema de Gestión de Biblioteca (Lineal) =====")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Préstamos/Reservas")
        print("4. Editoriales y Géneros (Árboles)")
        print("9. Ver última acción (pila historial)")
        print("0. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_libros(svc)
        elif op == "2":
            menu_usuarios(svc)
        elif op == "3":
            menu_prestamos(svc)
        elif op == "4":
            ejecutar_busquedas()
        elif op == "9":
            top = svc.ver_top_historial()
            print(f"Última acción: {top}" if top else "Historial vacío.")
        elif op == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
