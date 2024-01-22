import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title('Sliders')

# slider
scale_float = tk.DoubleVar(value = 15)

scale = ttk.Scale(
    window,
    command = lambda value: progress.stop(), 
    from_ = 0, 
    to = 25,
    length = 300,
    orient = 'horizontal',
    variable = scale_float)
scale.pack()

# progress bar
progress = ttk.Progressbar(
    window,
    variable = scale_float, 
    maximum = 25,
    orient = 'horizontal',
    mode = 'determinate',
    length = 400)
progress.pack()

# Scrolled Text
scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5)
scrolled_text.pack()

# exercise
ex_var = tk.IntVar()

exercise_progress = ttk.Progressbar(
    window,
    variable = ex_var,
    orient = 'vertical'
)
exercise_progress.start()
exercise_progress.pack()

label = ttk.Label(window, textvariable = ex_var)
label.pack()

exercise_scale = ttk.Scale(
    window,
    from_ = 0,
    to = 100,
    variable = ex_var
)
exercise_scale.pack()
# run 
window.mainloop()