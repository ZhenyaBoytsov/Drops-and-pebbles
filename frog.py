import tkinter as tk
from tkinter.font import BOLD

#sizes
Body_size = 50
Tongue_size = 15
Eye_size = 20
Pupil_size = 7

#scales
Area = 500
Eyes_nearess = 0.55

#velocities
Body_velocity = 3
Tongue_velocity = 15

#acceleration
Boost = 3
Boost_time = 30

#frog
Temp = 20
Temp_step = 0.005
M = 5


class body:
    def __init__(self, x, y, canv, v, r = Body_size, color = "green", boost = Boost, boost_time = Boost_time):
        self.x = x
        self.y = y
        self.v = v 
        self.canv = canv
        self.r = r
        self.color = color 
        self.boost = boost
        self.boost_time = boost_time
        self.boost_effect = 0
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)
    
    def acceleration(self, event):
        self.boost_effect = self.boost_time
    
    def move(self, x0, y0):
        v = self.v*(1+self.boost*bool(self.boost_effect))
        self.boost_effect -= bool(self.boost_effect)
        l = ((x0 - self.x)**2 + (y0 - self.y)**2)**0.5
        dx = (x0-self.x)*v/l 
        dy = (y0-self.y)*v/l 
        self.canv.move(self.id, dx, dy)
        self.x += dx
        self.y += dy


class tongue:
    def __init__(self, x, y, canv, r = Tongue_size, color = "pink", mode = 0, v = Tongue_velocity):
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
    
    def too_far(self):
        self.mode = 0
        
    def new_mode(self, event):
        self.mode = 1
        self.target_x = event.x
        self.target_y = event.y
    

class cornea:
    def __init__(self, x, y, canv, r = Eye_size, color = "white", nearness = Eyes_nearess):
        self.x = x
        self.y = y
        self.canv = canv
        self.r = r
        self.color = color 
        self.nearness = nearness
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)
    def move(self, x0, y0):
        self.canv.move(self.id, x0-self.x, y0-self.y)
        self.x = x0
        self.y = y0


class pupil:
    def __init__(self, x, y, canv, r = Pupil_size, color = "black", nearness = Eyes_nearess):
        self.x = x
        self.y = y
        self.canv = canv
        self.r = r
        self.color = color 
        self.nearness = nearness
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)
    def move(self, x0, y0):
        self.canv.move(self.id, x0-self.x, y0-self.y)
        self.x = x0
        self.y = y0
        
class temp_text:
    def __init__(self, x, y, temp, canv):
        self.x = x
        self.y = y
        self.canv = canv
        self.id = self.canv.create_text(self.x, self.y, font=('arial', 18, BOLD), text = int(temp))
    def move(self, x0, y0, temp):
        self.canv.move(self.id, x0 - self.x, y0 - self.y)
        self.x = x0
        self.y = y0
        self.canv.itemconfig(self.id, text=int(temp))

class result:
    def __init__(self, x, y, canv):
        self.canv = canv
        self.x = x
        self.y = y
        self.id = self.canv.create_text(self.x, self.y, font=('arial', 22, BOLD), text = "RESULT: ")
    def rewrite(self, res, language):
        if (language == 0): self.t = "RESULT: "
        else: self.t = "СЧЁТ: "
        self.canv.itemconfig(self.id, text = self.t + str(res))
    
class frog:
    def __init__(self, x, y, canv, v = Body_velocity, area = Area, temp = Temp, temp_step = Temp_step, m = M):
        self.score = 0
        self.temp = temp
        self.temp_step = temp_step
        self.m = m
        self.connect = canv.create_line(x, y, x, y, width=5, fill="pink")
        self.tongue = tongue(x, y, canv)
        self.body = body(x, y, canv, v)
        self.temp_text = temp_text(x, y, temp, canv)
        self.cornea1 = cornea(x, y, canv)
        self.cornea2 = cornea(x, y, canv)
        self.pupil1 = pupil(x, y, canv)
        self.pupil2 = pupil(x, y, canv)
        self.canv = canv
        self.area = area
     
    def move_corneas(self, x0, y0):
        delta_x = x0 - self.body.x
        delta_y = y0 - self.body.y
        l = (delta_x**2 + delta_y**2)**0.5
        delta_x *= self.body.r/l
        delta_y *= self.body.r/l
        x1 = self.cornea1.nearness*(delta_x+delta_y)
        y1 = self.cornea1.nearness*(delta_y-delta_x)
        x2 = self.cornea2.nearness*(delta_x-delta_y)
        y2 = self.cornea2.nearness*(delta_y+delta_x)
        self.cornea1.move(self.body.x+x1, self.body.y+y1)
        self.cornea2.move(self.body.x+x2, self.body.y+y2)
        
    def move_pupils(self, x0, y0):
        delta_x1 = x0 - self.cornea1.x
        delta_y1 = y0 - self.cornea1.y
        delta_x2 = x0 - self.cornea2.x
        delta_y2 = y0 - self.cornea2.y
        l = (delta_x1**2 + delta_y1**2)**0.5
        delta_x1 *= self.pupil1.nearness*self.cornea1.r/l
        delta_y1 *= self.pupil1.nearness*self.cornea1.r/l
        delta_x2 *= self.pupil2.nearness*self.cornea2.r/l
        delta_y2 *= self.pupil2.nearness*self.cornea2.r/l
        self.pupil1.move(self.cornea1.x+delta_x1, self.cornea1.y+delta_y1)
        self.pupil2.move(self.cornea2.x+delta_x2, self.cornea2.y+delta_y2)
          
    def draw_new_connect(self):
        self.canv.delete(self.connect)
        delta_x = self.tongue.x - self.body.x
        delta_y = self.tongue.y - self.body.y
        l = (delta_x**2 + delta_y**2)**0.5
        if (l > self.area):
            self.tongue.too_far()
        if (l > self.body.r + self.tongue.r):
            x1 = self.body.x + delta_x*self.body.r/l
            y1 = self.body.y + delta_y*self.body.r/l
            x2 = self.tongue.x - delta_x*self.tongue.r/l
            y2 = self.tongue.y - delta_y*self.tongue.r/l
            self.connect = self.canv.create_line(x1, y1, x2, y2, width=5, fill="pink")
        else:
            self.connect = self.canv.create_line(0, 0, 0, 0)
            
    def tongue_hit(self, drop_temp):
        self.temp = (self.m*self.temp + drop_temp)/(self.m + 1)
        if (drop_temp > 0): self.score += 1
     
    def body_hit(self, drop_temp):
        self.temp = (self.m*self.temp + drop_temp)/(self.m + 1)
    
    def move(self, x0, y0):
        self.body.move(x0, y0)
        self.tongue.move(self.body.x, self.body.y)
        self.draw_new_connect()
        self.move_corneas(x0, y0)
        self.move_pupils(x0, y0)
        self.temp_text.move(self.body.x, self.body.y, self.temp)
        self.temp -= self.temp_step
    
    def new(self, temp = Temp):
        self.temp = Temp
        self.score = 0