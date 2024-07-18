
#Este programa gestiona información básica de un registro de estudiantes.
#Permite agregar estudiantes, mostrar la lista de estudiantes y buscar un estudiante por nombre.



class Estudiante:
    def __init__(self, nombre: str, edad: int, promedio: float, activo: bool):

        #Inicializa un nuevo estudiante.

       # :param nombre: El nombre del estudiante.
       # :param edad: La edad del estudiante.
        #:param promedio: El promedio del estudiante.
       # :param activo: Estado de actividad del estudiante.

        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
        self.activo = activo

    def __str__(self):

       # Devuelve una representación en cadena del estudiante.

        estado = "Activo" if self.activo else "Inactivo"
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Promedio: {self.promedio}, Estado: {estado}"


def agregar_estudiante(estudiantes: list):

    #Agrega un nuevo estudiante a la lista.

   # :param estudiantes: La lista de estudiantes.

    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    promedio = float(input("Ingrese el promedio del estudiante: "))
    activo = input("¿El estudiante está activo? (s/n): ").lower() == 's'

    nuevo_estudiante = Estudiante(nombre, edad, promedio, activo)
    estudiantes.append(nuevo_estudiante)
    print(f"Estudiante {nombre} agregado exitosamente.")


def mostrar_estudiantes(estudiantes: list):

   # Muestra la lista de estudiantes.

    #:param estudiantes: La lista de estudiantes.

    if not estudiantes:
        print("No hay estudiantes en el registro.")
    else:
        for estudiante in estudiantes:
            print(estudiante)


def buscar_estudiante(estudiantes: list, nombre: str):

   # Busca un estudiante por nombre.

    #:param estudiantes: La lista de estudiantes.
   # :param nombre: El nombre del estudiante a buscar.
   # :return: El estudiante encontrado o None si no se encuentra.

    for estudiante in estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None


def main():
    estudiantes = []
    while True:
        print("\nGestión de Registro de Estudiantes")
        print("1. Agregar Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Buscar Estudiante")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_estudiante(estudiantes)
        elif opcion == '2':
            mostrar_estudiantes(estudiantes)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            estudiante = buscar_estudiante(estudiantes, nombre)
            if estudiante:
                print("Estudiante encontrado:")
                print(estudiante)
            else:
                print(f"Estudiante con nombre {nombre} no encontrado.")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
