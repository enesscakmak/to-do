import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry


class EditTaskWindow:
    def __init__(self, parent, selected_item):
        self.parent = parent
        self.selected_item = selected_item
        self.index = int(self.parent.task_treeview.index(selected_item))  # Get the index of the selected item
        self.window = tk.Toplevel()  # Create a new window
        self.window.title("Edit Task")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        self.center_window()

        self.title_label = ttk.Label(self.window, text="Title:", background="#f0f0f0")
        self.title_label.pack(pady=5)

        self.title_entry = ttk.Entry(self.window, foreground="black")
        self.title_entry.pack(pady=5)
        self.title_entry.insert(tk.END, self.parent.tasks[self.index]["title"])

        self.description_label = ttk.Label(self.window, text="Description:", background="#f0f0f0")
        self.description_label.pack(pady=5)

        self.description_entry = ttk.Entry(self.window, foreground="black")
        self.description_entry.pack(pady=5)
        self.description_entry.insert(tk.END, self.parent.tasks[self.index]["description"])

        self.priority_label = ttk.Label(self.window, text="Priority:", background="#f0f0f0")
        self.priority_label.pack(pady=5)

        self.priority_var = tk.StringVar()
        self.priority_var.set(str(self.parent.tasks[self.index]["priority"]))

        self.priority_var.trace_add("write", self.validate_priority)

        self.priority_entry = ttk.Entry(self.window, textvariable=self.priority_var, foreground="black")
        self.priority_entry.pack(pady=5)

        self.finish_by_label = ttk.Label(self.window, text="Finish By:", background="#f0f0f0")
        self.finish_by_label.pack(pady=5)

        # Use this if you don't want to install tkcalendar
        # self.finish_by_entry = ttk.Entry(self.window, foreground="black")
        # self.finish_by_entry.pack(pady=5)
        # self.finish_by_entry.insert(tk.END, self.parent.tasks[self.index]["finish_by"])

        # Use this if you want to install tkcalendar ( pip install tkcalendar )
        self.finish_by_entry = DateEntry(self.window, date_pattern="yyyy-mm-dd", background="#f0f0f0",
                                         foreground="black", borderwidth=2, mindate=datetime.now().date())
        self.finish_by_entry.pack(pady=5)
        # Set the date to the current date of finish_by in YYYY-MM-DD format
        self.finish_by_entry.set_date(datetime.strptime(self.parent.tasks[self.index]["finish_by"], "%Y-%m-%d").date())
        #

        self.completed_var = tk.BooleanVar(value=self.parent.tasks[self.index]["completed"])
        self.completed_checkbutton = ttk.Checkbutton(self.window, variable=self.completed_var)
        self.completed_checkbutton.pack(pady=5)
        style = ttk.Style()
        style.configure("TCheckbutton", background="#f0f0f0")  # Background match for checkbutton

        self.edit_button = ttk.Button(self.window, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

    def edit_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_entry.get()
        finish_by = self.finish_by_entry.get()
        completed = bool(self.completed_var.get())

        if title and description and priority and finish_by:  # Check if all fields are filled
            try:
                priority = int(priority)
                if not (0 < priority <= 100):  # Priority should be between 0 and 100
                    raise ValueError("Priority should be between 0 and 100.")
            except ValueError:
                # Using messagebox for this as I couldn't resolve why the same thing in add_task is not working
                tk.messagebox.showwarning("False Priority",
                                          "Invalid priority. Please enter a number between 0 and 100 for priority.")
                return

            try:
                datetime.strptime(finish_by, "%Y-%m-%d")
            except ValueError:
                tk.messagebox.showwarning("False Date", "Invalid date format. Please use YYYY-MM-DD.")
                return

            self.parent.tasks[self.index]["title"] = title
            self.parent.tasks[self.index]["description"] = description
            self.parent.tasks[self.index]["priority"] = priority
            self.parent.tasks[self.index]["finish_by"] = finish_by
            self.parent.tasks[self.index]["completed"] = completed
            self.parent.update_task_list()
            self.parent.save_tasks()
            self.window.destroy()

    # Validation for priority
    def validate_priority(self, *args):
        new_text = self.priority_var.get()
        if new_text == "":  # Checks to see if entry is empty, otherwise you can't delete what you wrote
            return True
        try:
            priority = int(new_text)
            return 0 <= priority <= 100
        except ValueError:
            return False

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
