import tkinter as tk
from tkinter.font import BOLD

#sizes
Xsize = 800
Ysize = 600

class menu:
    def __init__(self, x, y, canv, xsize = Xsize, ysize = Ysize):
        self.x = x 
        self.y = y 
        self.xsize = xsize
        self.ysize = ysize
        self.canv = canv
        self.visability = 0
        self.mode = 1
        self.language = 0
        
    def clean(self):
        self.canv.delete(self.text1)
        self.canv.delete(self.text2)
        self.canv.delete(self.text3)
        self.canv.delete(self.text4)
    
    def write(self):
        l = 0.8*self.xsize/2
        h = 0.2*self.ysize
        dh = 0.2*h
        if (self.language):
            self.text1 = self.canv.create_text(self.x, self.y - self.ysize/2 +1*dh + 0.5*h, font=('arial', int(self.ysize/12), BOLD), text = "НОВАЯ ИГРА")
            self.text2 = self.canv.create_text(self.x, self.y - self.ysize/2 +2*dh + 1.5*h, font=('arial', int(self.ysize/12), BOLD), text = "РЕКОРДЫ")
            self.text3 = self.canv.create_text(self.x, self.y - self.ysize/2 +3*dh + 2.5*h, font=('arial', int(self.ysize/12), BOLD), text = "ЯЗЫК")
            self.text4 = self.canv.create_text(self.x, self.y - self.ysize/2 +4*dh + 3.5*h, font=('arial', int(self.ysize/12), BOLD), text = "ВЫХОД")
        else:
            self.text1 = self.canv.create_text(self.x, self.y - self.ysize/2 +1*dh + 0.5*h, font=('arial', int(self.ysize/12), BOLD), text = "NEW GAME")
            self.text2 = self.canv.create_text(self.x, self.y - self.ysize/2 +2*dh + 1.5*h, font=('arial', int(self.ysize/12), BOLD), text = "BEST RESULTS")
            self.text3 = self.canv.create_text(self.x, self.y - self.ysize/2 +3*dh + 2.5*h, font=('arial', int(self.ysize/12), BOLD), text = "LANGUAGE")
            self.text4 = self.canv.create_text(self.x, self.y - self.ysize/2 +4*dh + 3.5*h, font=('arial', int(self.ysize/12), BOLD), text = "QUIT")
    
    def show(self):
        self.visability = 1
        self.bg = self.canv.create_rectangle(self.x - self.xsize/2, self.y - self.ysize/2, self.x + self.xsize/2, self.y + self.ysize/2, fill="yellow")
        l = 0.8*self.xsize/2
        h = 0.2*self.ysize
        dh = 0.2*h
        self.str1 = self.canv.create_rectangle(self.x - l, self.y - self.ysize/2 + dh, self.x + l, self.y - self.ysize/2 +dh + h, fill="red")
        self.str2 = self.canv.create_rectangle(self.x - l, self.y - self.ysize/2 +2*dh + h, self.x + l, self.y - self.ysize/2 +2*dh + 2*h, fill="red")
        self.str3 = self.canv.create_rectangle(self.x - l, self.y - self.ysize/2 +3*dh + 2*h, self.x + l, self.y - self.ysize/2 +3*dh + 3*h, fill="red")
        self.str4 = self.canv.create_rectangle(self.x - l, self.y - self.ysize/2 +4*dh + 3*h, self.x + l, self.y - self.ysize/2 +4*dh + 4*h, fill="red")
        self.write()
    
    def close(self):
        self.canv.delete(self.bg)
        self.canv.delete(self.str1)
        self.canv.delete(self.str2)
        self.canv.delete(self.str3)
        self.canv.delete(self.str4)
        self.canv.delete(self.text1)
        self.canv.delete(self.text2)
        self.canv.delete(self.text3)
        self.canv.delete(self.text4)
        self.visability = 0
    
    def use_button(self, event):
        l = 0.8*self.xsize/2
        h = 0.2*self.ysize
        dh = 0.2*h
        if (self.visability == 0): return
        norm_x = ((event.x > self.x - l) and (event.x < self.x + l))
        if (not norm_x): return
        y1 = ((event.y > self.y - self.ysize/2 + dh) and (event.y < self.y - self.ysize/2 +dh + h))
        y2 = ((event.y > self.y - self.ysize/2 + 2*dh + h) and (event.y < self.y - self.ysize/2 +2*dh + 2*h))
        y3 = ((event.y > self.y - self.ysize/2 + 3*dh + 2*h) and (event.y < self.y - self.ysize/2 +3*dh + 3*h))
        y4 = ((event.y > self.y - self.ysize/2 + 4*dh + 3*h) and (event.y < self.y - self.ysize/2 +4*dh + 4*h))
        
        if y1:
            self.mode = 1
            self.visability = 0
        elif y2:
            self.canv.delete(self.text2)
            if (self.language): t = "ТЫ ВСЕГДА ЛУЧШИЙ!"
            else: t = "YOU'RE ALWAYS THE BEST!"
            self.text2 = self.canv.create_text(self.x, self.y - self.ysize/2 +2*dh + 1.5*h, font=('arial', int(self.ysize/20), BOLD), text = t)
        elif y3:
            self.language = 1 - self.language
            self.clean()
            self.write()
        elif y4:
            self.mode = 0
            self. visability = 0   





