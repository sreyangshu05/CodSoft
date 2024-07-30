import tkinter as tk
from tkinter import messagebox
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x400")
        self.root.config(bg="#f5f5f5")
        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16), fg="#ffffff", bg="black")
        self.title_label.pack(pady=10)
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(root, textvariable=self.task_var, width=40, font=("Helvetica", 12))
        self.task_entry.pack(pady=10)
        self.buttons_frame = tk.Frame(root, bg="#f5f5f5")
        self.buttons_frame.pack(pady=10)
        self.add_button = tk.Button(self.buttons_frame, text="Add Task", command=self.add_task, bg="#00cc66",
                                    fg="#ffffff")
        self.add_button.grid(row=0, column=0, padx=5)
        self.update_button = tk.Button(self.buttons_frame, text="Update Task", command=self.update_task, bg="#ffcc00",
                                       fg="#ffffff")
        self.update_button.grid(row=0, column=1, padx=5)
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task, bg="#ff3333",
                                       fg="#ffffff")
        self.delete_button.grid(row=0, column=2, padx=5)
        self.tasks_listbox = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12))
        self.tasks_listbox.pack(pady=20)
        self.tasks = []
    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    def update_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            new_task = self.task_var.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_tasks_listbox()
                self.task_var.set("")
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")
    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)
def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()