import tkinter as tk

# --- constants --- (UPPER_CASE_NAMES)

SIZE = 40

# --- main --- (lower_case_names)

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

color = 'white'

for y in range(10):

    for x in range(10):
        x1 = x*SIZE
        y1 = y*SIZE
        x2 = x1 + SIZE
        y2 = y1 + SIZE
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == 'white':
            color = 'black'
        else:    
            color = 'white'

    if color == 'white':
        color = 'black'
    else:    
        color = 'white'

root.mainloop()  