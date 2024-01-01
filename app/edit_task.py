import tkinter as tk
from tkinter import ttk

class EditTaskWindow:
    def __init__(self, parent, selected_item):
        self.parent = parent
        self.selected_item = selected_item
        self.index = int(self.parent.task_treeview.index(selected_item))
        self.window = tk.Toplevel()
        self.window.title("Edit Task")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        self.center_window()

        self.title_label = ttk.Label(self.window, text="Title:", background="#f0f0f0")
        self.title_label.pack(pady=5)

        self.title_entry = ttk.Entry(self.window)
        self.title_entry.pack(pady=5)
        self.title_entry.insert(tk.END, self.parent.tasks[self.index]["title"])

        self.description_label = ttk.Label(self.window, text="Description:", background="#f0f0f0")
        self.description_label.pack(pady=5)

        self.description_entry = ttk.Entry(self.window)
        self.description_entry.pack(pady=5)
        self.description_entry.insert(tk.END, self.parent.tasks[self.index]["description"])

        self.priority_label = ttk.Label(self.window, text="Priority:", background="#f0f0f0")
        self.priority_label.pack(pady=5)

        self.priority_entry = ttk.Entry(self.window)
        self.priority_entry.pack(pady=5)
        self.priority_entry.insert(tk.END, self.parent.tasks[self.index]["priority"])

        self.finish_by_label = ttk.Label(self.window, text="Finish By:", background="#f0f0f0")
        self.finish_by_label.pack(pady=5)

        self.finish_by_entry = ttk.Entry(self.window)
        self.finish_by_entry.pack(pady=5)
        self.finish_by_entry.insert(tk.END, self.parent.tasks[self.index]["finish_by"])

        self.completed_label = ttk.Label(self.window, text="Completed:", background="#f0f0f0")
        self.completed_label.pack(pady=5)

        self.completed_var = tk.BooleanVar(value=self.parent.tasks[self.index]["completed"])
        self.completed_checkbutton = tk.Checkbutton(self.window, text="", variable=self.completed_var, bg="#f0f0f0")
        self.completed_checkbutton.pack(pady=5)

        self.edit_button = ttk.Button(self.window, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

    def edit_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_entry.get()
        finish_by = self.finish_by_entry.get()
        completed = bool(self.completed_var.get())


        if title and description and priority and finish_by:
            self.parent.tasks[self.index]["title"] = title  # Add this line to update the title
            self.parent.tasks[self.index]["description"] = description
            self.parent.tasks[self.index]["priority"] = priority
            self.parent.tasks[self.index]["finish_by"] = finish_by
            self.parent.tasks[self.index]["completed"] = completed
            self.parent.update_task_list()
            self.parent.save_tasks()
            self.window.destroy()

    def center_window(self):
        # Update the window to make sure we get correct sizes
        self.window.update()

        # Get window width and height
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        # Get parent window width, height, and position
        parent_width = self.parent.root.winfo_width()
        parent_height = self.parent.root.winfo_height()
        parent_x = self.parent.root.winfo_rootx()
        parent_y = self.parent.root.winfo_rooty()

        # Calculate position of window's top-left corner
        position_top = parent_y + int(parent_height / 2.5 - window_height / 2)
        position_right = parent_x + int(parent_width / 2.2 - window_width / 2)

        # Set the position of the window
        self.window.geometry("+{}+{}".format(position_right, position_top))