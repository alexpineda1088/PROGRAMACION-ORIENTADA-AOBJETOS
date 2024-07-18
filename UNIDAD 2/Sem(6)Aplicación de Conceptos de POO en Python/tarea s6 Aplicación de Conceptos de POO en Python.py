# Este código cumple con los requisitos de la tarea al demostrar los conceptos de POO como
# herencia (con Vehiculo y Automovil), encapsulación (con el atributo protegido _encendido) y polimorfismo
# (con el método conducir sobrescrito en Automovil).

# Definición de la clase base Vehiculo

class Vehiculo:
    def __init__(self, marca, modelo):

       # Constructor de la clase Vehiculo.

        #Args:
        #- marca (str): La marca del vehículo.
        #- modelo (str): El modelo del vehículo.

        self.marca = marca
        self.modelo = modelo
        self._encendido = False  # Atributo protegido para indicar si el vehículo está encendido o apagado

    def encender(self):
        #Método para encender el vehículo.
        self._encendido = True
        print(f"{self.marca} {self.modelo} ha sido encendido.")

    def apagar(self):
        #Método para apagar el vehículo.
        self._encendido = False
        print(f"{self.marca} {self.modelo} ha sido apagado.")

    def conducir(self):

       # Método abstracto que debe ser implementado por las clases derivadas.
        #Levanta un error si no se implementa en la clase derivada.

        raise NotImplementedError("Método conducir debe ser implementado en la clase derivada.")

    def __str__(self):

       # Método especial para representar el objeto como una cadena.
        #Retorna una descripción del vehículo incluyendo su estado de encendido/apagado.

        estado = "encendido" if self._encendido else "apagado"
        return f"{self.marca} {self.modelo}, estado: {estado}"


# Definición de la clase derivada Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):

       # Constructor de la clase Automovil.

       #Args:
       # - marca (str): La marca del automóvil.
       #- modelo (str): El modelo del automóvil.
       # - color (str): El color del automóvil.

        super().__init__(marca, modelo)
        self.color = color

    def conducir(self):
        #Implementación del método conducir para Automovil.
        print(f"El {self.marca} {self.modelo} de color {self.color} está en movimiento.")


# Función para probar cualquier objeto de tipo Vehiculo
def probar_vehiculo(vehiculo):

    #Función para probar un vehículo, encendiéndolo, conduciéndolo y apagándolo.

    #Args:
    #- vehiculo (Vehiculo): Objeto de tipo Vehiculo o una de sus subclases.

    vehiculo.encender()
    vehiculo.conducir()
    vehiculo.apagar()


# Programa principal
if __name__ == "__main__":
    # Crear instancias de Automovil
    auto1 = Automovil("Toyota", "Corolla", "Rojo")
    auto2 = Automovil("Honda", "Civic", "Azul")

    # Mostrar información del auto1
    print(auto1)

    # Probar el auto1
    probar_vehiculo(auto1)

    print()

    # Mostrar información del auto2
    print(auto2)

    # Probar el auto2
    probar_vehiculo(auto2)
