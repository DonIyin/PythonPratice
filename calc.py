import tkinter as tk
from tkinter import messagebox

# window initialization
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x450")
root.resizable(False, False)
frame = tk.Frame(root)

# entry definitions
display = tk.Entry(root, background='#ddf', font='arial, 20', width=60, justify="right")
display.insert(0, "0")
display.pack(pady=20, padx=5)


# function to evaluate and display result
def calculate():
    try:
        result = eval(display.get())  # Evaluate the expression in the entry
        display.delete(0, tk.END)     # Clear the entry
        display.insert(tk.END, str(result))  # Display the result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")


# function to handle button clicks
def button_click(symbol):
    display.insert(tk.END, symbol)


# function to clear the entry
def clear_entry():
    display.delete(0, tk.END)
    display.insert(0, "0")


# function to delete the last character in the entry
def delete():
    current_entry = display.get()
    if len(current_entry) > 1:
        display.delete(len(current_entry) - 1, tk.END)
    elif len(current_entry) == 1:
        display.delete(0, tk.END)
        display.insert(tk.END, "0")


# function to confirm quitting
def quit_button():
    confirm_quit = messagebox.askyesno("Leave Calculator", "Are you sure you want to quit?")
    if confirm_quit:
        root.destroy()


# button layout
buttons = [
    ("7", lambda: button_click('7')),
    ("8", lambda: button_click('8')),
    ("9", lambda: button_click('9')),
    ("4", lambda: button_click('4')),
    ("5", lambda: button_click('5')),
    ("6", lambda: button_click('6')),
    ("1", lambda: button_click('1')),
    ("2", lambda: button_click('2')),
    ("3", lambda: button_click('3')),
    ("0", lambda: button_click('0')),
    ("+", lambda: button_click('+')),
    ("-", lambda: button_click('-')),
    ("*", lambda: button_click('*')),
    ("/", lambda: button_click('/')),
    ("=", calculate),
    ("C", clear_entry),
    ("DEL", delete)
]

# create and place buttons
for i, (text, command) in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    btn = tk.Button(frame, text=text, font="Arial 10", width=10, height=3, foreground="blue", command=command)
    btn.grid(row=row, column=col, sticky=(tk.W, tk.E))

frame.pack()

# quit button
quit_btn = tk.Button(root, text="Quit", font=14, command=quit_button)
quit_btn.pack(pady=10)

# start the main event loop
root.mainloop()
