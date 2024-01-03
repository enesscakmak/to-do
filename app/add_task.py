import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from tkcalendar import DateEntry


class AddTaskWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()  # Create window
        self.window.title("Add Task")
        self.center_window()
        self.window.resizable(False, False)

        self.title_label = ttk.Label(self.window, text="Title:", background="#f0f0f0")
        self.title_label.grid(row=0, column=0, padx=10, pady=5)

        self.title_entry = ttk.Entry(self.window, foreground="black")
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        self.description_label = ttk.Label(self.window, text="Description:", background="#f0f0f0")
        self.description_label.grid(row=1, column=0, padx=10, pady=5)

        self.description_entry = ttk.Entry(self.window, foreground="black")
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)

        self.priority_label = ttk.Label(self.window, text="Priority:", background="#f0f0f0")
        self.priority_label.grid(row=2, column=0, padx=10, pady=5)

        # Validation for priority
        vcmd = (self.window.register(self.validate_priority), "%P")
        self.priority_entry = ttk.Entry(self.window, validate="key", validatecommand=vcmd, foreground="black")
        self.priority_entry.grid(row=2, column=1, padx=10, pady=5)

        self.finish_by_label = ttk.Label(self.window, text="Finish By:", background="#f0f0f0")
        self.finish_by_label.grid(row=3, column=0, padx=10, pady=5)

        # Use this if you don't want to install tkcalendar
        # self.finish_by_entry = ttk.Entry(self.window, foreground="black")

        # Use this if you want to install tkcalendar ( pip install tkcalendar )
        self.finish_by_entry = DateEntry(self.window, date_pattern="yyyy-mm-dd", background="#f0f0f0",
                                         foreground="black", borderwidth=2, mindate=datetime.now().date())
        #
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

    def validate_priority(self, entry):
        if entry == "":  # Checks to see if entry is empty, otherwise you can't delete what you wrote
            return True
        try:
            priority = int(entry)
            return 0 < priority <= 100  # Priority must be between 1 and 100
        except ValueError:
            return False

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_entry.get()
        finish_by = self.finish_by_entry.get()
        completed = self.varCompleted.get()

        try:
            datetime.strptime(finish_by, "%Y-%m-%d")  # year-month-day format
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
            return

        if title and description and priority and finish_by:  # Check if all fields are filled before saving
            self.parent.add_task(title, description, priority, finish_by, completed)
            self.window.destroy()

    def center_window(self):
        # Update the window to make sure we get correct sizes
        self.window.update()

        # Get window width and height
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        # Get main window width, height, and position
        parent_width = self.parent.root.winfo_width()
        parent_height = self.parent.root.winfo_height()
        parent_x = self.parent.root.winfo_rootx()
        parent_y = self.parent.root.winfo_rooty()

        # Calculate position of window's top-left corner
        position_top = parent_y + int(parent_height / 3 - window_height / 2)

        position_right = parent_x + int(parent_width / 2.2 - window_width / 2)

        # Set the position of the window
        self.window.geometry("+{}+{}".format(position_right, position_top))
