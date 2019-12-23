import tkinter as tk
from tkinter.font import BOLD
import random
import math

random.seed(version=2) # делает последующие вызовы генератора случайных чисел детерминированными: вход А производит выход Б

drop_size=15 # размер
drop_velocity=3 # скорсоть
velocity_step=0.1 # шаг увеличения скорости
max_velocity=10 # максимальная скорость
max_temp=30 # максимальная температура
min_temp=-5 # минимальная температура
dtemp=0.001 # изменение температуры

drop_color="#00FFFF" # цвет капли
ice_color="#E0FFFF" # цвет градины

class drop:
	def __init__(self, x, y, canv, v=drop_velocity, v_s=velocity_step, m_v=max_velocity, r=drop_size,
				max_temp=max_temp, min_temp=min_temp, dtemp=dtemp, color=drop_color, ice_color=ice_color):
		self.is_warm=1 # температура больше нуля, или меньше
		self.x=x
		self.y=y 
		self.canv=canv
		a=random.random()*2*math.pi # рандомный угол полёта новой капли
		self.vx=v*math.sin(a)
		self.vy=v*math.cos(a)
		self.v_s=v_s
		self.m_v=m_v
		self.r=r
		self.color=color # цвет капли
		self.ice_color=ice_color # цвет градины
		self.temp=random.randint(min_temp, max_temp) # любая температура из диапазона
		self.min_temp=min_temp #
		self.dtemp=dtemp # уменьшение температуры за одну итерацию программы
		self.id=self.canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color) # форма
		self.text=self.canv.create_text(self.x, self.y, font=('arial', 18, BOLD), text=int(self.temp)) # текст на капле

	def rebound(self, v1, v2): # отскок
		v=(v1**2+v2**2)**0.5
		if (v>self.m_v): self.v_s = 0
		v1=-v1*(v+self.v_s)/v # скорость, которая отражается
		v2=v2*(v+self.v_s)/v # скорость, которая сохраняется
		return v1, v2

	def make_ice(self): # капля превращается во льдинку
		self.is_warm=0 # температура меньше нуля
		self.r=self.r*1.1 # меняется радиус
		self.canv.delete(self.id) # удаляем каплю
		self.canv.delete(self.text) # удаляем текст на капле
		self.id=self.canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.ice_color)
		self.text=self.canv.create_text(self.x, self.y, font=('arial', 18, BOLD), text = int(self.temp))

	def hittest(self, x0, y0, r0): # проверяет, сталкиваются объекты или нет
		l=((x0-self.x)**2+(y0-self.y)**2)**0.5
		return (l<=r0+self.r)

	def clean(self): # удаление объекта
		self.canv.delete(self.id)
		self.canv.delete(self.text)

	def move(self, x0, y0):
		self.temp=self.min_temp+(1-dtemp)*(self.temp-self.min_temp) # понижаем температуру
		if (self.is_warm==1 and self.temp<0): # если температар больше нуля, делает льдинкой
			self.make_ice()
		dx=self.vx
		dy=self.vy
		# проверка столкновений с 4-мя стенками
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
		self.canv.move(self.id, dx, dy) # сдвигает объект
		self.canv.move(self.text, dx, dy) # сдвигает текст
		self.canv.itemconfig(self.text, text=int(self.temp))
		self.x+=dx
		self.y+=dy