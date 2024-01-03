import tkinter as tk
from tkinter import ttk
import json
from add_task import AddTaskWindow
from edit_task import EditTaskWindow
import ttkthemes


class ToDoApp:
    def __init__(self, root):
        self.root = root
        root.minsize(400, 400)
        root.maxsize(600, 600)
        self.center_window()
        self.root.title("To-Do App")
        self.tasks = []

        # Load tasks from JSON file if it exists
        self.load_tasks()

        self.style = ttkthemes.ThemedStyle(root)
        self.style.set_theme("arc")  # Starting theme(adapta looks perfect too, i set it as default
        # selection in OptionMenu so you can directly click Apply Theme to try it)

        # OptionMenu for selecting themes
        self.clicked = tk.StringVar()
        self.clicked.set("adapta")  # Default selection for OptionMenu
        themes = sorted(self.style.get_themes())  # Get all themes available on pc and sort it
        themesMenu = ttk.OptionMenu(root, self.clicked, *themes)
        themesMenu.grid(row=6, column=0)
        themesMenu.config(width=19)
        self.style.configure("TMenubutton", foreground="black", background="#f0f0f0")

        # Button to apply the selected theme
        applyThemeButton = ttk.Button(root, text="Apply Theme", command=self.change_theme, width=22)
        applyThemeButton.grid(row=6, column=1, pady=10)

        self.style.configure("TLabel", foreground="black", background="#f0f0f0", font=("Helvetica", 10))
        self.title_label = ttk.Label(root, text="Plan Everything", font=("Helvetica", 16), background="#f0f0f0")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.sort_by_title_button = ttk.Button(root, text="Sort by Title", command=self.sort_by_title, width=22)
        self.sort_by_title_button.grid(row=1, column=0, padx=10, pady=5)
        self.style.configure("TButton", foreground="black")

        self.sort_by_priority_button = ttk.Button(root, text="Sort by Priority", command=self.sort_by_priority,
                                                  width=22)
        self.sort_by_priority_button.grid(row=1, column=1, padx=10, pady=5)

        self.sort_by_completion_time_button = ttk.Button(root, text="Sort by Completion Time",
                                                         command=self.sort_by_completion_time, width=22)
        self.sort_by_completion_time_button.grid(row=2, column=0, padx=10, pady=5)

        self.sort_by_completed_button = ttk.Button(root, text="Sort by Completed", command=self.sort_by_completed,
                                                   width=22)
        self.sort_by_completed_button.grid(row=2, column=1, padx=10, pady=5)

        # Create Treeview with columns
        self.task_treeview = ttk.Treeview(root,
                                          columns=("ID", "Title", "Description", "Priority", "Finish By", "Completed"),
                                          show="headings", cursor="hand2")

        self.task_treeview.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.style.configure("Treeview", rowheight=25, foreground="black", font=("Helvetica", 10))
        self.style.map("Treeview", background=[('selected', '#c88de3')], foreground=[('selected', 'black')])
        self.style.configure("Treeview.Heading", rowheight=25, foreground="black", font=("Helvetica", 9, "bold"))

        # Set column headings and center text
        columns = ["ID", "Title", "Description", "Priority", "Finish By", "Completed"]
        for col in columns:
            self.task_treeview.heading(col, text=col, anchor="center", command=lambda c=col: self.sort_by_column(c))
            self.task_treeview.column(col, anchor="center", width=30)
            if col == "ID":
                self.task_treeview.column(col, width=20, stretch=tk.NO)

        # Add weight configuration for rows and columns
        # These lines are to make the app responsive
        # First is index, and weight specifies how much additional space will it gain when resized
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(3, weight=1)
        root.columnconfigure(1, weight=1)

        self.add_button = ttk.Button(root, text="Add Task", command=self.open_add_task_window, width=22)
        self.add_button.grid(row=4, column=0, columnspan=1, pady=5)

        self.edit_button = ttk.Button(root, text="Edit Task", command=self.open_edit_task_window, width=22)
        self.edit_button.grid(row=4, column=1, columnspan=1, pady=5)

        self.remove_button = ttk.Button(root, text="Remove Task", command=self.remove_task, width=22)
        self.remove_button.grid(row=5, column=0, columnspan=1, pady=5)

        self.complete_button = ttk.Button(root, text="Complete Task", command=self.complete_task, width=22)
        self.complete_button.grid(row=5, column=1, columnspan=1, pady=5)

        # Save tasks to JSON file when the application is closed
        root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.update_task_list()

    def change_theme(self):
        style = ttkthemes.ThemedStyle(root)
        style.theme_use(self.clicked.get())

    # Sorting functions
    # You can add reverse=True if you want to sort by descending order
    # Example: self.tasks.sort(key=lambda task: task["title"], reverse=True)
    def sort_by_title(self):
        self.tasks.sort(key=lambda task: task["title"])
        self.update_task_list()

    def sort_by_priority(self):
        self.tasks.sort(key=lambda task: int(task["priority"]))
        self.update_task_list()

    def sort_by_completion_time(self):
        self.tasks.sort(key=lambda task: task["finish_by"])
        self.update_task_list()

    def sort_by_completed(self):
        self.tasks.sort(key=lambda task: task["completed"])
        self.update_task_list()

    def sort_by_column(self, column):
        if column == "ID":
            return
        else:
            column_key = column.replace(" ", "_").lower()
        self.tasks.sort(key=lambda task: task[column_key])
        self.update_task_list()

    def add_task(self, title, description, priority, finish_by, completed):
        task = {
            "title": title,
            "description": description,
            "priority": priority,
            "finish_by": finish_by,
            "completed": bool(completed)
        }

        self.tasks.append(task)
        self.update_task_list()
        self.save_tasks()

    def remove_task(self):
        selected_item = self.task_treeview.selection()  # Get selected item from Treeview
        if selected_item:
            task_index = int(self.task_treeview.index(selected_item[0]))
            del self.tasks[task_index]
            self.update_task_list()
            self.save_tasks()

    def complete_task(self):
        focused_item = self.task_treeview.focus()
        if focused_item:
            index = int(self.task_treeview.index(focused_item))
            if 0 <= index < len(self.tasks):
                self.tasks[index]["completed"] = True
                self.update_task_list()
                self.save_tasks()

    def center_window(self):
        # Get window width and height
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate position of window's top-left corner
        # 3.5 and 2.2 is because it was in middle of screen like this (for 1920x1080)
        # but i don't know for sure if it will be the same for every screen
        position_top = int(screen_height / 3.5 - window_height / 2)
        position_right = int(screen_width / 2.2 - window_width / 2)

        # Set the position of the window
        self.root.geometry("+{}+{}".format(position_right, position_top))

    def update_task_list(self):
        # Clear existing data in the Treeview
        for item in self.task_treeview.get_children():
            self.task_treeview.delete(item)

        # Insert new data into the Treeview
        for task_index, task in enumerate(self.tasks):
            # Use task_index as an identifier for the task
            self.task_treeview.insert("", tk.END, values=(
                task_index, task["title"], task["description"], task["priority"], task["finish_by"], task["completed"]))

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            pass

    def on_close(self):
        self.save_tasks()
        self.root.destroy()

    def open_add_task_window(self):
        AddTaskWindow(self)

    def open_edit_task_window(self):
        selected_item = self.task_treeview.selection()
        if selected_item:
            EditTaskWindow(self, selected_item[0])


root = tk.Tk()
ToDoApp(root)
root.mainloop()
