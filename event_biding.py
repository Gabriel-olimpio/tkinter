import tkinter as tk
from tkinter import ttk
# list of events
# https://www.pythontutorial.net/tkinter/tkinter-event-binding/


def get_pos(event):
    print(f'x: {event.x} y: {event.y}')


# window  
window = tk.Tk()
window.title('Event Biding')
window.geometry('600x400')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = 'Button')
btn.pack()


# events
btn.bind('<Alt-KeyPress-a>', lambda event: print(event))
text.bind('<Motion>', get_pos)
window.bind('<Keypress>', lambda event: print(f'a button was pressed({event.char})'))

entry.bind('<FocusIn>', lambda event: print('entry field selected'))
entry.bind('<FocusOut>', lambda event: print('entry field unselected'))

# exercise
# print "Mousewheel" when the user hold down shift and uses the mouswheel while text is selected

text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

# run
window.mainloop()