# To-Do App
Basic to-do project to practice coding. Both in web and as a app.  

[Go to App Version](#-app)  
[Go to Web Version](#-web)

# App


<p align="center">
<img width="40%" height="10%" src="https://github.com/enesscakmak/to-do/assets/114193468/817805e8-9a4e-40cf-aa43-553295d96466">
</p>

## Features

- Add, edit, remove and complete tasks with a user-friendly interface.  

- Sort tasks by title, priority, completion time, and completed status.    
- Sort whether with buttons or by column headers.    
- Select the theme you want to see.  
- Responsive layout for an improved user experience.
    
<p align="center">
<img width="40%" height="10%" src="https://github.com/enesscakmak/to-do/assets/114193468/e3c52134-00f2-4d93-9778-0b54d5029946">
<img width="40%" height="10%" src="https://github.com/enesscakmak/to-do/assets/114193468/2e830a6e-d858-4291-bf83-5b77beba12a6">
</p>   
  
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/enesscakmak/to-do
2. Change into the project directory:
   ```bash
   cd to-do  
   cd app
3. Run the app
   ```bash
   python todo_app.py

### Dependencies  
- `tkthemes`: A library for adding themes to Tkinter applications.
   ```bash
   pip install ttkthemes
- `tkcalendar`: A calendar widget for Tkinter.
  ```bash
  pip install tkcalendar
### Usage
Add new tasks with a title, description, priority, finish by date, and completion status.
Edit existing tasks to update information or mark them as completed.
Remove tasks that are no longer needed.
Sort tasks based on various criteria for better organization.
  

# Web  


### Stack  
- SQLAlchemy
- Flask
- WTForms
- Bootstrap 5

        
### Home
- Simple landing page with buttons that direct to task list or add task page.  

![home](https://github.com/enesscakmak/to-do/assets/114193468/d7779489-5089-4122-b2c7-bdd73b286a9c)


### Task List  
- Task list page that shows the components of your tasks.  
- You can sort by pressing headers like Title for alphabetical order of titles or Priority for numeratic order.  
- You can go into Edit and Details page or Delete the task if you want from here too.  
- There are home and add task button on top left to surf and a dropdown to select how many of task you want to see in a page.  
- You can navigate between task lists with the pagination buttons at the bottom.

![tasks](https://github.com/enesscakmak/to-do/assets/114193468/d636ca79-70b6-4323-a243-cae457d29df0)  

### Add Task  
- Page for adding tasks with Title, Description(non-essential), Priority, Date and a radiobutton to check if you already did it.
- You can enter date by hand or with a date picker calendar.

![addTask](https://github.com/enesscakmak/to-do/assets/114193468/415b4ac4-a71b-4631-ab1d-b9ce84ec5018)


### Edit Task  
- Page to edit any information of a task or to check completed when a task is done.

   ![editTask](https://github.com/enesscakmak/to-do/assets/114193468/a5d09542-51e0-4aec-b8ae-912137cb8208)

### Details  
- Details page if you want to see all details of a task plainly.


![details](https://github.com/enesscakmak/to-do/assets/114193468/326c7067-43fb-4d28-aed0-c81119aaa448)
