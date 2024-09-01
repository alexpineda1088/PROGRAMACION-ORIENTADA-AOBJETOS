# Clase para representar un producto en el inventario
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible del producto
        self.precio = precio  # Precio unitario del producto

    def __str__(self):
        # Método para representar el objeto Producto como una cadena
        return f'{self.id} {self.nombre} {self.cantidad} {self.precio}'

# Clase para gestionar el inventario de productos
class Inventario:
    def __init__(self):
        self.productos = []  # Lista para almacenar los productos
        self.cargar_inventario()  # Carga los productos desde el archivo al inicializar

    def cargar_inventario(self):
        # Carga los productos desde el archivo 'Inventario.txt'
        with open('Inventario.txt', 'r') as file:
            for line in file:
                id, nombre, cantidad, precio = line.strip().split(',')
                # Crea un objeto Producto para cada línea y lo añade a la lista de productos
                self.productos.append(Producto(id, nombre, cantidad, float(precio)))

    def guardar_inventario(self):
        # Guarda los productos actuales en el archivo 'Inventario.txt'
        with open('Inventario.txt', 'w') as file:
            for producto in self.productos:
                file.write(f'{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n')

    def agregar_producto(self, producto):
        # Añade un nuevo producto al inventario y guarda los cambios en el archivo
        self.productos.append(producto)
        self.guardar_inventario()
        print('Producto agregado exitosamente')

    def eliminar_producto(self, id):
        # Elimina un producto del inventario por su ID y guarda los cambios en el archivo
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Se eliminó un producto")

    def actualizar_precio(self, id, precio):
        # Actualiza el precio de un producto por su ID y guarda los cambios en el archivo
        for producto in self.productos:
            if producto.id == id:
                producto.precio = precio
                self.guardar_inventario()
                print('Producto actualizado exitosamente')

    def buscar_producto_nombre(self, nombre):
        # Busca un producto por su nombre y lo retorna
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario
        for producto in self.productos:
            print(producto)

# Inicializa el inventario
mi_inventario = Inventario()

def Menu():
    # Función que muestra el menú y gestiona las opciones del usuario
    while True:
        print('Menu')
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar Precio")
        print("4. Buscar producto por nombre")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            # Opción para agregar un nuevo producto
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))

            mi_inventario.agregar_producto(Producto(id, nombre, cantidad, precio))

        elif opcion == 2:
            # Opción para eliminar un producto por su ID
            id = input("Ingrese el ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id)

        elif opcion == 3:
            # Opción para actualizar el precio de un producto por su ID
            id = input("Ingrese el ID del producto a actualizar: ")
            precio = float(input("Ingrese nuevo precio del producto: "))
            mi_inventario.actualizar_precio(id, precio)

        elif opcion == 4:
            # Opción para buscar un producto por su nombre
            nombre = input("Ingrese el nombre del producto: ")
            producto = mi_inventario.buscar_producto_nombre(nombre)
            if producto:
                print(f'Producto encontrado: ID={producto.id}, Nombre={producto.nombre}, Cantidad={producto.cantidad}, Precio={producto.precio}')
            else:
                print("Producto no encontrado")

        elif opcion == 5:
            # Opción para mostrar todos los productos en el inventario
            mi_inventario.mostrar_inventario()

        elif opcion == 6:
            # Opción para salir del menú
            print("Saliendo del menú...")
            break

if __name__ == '__main__':
    # Llama a la función Menu para iniciar el programa
    Menu()

def crear_archivo_inventario():
    # Función para crear un archivo 'inventario.txt' con datos de productos predefinidos
    datos = [
        "001,Manzana,50,0.60",
        "002,Banana,100,0.40",
        "003,Leche,30,1.20",
        "004,Pan,20,1.00",
        "005,Arroz,10,2.50"
    ]

    with open('inventario.txt', 'w') as f:
        for linea in datos:
            f.write(linea + '\n')

# Crea el archivo de inventario con datos de ejemplo
crear_archivo_inventario()
