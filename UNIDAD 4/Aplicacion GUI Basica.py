import tkinter as tk
from tkinter import messagebox

# Funciones para manejar los eventos
def agregar():
    texto = entry_text.get()  # Obtiene el texto del campo de entrada
    if texto:  # Verifica si el campo de entrada no está vacío
        lista.insert(tk.END, texto)  # Inserta el texto al final de la lista (Listbox)
        entry_text.set("")  # Limpia el campo de entrada después de agregar el texto
    else:
        # Muestra una advertencia si el usuario intenta agregar un texto vacío
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

def limpiar():
    # Borra todos los elementos de la lista (Listbox) desde el primer elemento hasta el último
    lista.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()  # Crea la ventana principal de la aplicación
ventana.title("Aplicación GUI Básica")  # Establece el título de la ventana
ventana.geometry('500x500')
# Etiqueta descriptiva
label = tk.Label(ventana, text="Ingrese información:")  # Crea una etiqueta con el texto "Ingrese información"
label.pack(pady=5)  # Muestra la etiqueta en la ventana con un pequeño margen vertical (pady)

# Campo de texto
entry_text = tk.StringVar()  # Crea una variable para almacenar el texto ingresado por el usuario
entry = tk.Entry(ventana, textvariable=entry_text)  # Crea un campo de texto vinculado a la variable 'entry_text'
entry.pack(pady=5)  # Muestra el campo de texto en la ventana con un margen vertical

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)  # Crea un botón con el texto "Agregar"
# Al hacer clic en el botón, se llama a la función 'agregar'
boton_agregar.pack(pady=5)  # Muestra el botón en la ventana con un pequeño margen

# Lista para mostrar los datos agregados
lista = tk.Listbox(ventana)  # Crea una lista (Listbox) para mostrar los elementos agregados
lista.pack(pady=5)  # Muestra la lista en la ventana con un margen vertical

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)  # Crea un botón con el texto "Limpiar"
# Al hacer clic en el botón, se llama a la función 'limpiar'
boton_limpiar.pack(pady=5)  # Muestra el botón en la ventana con un margen vertical

# Ejecutar la aplicación
ventana.mainloop()  # Inicia el bucle principal de la aplicación para que la ventana permanezca abierta y activa