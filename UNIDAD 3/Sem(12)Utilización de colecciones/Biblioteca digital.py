# Clase que representa un Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        """
        Inicializa un libro con los detalles proporcionados.
        La tupla (titulo, autor) se usa para atributos inmutables.
        """
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn  # Identificador único para cada libro

    def __str__(self):
        """
        Retorna una representación legible del libro.
        """
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"


# Clase que representa a un Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        """
        Inicializa un usuario con un nombre y un ID único.
        Los libros prestados se almacenan en una lista.
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar libros prestados

    def prestar_libro(self, libro):
        """
        Añade un libro a la lista de libros prestados del usuario.
        """
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        """
        Elimina un libro de la lista de libros prestados según su ISBN.
        """
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def listar_libros_prestados(self):
        """
        Muestra todos los libros que el usuario tiene actualmente prestados.
        """
        if self.libros_prestados:
            for libro in self.libros_prestados:
                print(libro)
        else:
            print(f"{self.nombre} no tiene libros prestados.")

    def __str__(self):
        """
        Retorna una representación legible del usuario.
        """
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


# Clase que representa a la Biblioteca
class Biblioteca:
    def __init__(self):
        """
        Inicializa la biblioteca con diccionario de libros disponibles,
        un conjunto de usuarios registrados y un historial de préstamos.
        """
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y el objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto para almacenar IDs de usuarios únicos
        self.historial_prestamos = {}  # Diccionario para almacenar libros prestados por usuario

    def agregar_libro(self, libro):
        """
        Añade un libro al catálogo de la biblioteca.
        Si el libro ya existe (por ISBN), se ignora.
        """
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro {libro.titulo} añadido a la biblioteca.")
        else:
            print("Este libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        """
        Elimina un libro del catálogo de la biblioteca usando su ISBN.
        """
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no está en la biblioteca.")

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca.
        Si el ID del usuario ya está registrado, no se duplica.
        """
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.historial_prestamos[usuario.id_usuario] = []  # Inicializa historial de préstamos para este usuario
            print(f"Usuario {usuario.nombre} registrado con éxito.")
        else:
            print("El ID del usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        """
        Elimina un usuario registrado de la biblioteca.
        """
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.historial_prestamos[id_usuario]  # Elimina también su historial de préstamos
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        """
        Presta un libro disponible a un usuario registrado.
        Actualiza el catálogo de libros disponibles y el historial del usuario.
        """
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)  # Remueve el libro del catálogo de libros disponibles
            self.historial_prestamos[id_usuario].append(libro)  # Añade el libro al historial de préstamos del usuario
            print(f"Libro {libro.titulo} prestado al usuario {id_usuario}.")
        else:
            print("No se puede prestar el libro, verifique si el usuario o el libro están disponibles.")

    def devolver_libro(self, id_usuario, isbn):
        """
        Permite a un usuario devolver un libro que tiene prestado.
        El libro se devuelve al catálogo de libros disponibles.
        """
        if id_usuario in self.usuarios_registrados:
            libros_prestados = self.historial_prestamos[id_usuario]
            # Busca el libro por ISBN entre los libros prestados
            libro = next((lib for lib in libros_prestados if lib.isbn == isbn), None)
            if libro:
                libros_prestados.remove(libro)  # Remueve el libro de la lista de préstamos
                self.libros_disponibles[isbn] = libro  # Añade el libro de vuelta al catálogo de la biblioteca
                print(f"Libro {libro.titulo} devuelto a la biblioteca.")
            else:
                print("Este usuario no tiene prestado este libro.")
        else:
            print("El usuario no está registrado.")

    def buscar_libro(self, **kwargs):
        """
        Busca libros en el catálogo de la biblioteca según los criterios proporcionados.
        Los criterios pueden ser título, autor o categoría.
        """
        resultados = []
        for libro in self.libros_disponibles.values():
            # Revisa que todos los criterios coincidan con los atributos del libro
            if all(getattr(libro, k) == v for k, v in kwargs.items()):
                resultados.append(libro)

        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con los criterios de búsqueda.")


# Ejemplo de uso del sistema:

# Crear instancias de libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "978-3-16-148410-0")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "978-0-14-118499-9")

# Crear instancias de usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana Gómez", "456")

# Crear la biblioteca
biblioteca = Biblioteca()

# Añadir libros al catálogo
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar un libro a un usuario
biblioteca.prestar_libro("001", "978-3-16-148410-0")

# Listar los libros prestados de un usuario
usuario1.listar_libros_prestados()

# Devolver un libro a la biblioteca
biblioteca.devolver_libro("001", "978-3-16-148410-0")
