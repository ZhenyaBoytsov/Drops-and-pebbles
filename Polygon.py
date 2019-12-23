from array import *
import frog
import drops
import menu
import time
import random
import tkinter as tk

random.seed(version=2)


class Mouse:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def new_coords(self, event):
        self.x = event.x
        self.y = event.y


root = tk.Tk()
X, Y = 1440, 900  # размер окна
root.geometry(str(X) + "x" + str(Y))
root.title("glacier")

canv = tk.Canvas(root, bg="blue")
canv.pack(expand="YES", fill="both")

MENU = menu.menu(X / 2, Y / 2, canv)

f = frog.frog(X / 2, Y / 2, canv)
res = frog.result(X - 100, 50, canv)
DROPS = []

m = Mouse()
root.bind("<Motion>", m.new_coords)
root.bind("<Button-3>", f.tongue.new_mode)
root.bind("<Button-1>", MENU.use_button)
root.bind("<space>", f.body.acceleration)

while MENU.mode == 1:
    MENU.show()
    while MENU.visability == 1:
        root.update()
    MENU.close()
    root.update()
    if MENU.mode == 0: break
    f.new()
    while len(DROPS) > 0:
        DROPS[0].clean()
        DROPS.remove(DROPS[0])
    i = 75
    while f.temp > 0:
        time.sleep(0.01)
        f.move(m.x, m.y)
        for D in DROPS:
            D.move(X, Y)
            if D.hittest(f.body.x, f.body.y, f.body.r):
                f.body_hit(D.temp)
                D.clean()
                DROPS.remove(D)
            elif D.hittest(f.tongue.x, f.tongue.y, f.tongue.r):
                f.tongue_hit(D.temp)
                D.clean()
                DROPS.remove(D)
        i += 1
        if i > 75:
            DROPS.append(drops.drop(random.randint(0, 1) * X, random.randint(0, 1) * Y, canv))  #спавн у границ окна
            i = 0
        res.rewrite(f.score, MENU.language)
        root.update()
