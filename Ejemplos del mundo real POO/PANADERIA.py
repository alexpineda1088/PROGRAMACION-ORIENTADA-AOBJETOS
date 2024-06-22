#  LOCAL panaderia.py

class Producto:

    # Inicializa un nuevo producto con el nombre, precio y cantidad disponibles.
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidad_vendida):

      #  Reduce la cantidad disponible del producto en la cantidad vendida.
     # Devuelve True si la venta es exitosa, False en caso contrario.
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            return True
        else:
            return False

    def reponer(self, cantidad_repuesta):

       # Incrementa la cantidad disponible del producto en la cantidad repuesta.

        self.cantidad += cantidad_repuesta

class Panaderia:
    def __init__(self):

       # Inicializa una nueva panadería con una lista vacía de productos.

        self.productos = []

    def agregar_producto(self, producto):

       # Agrega un producto a la lista de productos de la panadería.

        self.productos.append(producto)

    def mostrar_productos(self):

       # Muestra una lista de productos disponibles en la panadería.

        print("Productos disponibles:")
        for producto in self.productos:
            print(f"- {producto.nombre} (Precio: ${producto.precio}, Cantidad: {producto.cantidad})")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una panadería
    panaderia = Panaderia()

    # Crear algunos productos
    producto1 = Producto("Pan Integral", 0.25, 20)
    producto2 = Producto("Croissant", 0.50, 15)

    # Agregar productos a la panadería
    panaderia.agregar_producto(producto1)
    panaderia.agregar_producto(producto2)

    # Mostrar productos disponibles
    panaderia.mostrar_productos()

    # Vender algunos productos
    producto1.vender(5)
    producto2.vender(3)

    # Mostrar productos disponibles nuevamente
    panaderia.mostrar_productos()

    # Reponer algunos productos
    producto1.reponer(10)
    producto2.reponer(5)

    # Mostrar productos disponibles nuevamente
    panaderia.mostrar_productos()
