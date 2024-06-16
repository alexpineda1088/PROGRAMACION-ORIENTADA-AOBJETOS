# Programación Orientada a Objetos para calcular el promedio semanal del clima

class ClimaDiario:
    def __init__(self):
        self.temperaturas = []  # Inicializa una lista para almacenar las temperaturas diarias

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)  # Agrega la temperatura a la lista

    def calcular_promedio(self):
        if len(self.temperaturas) == 0:  # Verifica si la lista de temperaturas está vacía
            return 0  # Si está vacía, devuelve 0
        # Calcula el promedio sumando las temperaturas y dividiendo por el número de días
        return sum(self.temperaturas) / len(self.temperaturas)


class ProgramaClima:
    def __init__(self):
        self.clima_diario = ClimaDiario()  # Crea una instancia de la clase ClimaDiario

    def ejecutar(self):
        print("Programa para calcular el promedio semanal de temperaturas")
        for i in range(7):  # Bucle para ingresar las temperaturas de los 7 días de la semana
            while True:
                try:
                    # Solicita al usuario ingresar la temperatura del día i+1
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    self.clima_diario.ingresar_temperatura(temp)  # Llama al método para agregar la temperatura
                    break  # Sale del bucle interno si la entrada es válida
                except ValueError:
                    # Muestra un mensaje de error si la entrada no es un número válido
                    print("Por favor, ingrese un número válido.")

        promedio = self.clima_diario.calcular_promedio()  # Calcula el promedio semanal
        # Imprime el promedio semanal de temperaturas con dos decimales
        print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")


# Crear instancia de ProgramaClima y ejecutar
if __name__ == "__main__":
    programa = ProgramaClima()  # Crea una instancia de la clase ProgramaClima
    programa.ejecutar()  # Llama al método ejecutar para iniciar el programa
