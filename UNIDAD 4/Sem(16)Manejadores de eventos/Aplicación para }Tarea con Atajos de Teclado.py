import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root
        self.root.title("Gestor de Tareas")

        # Crear un marco para contener el campo de entrada y los botones
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)  # Añadir un espaciado vertical

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(side=tk.LEFT)  # Posicionarlo a la izquierda en el marco

        # Botón para añadir tarea
        self.add_button = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)  # Posicionarlo a la izquierda en el marco

        # Botón para marcar como completada
        self.complete_button = tk.Button(self.frame, text="Marcar Completada", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT)  # Posicionarlo a la izquierda en el marco

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT)  # Posicionarlo a la izquierda en el marco

        # Lista para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, width=75, height=10)
        self.task_listbox.pack(pady=10)  # Añadir espaciado vertical

        # Vincular atajos de teclado a funciones
        self.root.bind('<Return>', lambda event: self.add_task())  # Presionar Enter para añadir tarea
        self.root.bind('<c>', lambda event: self.complete_task())  # Presionar C para completar tarea
        self.root.bind('<Delete>', lambda event: self.delete_task())  # Presionar Delete para eliminar tarea
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Presionar Escape para cerrar la aplicación

    def add_task(self):
        # Obtener el texto del campo de entrada
        task = self.task_entry.get()
        if task:  # Verificar si hay texto en el campo
            self.task_listbox.insert(tk.END, task)  # Añadir tarea a la lista
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            # Mostrar un mensaje de advertencia si no se ingresa una tarea
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def complete_task(self):
        try:
            # Obtener el índice de la tarea seleccionada
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)  # Obtener el texto de la tarea seleccionada
            # Marcar la tarea como completada
            self.task_listbox.delete(selected_task_index)  # Eliminar la tarea original
            # Insertar la tarea completada con una anotación
            self.task_listbox.insert(selected_task_index, f"{task} (Completada)")
            # Cambiar el color de fondo de la tarea completada
            self.task_listbox.itemconfig(selected_task_index, {'bg': 'light green'})
        except IndexError:
            # Mostrar un mensaje de advertencia si no se selecciona ninguna tarea
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            # Obtener el índice de la tarea seleccionada
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)  # Eliminar la tarea seleccionada
        except IndexError:
            # Mostrar un mensaje de advertencia si no se selecciona ninguna tarea
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")


if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    app = TaskManagerApp(root)  # Instanciar la aplicación
    root.mainloop()  # Iniciar el bucle de la interfaz gráfica
