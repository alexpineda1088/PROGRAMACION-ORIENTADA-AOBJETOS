# Alquiler_ropa.py

class Prenda:
    def __init__(self, tipo, talla, id_prenda):

        #Inicializa una nueva prenda con el tipo, talla e ID proporcionados.
       # La prenda se marca como disponible por defecto.

        self.tipo = tipo
        self.talla = talla
        self.id_prenda = id_prenda
        self.disponible = True

    def alquilar(self):

       # Marca la prenda como no disponible si está disponible para ser alquilada.
        #Devuelve True si el alquiler es exitoso, False en caso contrario.

        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def devolver(self):

        # Marca la prenda como disponible.

        self.disponible = True

class Cliente:
    def __init__(self, nombre, id_cliente):

        # Inicializa un nuevo cliente con el nombre e ID proporcionados.

        self.nombre = nombre
        self.id_cliente = id_cliente
        self.prendas_alquiladas = []

    def alquilar_prenda(self, prenda):

        # Intenta alquilar una prenda para el cliente.
        # Si la prenda se alquila con éxito, se agrega a la lista de prendas alquiladas del cliente.

        if prenda.alquilar():
            self.prendas_alquiladas.append(prenda)
            print(f"Prenda '{prenda.tipo}' de talla {prenda.talla} alquilada por {self.nombre}.")
        else:
            print(f"Prenda '{prenda.tipo}' de talla {prenda.talla} no está disponible.")

    def devolver_prenda(self, prenda):

       # Devuelve una prenda alquilada por el cliente.
       # La prenda se elimina de la lista de prendas alquiladas del cliente.

        if prenda in self.prendas_alquiladas:
            prenda.devolver()
            self.prendas_alquiladas.remove(prenda)
            print(f"Prenda '{prenda.tipo}' de talla {prenda.talla} devuelta por {self.nombre}.")
        else:
            print(f"Prenda '{prenda.tipo}' de talla {prenda.talla} no fue alquilada por {self.nombre}.")

class TiendaAlquiler:
    def __init__(self):

        # Inicializa una nueva tienda de alquiler con listas vacías de prendas y clientes.

        self.prendas = []
        self.clientes = []

    def agregar_prenda(self, prenda):

        # Agrega una prenda a la lista de prendas de la tienda.

        self.prendas.append(prenda)

    def registrar_cliente(self, cliente):

       # Registra un nuevo cliente en la tienda.

        self.clientes.append(cliente)

    def mostrar_prendas_disponibles(self):

       # Muestra una lista de prendas disponibles en la tienda.

        print("Prendas disponibles:")
        for prenda in self.prendas:
            if prenda.disponible:
                print(f"- {prenda.tipo} (Talla: {prenda.talla}, ID: {prenda.id_prenda})")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una tienda de alquiler
    tienda = TiendaAlquiler()

    # Crear algunas prendas
    prenda1 = Prenda("Vestido", "M", "001")
    prenda2 = Prenda("Traje", "L", "002")

    # Agregar prendas a la tienda
    tienda.agregar_prenda(prenda1)
    tienda.agregar_prenda(prenda2)

    # Crear un cliente
    cliente = Cliente("Ana Suarez", "1001")
    cliente2 = Cliente("Jaime Ochoa", "1002")
    # Registrar el cliente en la tienda
    tienda.registrar_cliente(cliente)
    tienda.registrar_cliente(cliente2)
    # Mostrar prendas disponibles
    tienda.mostrar_prendas_disponibles()

    # Alquilar una prenda
    cliente.alquilar_prenda(prenda1)
    cliente2.alquilar_prenda(prenda2)
    # Mostrar prendas disponibles nuevamente
    tienda.mostrar_prendas_disponibles()

    # Devolver la prenda
    cliente.devolver_prenda(prenda1)

    # Mostrar prendas disponibles nuevamente
    tienda.mostrar_prendas_disponibles()
