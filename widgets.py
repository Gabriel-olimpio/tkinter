import tkinter as tk
from tkinter import ttk

def button_func():
    print('button pressed')

# create a window
window = tk.Tk()
window.title('Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'Test')
label.pack()

# tk.text
text = tk.Text(master = window) # master is like a parent
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# ttk button
button = ttk.Button(master = window, text = 'Button', command = button_func)
button.pack()

# exercise
# add one more text label and a button with a function that prints "hello"
# the label should say "my label" and be between the entry widget and the button

def button_talk():
    print('hello')

# exercise entry
entry_widget = ttk.Entry(master = window)
entry_widget.pack()

# exercise label
label_widget = ttk.Label(master = window, text = 'my label')
label_widget.pack()

# exercise button
button_widget = ttk.Button(master = window, text = 'Press', command = button_talk)
button_widget.pack()

# run 
window.mainloop() 