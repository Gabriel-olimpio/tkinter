import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Frames and parenting')
window.geometry('600x400')


# frame
frame = ttk.Frame(window, width = 100, height = 200, borderwidth = 10, relief = tk.GROOVE )
frame.pack(side = 'left')

# master setting
label = ttk.Label(frame, text = 'label in frame')
label.pack()

button = ttk.Button(frame, text= 'butto in frame')
button.pack()

# example
label2 = ttk.Label(window, text = 'label outside the frame')
label2.pack(side = 'left')

# exercise
# create another frame with a label, a button and an entry and place it to the right of other widgets

frame2 = ttk.Frame(window, width = 120, height = 220, borderwidth= 12, relief = tk.GROOVE )
frame2.pack(side = 'right')

ex_label = ttk.Label(frame2, text = 'frame 2 label')
ex_label.pack()

button2 = ttk.Button(frame2, text = 'frame 2 button')
button2.pack()

entry2 = ttk.Entry(frame2) 
entry2.pack()

# run
window.mainloop()