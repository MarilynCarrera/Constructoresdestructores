class Libro:
    """
    Clase que representa un libro.

    El constructor __init__ se encarga de inicializar los atributos del libro:
    - título
    - autor
    - páginas

    El destructor __del__ se encarga de imprimir un mensaje cuando el objeto Libro
    es eliminado de la memoria.
    """

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        print(f"Se ha creado un nuevo libro: '{self.titulo}' de {self.autor}")

    def __del__(self):
        print(f"El libro '{self.titulo}' ha sido eliminado de la memoria.")


class Biblioteca:
    """
    Clase que representa una biblioteca.

    El constructor __init__ inicializa la lista de libros de la biblioteca.

    El método agregar_libro permite añadir un nuevo libro a la biblioteca.

    El destructor __del__ se encarga de eliminar todos los libros de la biblioteca
    cuando el objeto Biblioteca es eliminado de la memoria.
    """

    def __init__(self):
        self.libros = []
        print("Se ha creado una nueva biblioteca.")

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Se ha agregado el libro '{libro.titulo}' a la biblioteca.")

    def __del__(self):
        for libro in self.libros:
            del libro
        print("La biblioteca y todos sus libros han sido eliminados de la memoria.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
    libro2 = Libro("El Quijote", "Miguel de Cervantes", 1056)
    libro3 = Libro("Orgullo y prejuicio", "Jane Austen", 432)

    # Crear una biblioteca y agregar los libros
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # La biblioteca y sus libros se eliminarán automáticamente al salir del programa