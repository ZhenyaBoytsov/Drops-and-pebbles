import frog
import time
import tkinter as tk

class mouse:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 
    def new_coords(self, event):
        self.x = event.x 
        self.y = event.y 

root = tk.Tk()
root.geometry("1440x1080")
root.title("glacier")

canv = tk.Canvas(root, bg = "blue")
canv.pack(expand="YES",  fill="both")

f = frog.frog(720, 540, canv)
    
m = mouse()
root.bind("<Motion>", m.new_coords)
root.bind("<Button-1>", f.tongue.new_mode)

while(1):
    root.after(10, f.move(m.x, m.y))
    root.update()
 
root.mainloop()

