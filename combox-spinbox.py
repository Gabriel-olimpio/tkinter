import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Combobox and Spinbox')
window.geometry('600x400')

#combobox
items = ('Ice cream', 'Pizza', 'Sushi')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo['values'] = items
# combo.configure(values = items)
combo.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected Value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

# Spinbox
spin_Int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
    window, 
    from_ = 3, 
    to = 30, 
    increment = 3, 
    command = lambda: print(spin_Int.get()),
    textvariable = spin_Int)

spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
# spin['value'] = (1,2,3,4,5)
spin.pack()


# exercise 
# create a spinbox that contains the letters A B C D E
# and print the value whenever the value is decreased

letters = ('A', 'B', 'C', 'D', 'E')
exercise_string = tk.StringVar(value = letters[0])
exercise_spin = ttk.Spinbox(window, textvariable = exercise_string, values = letters)
exercise_spin.bind('<<Decrement>>', lambda event: print(exercise_string.get()))
exercise_spin.pack()

#run
window.mainloop()