import tkinter as tk

class body:
    def __init__(self, x, y, canv, v, r = 50, color = "green"):
        self.x = x
        self.y = y
        self.v = v 
        self.canv = canv
        self.r = r
        self.color = color 
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)
    
    def move(self, x0, y0):
        l = ((x0 - self.x)**2 + (y0 - self.y)**2)**0.5
        dx = (x0-self.x)*self.v/l 
        dy = (y0-self.y)*self.v/l 
        self.canv.move(self.id, dx, dy)
        self.x += dx
        self.y += dy

class frog:
    def __init__(self, x, y, canv, v = 3):
        self.body = body(x, y, canv, v)
        #self.x = x
        #self.y = y
        #self.v = v
        #self.canv = canv
        
    def move(self, x0, y0):
        self.body.move(x0, y0)
        