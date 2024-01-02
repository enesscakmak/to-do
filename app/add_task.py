import tkinter as tk
from tkinter import ttk

class AddTaskWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title("Add Task")
        self.center_window()
        self.window.resizable(False, False)

        self.title_label = ttk.Label(self.window, text="Title:", background="#f0f0f0")
        self.title_label.grid(row=0, column=0, padx=10, pady=5)

        self.title_entry = ttk.Entry(self.window)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        self.description_label = ttk.Label(self.window, text="Description:", background="#f0f0f0")
        self.description_label.grid(row=1, column=0, padx=10, pady=5)

        self.description_entry = ttk.Entry(self.window)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)

        self.priority_label = ttk.Label(self.window, text="Priority:", background="#f0f0f0")
        self.priority_label.grid(row=2, column=0, padx=10, pady=5)

        self.priority_entry = ttk.Entry(self.window)
        self.priority_entry.grid(row=2, column=1, padx=10, pady=5)

        self.finish_by_label = ttk.Label(self.window, text="Finish By:", background="#f0f0f0")
        self.finish_by_label.grid(row=3, column=0, padx=10, pady=5)

        self.finish_by_entry = ttk.Entry(self.window)
        self.finish_by_entry.grid(row=3, column=1, padx=10, pady=5)

        self.completed_label = ttk.Label(self.window, text="Completed:", background="#f0f0f0")
        self.completed_label.grid(row=4, column=0, padx=10, pady=5)

        self.varCompleted = tk.StringVar()

        self.completed_entry = ttk.Checkbutton(self.window, variable=self.varCompleted)
        self.completed_entry.grid(row=4, column=1, padx=10, pady=5)
        style = ttk.Style()
        style.configure("TCheckbutton", background="#f0f0f0")  # Background match for checkbutton

        self.add_button = ttk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.grid(row=5, columnspan=2, pady=10)

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_entry.get()
        finish_by = self.finish_by_entry.get()
        completed = self.varCompleted.get()

        if title and description and priority and finish_by:
            self.parent.add_task(title, description, priority, finish_by, completed)
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
        position_top = parent_y + int(parent_height / 3 - window_height / 2)

        position_right = parent_x + int(parent_width / 2.2 - window_width / 2)

        # Set the position of the window
        self.window.geometry("+{}+{}".format(position_right, position_top))