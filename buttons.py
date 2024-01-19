import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

# button
def button_func():
    print('basic button')
    print(radio_var.get())

button_string = tk.StringVar(value = 'a button with string var')
button = ttk.Button(window, text = 'A button', command = button_func, textvariable = button_string)
button.pack()

# checkbutton
check_var = tk.BooleanVar()
check = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    command = lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = 5)
check.pack()

check2 = ttk.Checkbutton(
    window,
    text = 'checkbox 2',
    command = lambda: print('test')
)
check2.pack()
# radio buttons

radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'radio button 1',
    value = 'radio 1',
    variable = radio_var,
    command = lambda: print(radio_var.get())) 
radio1.pack()

radio2 = ttk.Radiobutton(
    window,
    text = 'radio button 2',
    value = 2,
    variable = radio_var)
radio2.pack()

# exercise

exercise_boolvar = tk.BooleanVar()
radio_string = tk.StringVar()

exercise_check = ttk.Checkbutton(
    window,
    text = 'exercise check',
    variable = exercise_boolvar,
    command= lambda : print(radio_string.get()))
exercise_check.pack()

def radio_func():
    print(exercise_boolvar.get())
    exercise_boolvar.set(False)



exercise_radiob1 = ttk.Radiobutton(
    window,
    text = 'r1',
    value = 'A',
    command = radio_func,
    variable= radio_string)
exercise_radiob1.pack()

exercise_radiob2 = ttk.Radiobutton(
    window,
    text = 'r2',
    value = 'B',
    command = radio_func,
    variable= radio_string)
exercise_radiob2.pack()


# run
window.mainloop()