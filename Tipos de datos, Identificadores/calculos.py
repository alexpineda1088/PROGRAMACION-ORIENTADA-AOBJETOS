
#Este programa calcula el área de un círculo y un rectángulo, y convierte una temperatura de Celsius a Fahrenheit.


import math


def calcular_area_circulo(radio: float) -> float:

    #Calcula el área de un círculo dado su radio.

    #:return: El área del círculo.

    return math.pi * (radio ** 2)


def calcular_area_rectangulo(longitud: float, ancho: float) -> float:
    #Calcula el área de un rectángulo dadas su longitud y ancho.

    #param longitud: La longitud del rectángulo.
    #param ancho: El ancho del rectángulo.
    #return: El área del rectángulo.

    return longitud * ancho


def convertir_celsius_a_fahrenheit(celsius: float) -> float:

   # Convierte una temperatura de Celsius a Fahrenheit.

    #param celsius: La temperatura en grados Celsius.
    #return: La temperatura en grados Fahrenheit.

    return (celsius * 9 / 5) + 32


def main():
    # Cálculo del área de un círculo
    radio = 5.6  # float
    area_circulo = calcular_area_circulo(radio)
    print(f"El área del círculo con radio {radio} es {area_circulo:.2f}")

    # Cálculo del área de un rectángulo
    longitud = 10  # integer
    ancho = 7.3 # float
    area_rectangulo = calcular_area_rectangulo(longitud, ancho)
    print(f"El área del rectángulo con longitud {longitud} y ancho {ancho} es {area_rectangulo:.2f}")

    # Conversión de Celsius a Fahrenheit
    celsius = 25.0  # float
    fahrenheit = convertir_celsius_a_fahrenheit(celsius)
    print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit")


if __name__ == "__main__":
    main()
