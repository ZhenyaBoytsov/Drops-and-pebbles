import tkinter as tk
from tkinter.font import BOLD
import random
import math

random.seed(version=2)

drop_size=15
drop_velocity=3
velocity_step=0.1
max_velocity=10
max_temp=30
min_temp=-5
dtemp=0.001

drop_color="#00FFFF"
ice_color="#E0FFFF"

class drop:
	def __init__(self, x, y, canv, v=drop_velocity, v_s=velocity_step, m_v=max_velocity, r=drop_size,
				max_temp=max_temp, min_temp=min_temp, dtemp=dtemp, color=drop_color, ice_color=ice_color):
		self.is_warm=1
		self.x=x
		self.y=y 
		self.canv=canv
		a=random.random()*2*math.pi
		self.vx=v*math.sin(a)
		self.vy=v*math.cos(a)
		self.v_s=v_s
		self.m_v=m_v
		self.r=r
		self.color=color
		self.ice_color=ice_color
		self.temp=random.randint(min_temp, max_temp)
		self.min_temp=min_temp
		self.dtemp=dtemp
		self.id=self.canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)
		self.text=self.canv.create_text(self.x, self.y, font=('arial', 18, BOLD), text=int(self.temp))

	def rebound(self, v1, v2):
		v=(v1**2+v2**2)**0.5
		if (v>self.m_v): self.v_s = 0
		v1=-v1*(v+self.v_s)/v
		v2=v2*(v+self.v_s)/v
		return v1, v2

	def make_ice(self):
		self.is_warm=0
		self.r=self.r*1.1
		self.canv.delete(self.id)
		self.canv.delete(self.text)
		self.id=self.canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.ice_color)
		self.text=self.canv.create_text(self.x, self.y, font=('arial', 18, BOLD), text = int(self.temp))

	def hittest(self, x0, y0, r0):
		l = ((x0 - self.x)**2 + (y0 - self.y)**2)**0.5
		return (l <= r0 + self.r)

	def clean(self):
		self.canv.delete(self.id)
		self.canv.delete(self.text)

	def move(self, x0, y0):
		self.temp=self.min_temp+(1-dtemp)*(self.temp-self.min_temp)
		if (self.is_warm==1 and self.temp<0): 
			self.make_ice()
			dx=self.vx
			dy=self.vy
		if (self.x+dx<self.r):
			dx=self.r-self.x
			self.vx, self.vy=self.rebound(self.vx, self.vy)
		if (self.y+dy<self.r):
			dy=self.r-self.y
			self.vy, self.vx=self.rebound(self.vy, self.vx)
		if (self.x+dx>x0-self.r):
			dx=x0-self.r-self.x
			self.vx, self.vy= self.rebound(self.vx, self.vy)
		if (self.y+dy>y0-self.r):
			dy=y0-self.r-self.y
			self.vy, self.vx=self.rebound(self.vy, self.vx)
		self.canv.move(self.id, dx, dy)
		self.canv.move(self.text, dx, dy)
		self.canv.itemconfig(self.text, text=int(self.temp))
		self.x+=dx
		self.y+=dy