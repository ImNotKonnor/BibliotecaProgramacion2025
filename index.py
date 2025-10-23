import json
from datetime import date, timedelta

class Libro:
    def __init__(self, idlibro, titulo, autor, año_publicacion, editorial, isbn, genero=None, idioma="Español", paginas=None, ubicacion=None, ejemplares=1, estado="Disponible", estadoLibro="Buen estado"):
        self.idlibro = idlibro
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.editorial = editorial
        self.isbn = isbn
        self.genero = genero
        self.idioma = idioma
        self.paginas = paginas
        self.ubicacion = ubicacion
        self.ejemplares = ejemplares
        self.estado = estado # Este estado es para marcar si esta disponible o ocupado
        self.estadoLibro = estadoLibro # Este estado es para marcar si esta en buenas condiciones

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} ({self.año_publicacion}) - {self.autor} | {estado}"
    
    def to_dict(self):
        return self.__dict__
    
class Estudiante:
    def __init__(self, IdEstudiante, Cedula, Nombre, Apellido, Fecha_Nacimiento, Direccion, Telefono, Email):
         self.IdEstudiante = IdEstudiante
         self.Cedula = Cedula
         self.Nombre = Nombre
         self.Apellido = Apellido
         self.Fecha_Nacimiento = Fecha_Nacimiento
         self.Direccion = Direccion
         self.Telefono = Telefono
         self.Email = Email
    def __str__(self):
        return f"{self.Cedula} ({self.Nombre} {self.Apellido}) - {self.Telefono} - {self.Email}"
    def to_dict(self):
        return self.__dict__

class Prestamo:
    def __init__(self, isbn, id_usuario, fecha_prestamo=None, fecha_devolucion=None):
        self.isbn = isbn
        self.id_usuario = id_estudiante
        self.fecha_prestamo = fecha_prestamo or str(date.today())
        self.fecha_devolucion = fecha_devolucion or str(date.today() + timedelta(days=7))

    def to_dict(self):
        return self.__dict__


def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


#Archivos usados para guardar datos
libros = [Libro(**l) for l in cargar_datos("libros.json")]
estudiantes = [Estudiante(**u) for u in cargar_datos("estudiantes.json")]
prestamos = [Prestamo(**p) for p in cargar_datos("prestamos.json")]
retirados = [Retirados(**p) for p in cargar_datos("librosretirados.json")]


#Funcion para registrar libros
def registrar_libro():
    idlibro = input("Ingrese Id del Libro: ")
    titulo = input("Ingrese el Titulo del Libro: ")
    autor = input("Ingrese el Autor del Libro: ")
    año_publicacion = input("Ingrese el año de publicacion: ")
    editorial = input("Ingrese la editorial del ejemplar: ")
    isbn = input("Ingrese el ISBN del libro: ")
    genero = input("Ingrese el genero del libro: ")
    paginas = input("¿Cuantas paginas tiene el libro?: ")
    ubicacion = input("¿En que lugar de la biblioteca esta almacenado?: ")
    ejemplares = input("¿Cuantos ejemplares hay disponibles?: ")


    if any(l.isbn == isbn for l in libros):
        print("❌ Ya existe un libro con ese ISBN.")
        return
    if any(l.idlibro == idlibro for l in libros):
        print("❌ Ya existe un libro con ese ID.")
        return


    libro = Libro(idlibro, titulo, autor, año_publicacion, editorial, isbn, genero, paginas, ubicacion, ejemplares) #Arreglar los datos se estan guardando al revez
    libros.append(libro)
    guardar_datos("libros.json", [l.to_dict() for l in libros])
    print("📘 Libro registrado con éxito.")

#Funcion para registrar estudiantes
def registrar_estudiante():
    IdEstudiante = input("Ingrese un identificador o ID: ")
    Cedula = input("Ingrese la cedula del estudiante: ")
    Nombre = input("Ingrese nombre del estudiante: ")
    Apellido = input("Ingrese apellido del estudiante: ")
    Fecha_Nacimiento = input("Ingrese fecha de nacimiento del estudiante: ")
    Direccion = input("Ingrese direccion del estudiante: ")
    Telefono = input("Ingrese telefono o celular del estudiante: ")
    Email = input("Ingrese Email del estudiante: ")

    if any(l.Cedula == Cedula for l in estudiantes):
        print("❌ Ya existe un estudiante con esa cedula.")
        return
    if any(l.IdEstudiante == IdEstudiante for l in estudiantes):
        print("❌ Ya existe un estudiante con ese ID.")
        return
    
    estudiante = Estudiante(IdEstudiante, Cedula, Nombre, Apellido, Fecha_Nacimiento, Direccion, Telefono, Email)
    estudiantes.append(estudiante)
    guardar_datos("estudiantes.json", [l.to_dict() for l in estudiantes])
    print("✅ Estudiante registrado con exito.")

def listar_libros():
    if not libros:
        print("📚 No hay libros registrados.")
        return
    print("\n--- LISTA DE LIBROS ---")
    for i, libro in enumerate(libros, start=1):
        print(f"{i}. {libro}")

def listar_estudiantes():
    if not estudiantes:
        print("👥 No hay estudiantes registrados.")
        return
    print("\n--- LISTA DE ESTUDIANTES ---")
    for i, estudiante in enumerate(estudiantes, start=1):
        print(f"{i}. {estudiante}")


#Funcion Menu para seleccionar las diferentes funciones del programa
def menu():
    while True:
        print("\n=====  MENÚ DE BIBLIOTECA  =====")
        print("1. Registrar libro")
        print("2. Registrar estudiante")
        print("3. Listar libros")
        print("4. Listar estudiantes")
        print("5. Realizar préstamo")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            registrar_estudiante()
        elif opcion == "3":
            listar_libros()
        elif opcion == "4":
            listar_estudiantes()
        elif opcion == "5":
            realizar_prestamo()
        elif opcion == "6":
            devolver_libro()
        elif opcion == "7":
            buscar_libro()
        elif opcion == "8":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")


# Ejecutar programa
if __name__ == "__main__":
    menu()
