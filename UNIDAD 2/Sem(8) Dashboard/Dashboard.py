import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/Sem(2)ejemplo base/abstraccion/ejemplo abstracción.py',
        '2': 'Unidad 1/Sem(2)ejemplo base/encapsulación/ejemplo encapsulación.py',
        '3': 'Unidad 1/Sem(2)ejemplo base/herencia/ejemplo herencia.py',
        '4': 'Unidad 1/Sem(2)ejemplo base/polimorfismo/ejemplo polimorfismo.py',
        '5': 'Unidad 1/ejemplo base.py',
        '6': 'Unidad 1/Sem(3)Promedio_Clima/promedio_clima_poo.py',
        '7': 'Unidad 1/Sem(3)Promedio_Clima/promedio_clima_tradicional.py',
        '8': 'Unidad 1/Sem(4)Ejemplos del mundo real POO/ALQUILER DE ROPA.py',
        '9': 'Unidad 1/Sem(4)Ejemplos del mundo real POO/PANADERIA.py',
        '10': 'Unidad 2/Sem(5)Tipos de datos, Identificadores/calculos.py',
        '11': 'Unidad 2/Sem(5)Tipos de datos, Identificadores/calculos 2.py',
        '12': 'Unidad 2/Sem(6)Aplicación de Conceptos de POO en Python/tarea s6 Aplicación de Conceptos de POO en Python.py',
        '13': 'Unidad 2/Sem(7)Constructores y Destructoress/uso de constructores (__init__) y destructores (__del__)..py',
        '14': 'Unidad 2/Sem(8) Dashboard/Dashboard.py',

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n.........Menu Principal - Dashboard......")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()