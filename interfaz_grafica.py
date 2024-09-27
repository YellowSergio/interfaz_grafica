import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Administrador de Tareas")
        self.window.geometry("450x450")

        self.todo_list = []
        self.setup_ui()

    def setup_ui(self):
        self.input_task = tk.Entry(self.window, width=40)
        self.input_task.pack(pady=10)

        self.btn_add = tk.Button(self.window, text="Agregar Tarea", command=self.add_task)
        self.btn_add.pack(pady=5)

        self.task_display = tk.Listbox(self.window, width=40, height=10)
        self.task_display.pack(pady=10)

        self.btn_remove = tk.Button(self.window, text="Eliminar Tarea", command=self.remove_task)
        self.btn_remove.pack(side=tk.LEFT, padx=20)

        self.btn_complete = tk.Button(self.window, text="Completar Tarea", command=self.complete_task)
        self.btn_complete.pack(side=tk.RIGHT, padx=20)

        self.status_label = tk.Label(self.window, text="0 tareas")
        self.status_label.pack(pady=10)

    def add_task(self):
        task_text = self.input_task.get()
        if task_text:
            self.todo_list.append(task_text)
            self.task_display.insert(tk.END, task_text)
            self.input_task.delete(0, tk.END)
            self.update_status()
        else:
            messagebox.showwarning("Advertencia", "No se puede agregar una tarea vacía.")

    def remove_task(self):
        try:
            selected_idx = self.task_display.curselection()[0]
            self.task_display.delete(selected_idx)
            del self.todo_list[selected_idx]
            self.update_status()
        except IndexError:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea para eliminar.")

    def complete_task(self):
        try:
            selected_idx = self.task_display.curselection()[0]
            completed_task = self.todo_list[selected_idx] + " (Hecha)"
            self.task_display.delete(selected_idx)
            self.task_display.insert(selected_idx, completed_task)
            self.todo_list[selected_idx] = completed_task
        except IndexError:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea para marcar como completada.")

    def update_status(self):
        total_tasks = len(self.todo_list)
        self.status_label.config(text=f"{total_tasks} tareas en la lista")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
