class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        """
        Inicializa un nuevo producto con ID, nombre, cantidad y precio.

        :param producto_id: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad del producto en inventario.
        :param precio: Precio del producto.
        """
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        """Devuelve el ID del producto."""
        return self.producto_id

    def obtener_nombre(self):
        """Devuelve el nombre del producto."""
        return self.nombre

    def obtener_cantidad(self):
        """Devuelve la cantidad del producto en inventario."""
        return self.cantidad

    def obtener_precio(self):
        """Devuelve el precio del producto."""
        return self.precio

    def establecer_cantidad(self, cantidad):
        """
        Establece la cantidad del producto en inventario.

        :param cantidad: Nueva cantidad del producto.
        """
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        """
        Establece el precio del producto.

        :param precio: Nuevo precio del producto.
        """
        self.precio = precio

    def __str__(self):
        """
        Devuelve una representación en cadena del producto.

        :return: Cadena con la información del producto.
        """
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


import json


class Inventario:
    def __init__(self):
        """
        Inicializa un nuevo inventario vacío.
        """
        self.productos = {}  # Diccionario para almacenar productos con ID como clave

    def añadir_producto(self, producto):
        """
        Añade un producto al inventario.

        :param producto: Instancia de la clase Producto a añadir.
        :raises ValueError: Si el producto ya existe en el inventario.
        """
        if producto.obtener_id() not in self.productos:
            self.productos[producto.obtener_id()] = producto
        else:
            raise ValueError("El producto ya existe en el inventario.")

    def eliminar_producto(self, producto_id):
        """
        Elimina un producto del inventario por su ID.

        :param producto_id: ID del producto a eliminar.
        :raises KeyError: Si el producto no existe en el inventario.
        """
        if producto_id in self.productos:
            del self.productos[producto_id]
        else:
            raise KeyError("El producto no existe en el inventario.")

    def actualizar_cantidad(self, producto_id, cantidad):
        """
        Actualiza la cantidad de un producto en el inventario.

        :param producto_id: ID del producto a actualizar.
        :param cantidad: Nueva cantidad del producto.
        :raises KeyError: Si el producto no existe en el inventario.
        """
        if producto_id in self.productos:
            self.productos[producto_id].establecer_cantidad(cantidad)
        else:
            raise KeyError("El producto no existe en el inventario.")

    def actualizar_precio(self, producto_id, precio):
        """
        Actualiza el precio de un producto en el inventario.

        :param producto_id: ID del producto a actualizar.
        :param precio: Nuevo precio del producto.
        :raises KeyError: Si el producto no existe en el inventario.
        """
        if producto_id in self.productos:
            self.productos[producto_id].establecer_precio(precio)
        else:
            raise KeyError("El producto no existe en el inventario.")

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca productos por nombre.

        :param nombre: Nombre del producto a buscar.
        :return: Lista de productos que coinciden con el nombre.
        """
        resultados = [producto for producto in self.productos.values() if
                      nombre.lower() in producto.obtener_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        """
        Guarda el inventario en un archivo JSON.

        :param archivo: Ruta del archivo donde se guardará el inventario.
        """
        with open(archivo, 'w') as f:
            productos_serializados = {k: vars(v) for k, v in self.productos.items()}
            json.dump(productos_serializados, f, indent=4)

    def cargar_inventario(self, archivo):
        """
        Carga el inventario desde un archivo JSON.

        :param archivo: Ruta del archivo desde donde se cargará el inventario.
        """
        try:
            with open(archivo, 'r') as f:
                productos_serializados = json.load(f)
                self.productos = {k: Producto(**v) for k, v in productos_serializados.items()}
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except json.JSONDecodeError:
            print("Error al leer el archivo.")


def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\n1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad")
    print("4. Actualizar precio")
    print("5. Buscar producto")
    print("6. Mostrar todos los productos")
    print("7. Guardar inventario")
    print("8. Cargar inventario")
    print("9. Salir")


def main():
    """
    Función principal para ejecutar el programa de gestión de inventario.
    """
    inventario = Inventario()  # Crear una instancia del inventario

    while True:
        mostrar_menu()  # Mostrar las opciones del menú
        eleccion = input("Elija una opción: ")

        if eleccion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            try:
                inventario.añadir_producto(producto)
                print("Producto añadido.")
            except ValueError as e:
                print(e)

        elif eleccion == "2":
            id = input("ID del producto a eliminar: ")
            try:
                inventario.eliminar_producto(id)
                print("Producto eliminado.")
            except KeyError as e:
                print(e)

        elif eleccion == "3":
            id = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            try:
                inventario.actualizar_cantidad(id, cantidad)
                print("Cantidad actualizada.")
            except KeyError as e:
                print(e)

        elif eleccion == "4":
            id = input("ID del producto: ")
            precio = float(input("Nuevo precio: "))
            try:
                inventario.actualizar_precio(id, precio)
                print("Precio actualizado.")
            except KeyError as e:
                print(e)

        elif eleccion == "5":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif eleccion == "6":
            inventario.mostrar_productos()

        elif eleccion == "7":
            archivo = input("Nombre del archivo para guardar: ")
            inventario.guardar_inventario(archivo)
            print("Inventario guardado.")

        elif eleccion == "8":
            archivo = input("Nombre del archivo para cargar: ")
            inventario.cargar_inventario(archivo)
            print("Inventario cargado.")

        elif eleccion == "9":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()

