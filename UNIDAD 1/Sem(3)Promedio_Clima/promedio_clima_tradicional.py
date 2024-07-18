# Programación Tradicional para calcular el promedio semanal del clima

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []  # Lista para almacenar las temperaturas diarias
    for i in range(7):  # Bucle para ingresar las temperaturas de los 7 días de la semana
        while True:
            try:
                # Solicita al usuario ingresar la temperatura del día i+1
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)  # Agrega la temperatura a la lista
                break  # Sale del bucle interno si la entrada es válida
            except ValueError:
                # Muestra un mensaje de error si la entrada no es un número válido
                print("Por favor, ingrese un número válido.")
    return temperaturas  # Devuelve la lista de temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    # Calcula el promedio sumando las temperaturas y dividiendo por el número de días
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("Programa para calcular el promedio semanal de temperaturas")
    temperaturas = ingresar_temperaturas()  # Llama a la función para ingresar temperaturas
    promedio = calcular_promedio(temperaturas)  # Calcula el promedio semanal
    # Imprime el promedio semanal de temperaturas con dos decimales
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
