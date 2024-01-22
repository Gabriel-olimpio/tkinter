import tkinter as tk
from tkinter import ttk
from random import choice

# window
window = tk.Tk()
window.title('TreeView')
window.geometry('600x400')

# data

first_names = ['Bob', 'Claudio', 'Augustus', 'Jamnes', 'Heisenberg', 'Jesse']
last_names = ['Wilson', 'Maximus', 'Loren', 'Jems', 'White', 'Pigman']

# treeview
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Surname')
table.heading('email', text = 'Email')
table.pack(fill = 'both', expand = True)

# insert values into a table
# table.insert(parent = '', index = 0, values = ('Joao', 'Jose', 'joaojose@gmail.com'))

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first[0]}{last}@email.com'

    data = (first, last, email)
    table.insert(parent = '', index = 0, values = data)

table.insert(parent = '', index = tk.END, values = ('xxxx', 'yyyy', 'zzzz')) # insert a value at the end of the table


# events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])


def delete_items(_):
    print('Delete')
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)


# run
window.mainloop()