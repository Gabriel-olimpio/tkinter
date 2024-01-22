import tkinter as tk
from tkinter import ttk

# https://www.pythontutorial.net/tkinter/tkinter-canvas/

# window
window = tk.Tk()
window.title('Canvas')
window.geometry('600x400')


# canvas

canvas = tk.Canvas(window, bg = 'black')
canvas.pack()

# canvas.create_rectangle((50, 20, 100, 200), fill = 'red', width = 10, dash = (4, 2), outline = 'gray')
# canvas.create_line((0, 0, 100, 150), fill = 'blue')
# canvas.create_oval(0, 0, 100, 100, fill = 'green')
# canvas.create_polygon((0,0, 100,200, 300,50), fill = 'yellow')
# canvas.create_arc((200, 0, 300, 100),
#                 fill = 'red', 
#                 start = 45, 
#                 extent = 180, 
#                 style = tk.ARC, 
#                 outline = 'yellow', 
#                 width = 10)


# canvas.create_text((100, 200), text = 'some text', fill = 'green', width = 10)

# canvas.create_window((50, 100), window = ttk.Label(window, text = 'text in a canvas'))


# Exercise
# use event biding to create a basic paint app


def draw_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2), fill = 'red')

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0, min(brush_size, 50))


brush_size = 4
canvas.bind('<Motion>', draw_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)

#run
window.mainloop()