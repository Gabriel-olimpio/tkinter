import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Tab widget')
window.geometry('600x400')

# Notebook Widget
notebook = ttk.Notebook(window)


tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = 'Some text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text = 'button in tab 1')
button1.pack()


tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'text in tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()



# exercise
# add another tab with 2 buttons and one label inside

tab3 = ttk.Frame(notebook)
label3 = ttk.Label(tab3, text = 'text in tab 3')
label3.pack()
button3 = ttk.Button(tab3, text = 'Button 1')
button3.pack()
button3_1 =ttk.Button(tab3, text = 'Button 2')
button3_1.pack()


notebook.add(tab1, text= 'Tab 1')
notebook.add(tab2, text= 'Tab 2')
notebook.add(tab3, text= 'Tab 3')
notebook.pack()


# run
window.mainloop()