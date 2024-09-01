
import json


def cargar_inventario(archivo):
    """
    Carga el inventario desde un archivo JSON.

    :param archivo: Ruta del archivo JSON.
    :return: Diccionario con los datos del inventario.
    """
    try:
        with open(archivo, 'r') as f:
            inventario = json.load(f)
        return inventario
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None
    except json.JSONDecodeError:
        print("Error al leer el archivo.")
        return None


def imprimir_productos(inventario):
    """
    Imprime los productos del inventario.

    :param inventario: Diccionario con los datos del inventario.
    """
    if inventario and "productos" in inventario:
        for producto in inventario["productos"]:
            print(f"ID: {producto['id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: {producto['precio']:.2f}")
            print("-" * 20)
    else:
        print("No hay productos para mostrar.")


def main():
    archivo = 'inventario.json'  # Nombre del archivo JSON
    inventario = cargar_inventario(archivo)
    imprimir_productos(inventario)


if __name__ == "__main__":
    main()
