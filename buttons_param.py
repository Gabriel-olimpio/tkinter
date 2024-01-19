import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('button pressed')
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print('a button was pressed')
        print(parameter.get())
    return inner_func


# setup
window = tk.TK()
window.title('Buttons param')
window.geometry('600x400')


# widgets
entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, textvariable= entry_string)
entry.pack()

button = ttk.Button(window, text = 'button', command = lambda: outer_func(entry_string))
button.pack()

# run
window.mainloop()