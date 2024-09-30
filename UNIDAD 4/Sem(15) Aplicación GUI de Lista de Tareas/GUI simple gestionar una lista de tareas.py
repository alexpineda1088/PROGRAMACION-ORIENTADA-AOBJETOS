import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        """
        Inicializa la interfaz de la aplicación de gestión de tareas.
        """
        self.root = root
        self.root.title("Gestor de Tareas")  # Título de la ventana principal

        # Lista para almacenar las tareas
        self.tasks = []

        # Campo de entrada donde el usuario puede escribir una nueva tarea
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)  # Ubicación y espacio alrededor del campo de entrada

        # Botón para añadir una nueva tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox para mostrar las tareas actuales
        self.task_listbox = tk.Listbox(root, height=10, width=40, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón para marcar una tarea como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar una tarea
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Asociar la tecla "Enter" con la acción de añadir una tarea
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Asociar doble clic sobre una tarea con la acción de marcarla como completada
        self.task_listbox.bind("<Double-1>", lambda event: self.complete_task())

    # Función para añadir una nueva tarea
    def add_task(self):
        """
        Añade la tarea introducida en el campo de entrada a la lista de tareas.
        Si el campo está vacío, muestra un mensaje de advertencia.
        """
        task = self.task_entry.get()  # Obtener el texto ingresado en el campo de entrada
        if task:
            self.tasks.append(task)  # Añadir la tarea a la lista de tareas
            self.update_task_listbox()  # Actualizar la visualización de la lista
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada después de añadir la tarea
        else:
            # Mostrar advertencia si el usuario intenta añadir una tarea vacía
            messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

    # Función para marcar una tarea como completada
    def complete_task(self):
        """
        Marca la tarea seleccionada como completada, añadiendo "(Completada)" al final del texto.
        Si no hay una tarea seleccionada, muestra un mensaje de advertencia.
        """
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            self.tasks[selected_index] += " (Completada)"  # Modificar la tarea para indicar que está completada
            self.update_task_listbox()  # Actualizar la visualización de la lista
        except IndexError:
            # Mostrar advertencia si no hay una tarea seleccionada
            messagebox.showwarning("Seleccionar tarea", "Por favor, selecciona una tarea.")

    # Función para eliminar una tarea
    def delete_task(self):
        """
        Elimina la tarea seleccionada de la lista de tareas.
        Si no hay una tarea seleccionada, muestra un mensaje de advertencia.
        """
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            del self.tasks[selected_index]  # Eliminar la tarea de la lista
            self.update_task_listbox()  # Actualizar la visualización de la lista
        except IndexError:
            # Mostrar advertencia si no hay una tarea seleccionada
            messagebox.showwarning("Seleccionar tarea", "Por favor, selecciona una tarea.")

    # Función para actualizar el contenido del Listbox
    def update_task_listbox(self):
        """
        Actualiza el Listbox para reflejar las tareas actuales. Limpia el Listbox y vuelve
        a añadir todas las tareas desde la lista de tareas.
        """
        self.task_listbox.delete(0, tk.END)  # Limpiar todas las tareas actualmente mostradas
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Añadir cada tarea al Listbox

# Inicialización de la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal de la aplicación
    task_manager = TaskManager(root)  # Crear una instancia del gestor de tareas
    root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica
