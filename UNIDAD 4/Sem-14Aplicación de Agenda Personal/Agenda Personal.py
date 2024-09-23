import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import tkinter.simpledialog as simpledialog

class AgendaApp:
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root
        self.root.title("Agenda Personal")

        # Crea un marco para los elementos de la interfaz
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Etiqueta y campo de entrada para la fecha
        self.label_fecha = tk.Label(self.frame, text="Fecha (DD/MM/AAAA):")
        self.label_fecha.grid(row=0, column=0)
        self.entry_fecha = tk.Entry(self.frame)
        self.entry_fecha.grid(row=0, column=1)

        # Etiqueta y campo de entrada para la hora
        self.label_hora = tk.Label(self.frame, text="Hora (HH:MM):")
        self.label_hora.grid(row=1, column=0)
        self.entry_hora = tk.Entry(self.frame)
        self.entry_hora.grid(row=1, column=1)

        # Etiqueta y campo de entrada para la descripción
        self.label_descripcion = tk.Label(self.frame, text="Descripción:")
        self.label_descripcion.grid(row=2, column=0)
        self.entry_descripcion = tk.Entry(self.frame)
        self.entry_descripcion.grid(row=2, column=1)

        # Botón para agregar un evento
        self.btn_agregar = tk.Button(self.frame, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=3, column=0, pady=10)

        # Botón para eliminar el evento seleccionado
        self.btn_eliminar = tk.Button(self.frame, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=3, column=1, pady=10)

        # TreeView para mostrar los eventos programados
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=20)

    def agregar_evento(self):
        # Obtiene los datos de entrada
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        # Verifica que todos los campos estén llenos
        if fecha and hora and descripcion:
            # Agrega un nuevo evento al TreeView
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            # Limpia los campos de entrada
            self.entry_fecha.delete(0, tk.END)
            self.entry_hora.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)
        else:
            # Muestra una advertencia si faltan campos
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        # Obtiene el evento seleccionado
        selected_item = self.tree.selection()
        if selected_item:
            # Pide confirmación antes de eliminar
            confirm = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este evento?")
            if confirm:
                # Elimina el evento seleccionado
                self.tree.delete(selected_item)
        else:
            # Muestra una advertencia si no hay selección
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")

if __name__ == "__main__":
    # Crea la ventana principal y ejecuta la aplicación
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
