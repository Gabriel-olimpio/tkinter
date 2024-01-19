import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')

# Tkinter Variable
string_var = tk.StringVar()

# widgets
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master= window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'Button')
button.pack()

# exercise
# create 2 entry fields and 1 label, they should all be connected via a StringVar
# set a start value of 'test'

string_var2 = tk.StringVar(value = 'test')
# string_var2.set('test')

labely = ttk.Label(master = window, textvariable = string_var2)
labely.pack()

entry_one = ttk.Entry(master = window, textvariable = string_var2)
entry_one.pack()

entry_two = ttk.Entry(master = window, textvariable = string_var2)
entry_two.pack()

# run
window.mainloop()
