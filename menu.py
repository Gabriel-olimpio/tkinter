import tkinter as tk
from tkinter import ttk

# https://www.pythontutorial.net/tkinter/tkinter-menu/

# window
window = tk.Tk()
window.title('Tab widget')
window.geometry('600x400')

# menu
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff =  False)
file_menu.add_command(label = 'New', command = lambda: print('New File'))
file_menu.add_command(label = 'Open', command = lambda: print('Open File'))
file_menu.add_separator()
menu.add_cascade(label = 'File', menu = file_menu)


# another sub menu
help_menu = tk.Menu(menu, tearoff = False)
menu.add_cascade(label = 'Help', menu = 'help_menu')
help_menu.add_command(label = 'Help entrey', command = lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = 'Check', onvalue = 'on', offvalue = 'off', variable = help_check_string)

# exercise
ex_menu = tk.Menu(menu, tearoff = False)
ex_menu.add_command(label = 'exercise test')
menu.add_cascade(label = 'Exercise', menu = ex_menu )

ex_sub_menu = tk.Menu(menu, tearoff = False)
ex_menu.add_cascade(label = 'sub sub menu', menu = ex_sub_menu)
ex_sub_menu.add_command(label = 'more thing')

window.configure(menu = menu)

# menu button

menu_button = ttk.Menubutton(window, text = 'Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff = False)
button_sub_menu.add_command(label = 'entry 1', command = lambda: print('test 1'))
button_sub_menu.add_checkbutton(label = 'check 1')
# menu_button.configure(menu = button_sub_menu)
menu_button['menu'] = button_sub_menu

# run 
window.mainloop()