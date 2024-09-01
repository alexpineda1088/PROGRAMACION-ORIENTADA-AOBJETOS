class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor para inicializar un objeto Producto con un ID único, nombre, cantidad y precio.
        """
        self._id = id  # ID único del producto
        self._nombre = nombre  # Nombre del producto
        self._cantidad = cantidad  # Cantidad en inventario
        self._precio = precio  # Precio por unidad

    # Getters (Métodos para obtener los valores de los atributos)
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters (Métodos para establecer o actualizar los valores de los atributos)
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        """
        Método especial para retornar una representación en forma de cadena del objeto Producto.
        """
        return f'ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}'
class Inventario:
    def __init__(self):
        """
        Constructor para inicializar el inventario como una lista vacía de productos.
        """
        self._productos = []  # Lista para almacenar los objetos Producto

    def añadir_producto(self, producto):
        """
        Método para añadir un nuevo producto al inventario.
        Verifica que el ID del producto sea único antes de añadirlo.
        """
        if not any(p.get_id() == producto.get_id() for p in self._productos):
            self._productos.append(producto)
        else:
            print("Error: Ya existe un producto con este ID.")

    def eliminar_producto(self, id):
        """
        Método para eliminar un producto del inventario por su ID.
        """
        self._productos = [p for p in self._productos if p.get_id() != id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Método para actualizar la cantidad y/o el precio de un producto dado su ID.
        """
        for producto in self._productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                return
        print("Error: Producto no encontrado.")

    def buscar_productos(self, nombre):
        """
        Método para buscar productos en el inventario por nombre.
        Retorna una lista de productos cuyos nombres contienen la cadena de búsqueda.
        """
        return [p for p in self._productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        """
        Método para mostrar todos los productos en el inventario.
        """
        if not self._productos:
            print("Inventario vacío.")
        else:
            for producto in self._productos:
                print(producto)
#from Producto import Producto
#from Inventario import Inventario

def mostrar_menu():
    """
    Función para mostrar el menú de opciones al usuario.
    """
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    """
    Función principal para manejar la interacción del usuario con el sistema.
    """
    inventario = Inventario()  # Se crea una instancia de la clase Inventario

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Opción para añadir un nuevo producto
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            # Opción para eliminar un producto por ID
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            # Opción para actualizar la cantidad o el precio de un producto por ID
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja en blanco si no deseas cambiarla): ")
            precio = input("Nuevo precio (deja en blanco si no deseas cambiarlo): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)

        elif opcion == '4':
            # Opción para buscar productos por nombre
            nombre = input("Nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_productos(nombre)
            for producto in productos_encontrados:
                print(producto)

        elif opcion == '5':
            # Opción para mostrar todos los productos en el inventario
            inventario.mostrar_productos()

        elif opcion == '6':
            # Opción para salir del sistema
            print("Saliendo...")
            break

        else:
            # Manejo de opción no válida
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
