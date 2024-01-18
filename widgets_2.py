import tkinter as tk
from tkinter import ttk



def button_func():
    # get the content of the entry
    entry_text = entry.get()
    
    # update the label 
    # label.configure(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'

# window 
window = tk.Tk()
window.title('Get and Set widgets')

# widgets
label = ttk.Label(master = window, text = 'Something')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'Press', command = button_func)
button.pack() 

# exercise
# add another button that changes the text back to "some text" and enables entry

def btn_activate():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

button_activate = ttk.Button(master = window, text = 'activate', command = btn_activate)
button_activate.pack()


# run
window.mainloop()