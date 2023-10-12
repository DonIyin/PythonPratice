__author__ = "Iyinoluwa Don-Taiwo"
import tkinter as tk
from tkinter import Entry, Button, Listbox, Scrollbar
from tkinter import messagebox

# Function to add a task
def add_task(event=None):  # Add an event parameter to handle Enter key press
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Task description cannot be empty.")

# Function to mark a task as complete
def complete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task_index = int(selected_task_index[0])
        tasks_listbox.itemconfig(task_index, {'bg': 'light gray'})
        completed_tasks_listbox.insert(tk.END, tasks_listbox.get(task_index))
        tasks_listbox.delete(task_index)
    else:
        messagebox.showerror("Error", "Please select a task to mark as complete.")

# Create the main window with larger dimensions
window = tk.Tk()
window.title("Task Manager")
window.geometry("400x400")  # Set the window size

# Create and configure widgets
task_label = tk.Label(window, text="Add Task:", font=("Helvetica", 12))
task_label.pack()

task_entry = tk.Entry(window, font=("Helvetica", 12))
task_entry.pack()

add_button = tk.Button(window, text="Add Task", command=add_task, font=("Helvetica", 12), bg='green', fg='white')
add_button.pack()

list_label = tk.Label(window, text="Tasks:", font=("Helvetica", 12))
list_label.pack()

tasks_listbox = Listbox(window, selectmode=tk.SINGLE, font=("Helvetica", 12), bg='light blue')
tasks_listbox.pack()

complete_button = tk.Button(window, text="Mark Complete", command=complete_task, font=("Helvetica", 12), bg='blue', fg='white')
complete_button.pack()

completed_label = tk.Label(window, text="Completed Tasks:", font=("Helvetica", 12))
completed_label.pack()

completed_tasks_listbox = Listbox(window, selectmode=tk.SINGLE, font=("Helvetica", 12), bg='light gray')
completed_tasks_listbox.pack()

# Add a scrollbar for tasks list
tasks_scrollbar = Scrollbar(window)
tasks_listbox.config(yscrollcommand=tasks_scrollbar.set)
tasks_scrollbar.config(command=tasks_listbox.yview)
tasks_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Bind the Enter key to the "Add Task" function
task_entry.bind("<Return>", add_task)

# Start the GUI event loop
window.mainloop()
