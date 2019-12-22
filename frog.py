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

class tongue:
    def __init__(self, x, y, canv, r = 15, color = "pink", mode = 0, v = 15):
        self.x = x
        self.y = y 
        self.target_x = x
        self.target_y = y
        self.canv = canv
        self.r = r 
        self.color = color
        self.mode = mode
        self.v = v
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)
     
    def move(self, x0, y0):
        if (self.mode == 0):
            l = ((x0 - self.x)**2 + (y0 - self.y)**2)**0.5
            dx = (x0-self.x)*self.v/l 
            dy = (y0-self.y)*self.v/l 
            self.canv.move(self.id, dx, dy)
            self.x += dx
            self.y += dy
        else:
             l = ((self.target_x - self.x)**2 + (self.target_y - self.y)**2)**0.5
             dx = (self.target_x-self.x)*self.v/l 
             dy = (self.target_y-self.y)*self.v/l 
             self.canv.move(self.id, dx, dy)
             self.x += dx
             self.y += dy
             if (l < self.v):
                 self.mode = 0
        
    def new_mode(self, event):
        self.mode = 1
        self.target_x = event.x
        self.target_y = event.y
        

class frog:
    def __init__(self, x, y, canv, v = 3):
        self.connect = canv.create_line(x, y, x, y, width=5, fill="pink")
        self.tongue = tongue(x, y, canv)
        self.body = body(x, y, canv, v)
        self.canv = canv
        #self.x = x
        #self.y = y
        #self.v = v
     
    def draw_new_connect(self):
        self.canv.delete(self.connect)
        delta_x = self.tongue.x - self.body.x
        delta_y = self.tongue.y - self.body.y
        l = (delta_x**2 + delta_y**2)**0.5
        if (l > self.body.r + self.tongue.r):
            x1 = self.body.x + delta_x*self.body.r/l
            y1 = self.body.y + delta_y*self.body.r/l
            x2 = self.tongue.x - delta_x*self.tongue.r/l
            y2 = self.tongue.y - delta_y*self.tongue.r/l
            self.connect = self.canv.create_line(x1, y1, x2, y2, width=5, fill="pink")
        else:
            self.connect = self.canv.create_line(0, 0, 0, 0)
    
    def move(self, x0, y0):
        self.body.move(x0, y0)
        self.tongue.move(self.body.x, self.body.y)
        self.draw_new_connect()
        