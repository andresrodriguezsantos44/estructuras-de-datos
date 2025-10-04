
from typing import Optional
from models import Book, User
from library_service import LibraryService

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

def main():
    svc = LibraryService()
    while True:
        print("\n===== Sistema de Gestión de Biblioteca (Lineal) =====")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Préstamos/Reservas")
        print("9. Ver última acción (pila historial)")
        print("0. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_libros(svc)
        elif op == "2":
            menu_usuarios(svc)
        elif op == "3":
            menu_prestamos(svc)
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
