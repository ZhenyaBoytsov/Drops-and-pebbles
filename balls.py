import main
import tkinter as tk
import math
import time
import random
import sys
import pickle

colors=['red','orange','yellow','green','cyan','blue','violet']

# задание переменных для подсчёта очков и объектов для отображения счёта очков
count=0
cou=Label(root, font=("Comic Sans MS", 24, "bold"))
cou.place(x=0.5, y=0.5)
cou['text']=count
cou.pack()

def time_counter():
	interval=interval+1

class Precipitation():
	def __init__(self, canv, x0, y0, x, y, r, v, a, t, sof=0, s=0):
		self.x0=x0
		self.y0=y0
		self.x=x
		self.y=y
		self.radius=r
		self.velocity=v
		self.angle=a
		self.temperature=t
		self.sign_of_life=sof
		self.signal=s
		self.canvas=canv
		#self.ball=canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)

class Drops(Precipitation):
	def __init__(self, canv, x0, y0, x, y, r, v, a, t, sof=0, s=0):
		super().__init__(canv, x0, y0, x, y, r, v, a, t, sof, s)
		self.ball=canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
	def sign_of_life(self):
		self.sof=1
		canv.delete(self.drop)
	#def game_score_increase
		#if sign_of_life=0
			#create_a_new_drop()

class Hailstones(Precipitation):
	def __init__(elf, canv, x0, y0, x, y, r, v, a, t, sof=0, s=0):
		super().__init__(canv, x0, y0, x, y, r, v, a, t, sof, s)
		self.ball=canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
	def sign_of_life(self):
		self.sof=1
		canv.delete(self.drop)

drops_list=[]
hailstones_list=[]

def create_drops(): # метод создания n капель и добавления в массив
	for i in range(n):
		# выбор рандомных значений атрибутов капель
		x=x0=rnd(100, 700)
		y=y0=rnd(100, 500)
		r=rnd(30, 50)
		v=rnd(100, 500)
		a=rnd(0, int(2*math.pi*100000))
		t=rnd(100, 500)
		drops_list.append(Drop(canv, x0, y0, x, y, r, v, a, t))
		move_drop(i)

def create_hailstones(): # метод создания n градин и добавления в массив
	for j in range(n):
		# выбор рандомных значений атрибутов градин
		x=x0=rnd(100,700)
		y=y0=rnd(100,500)
		r=rnd(10, 20)
		v=rnd(100, 500)
		a=rnd(0, int(2*math.pi*100000))
		t=rnd(100, 500)
		hailstones_list.append(Hailstone(canv, x0, y0, x, y, r, v, a, t))
		move_hailstone(j)

def new_drop(i): # метод создания капель, которые идут на замену i элемента в массив
	# выбор рандомных значений атрибутов капель
	x=x0=rnd(100, 700) #выбор рандомных значений капли
	y=y0=rnd(100, 500)
	r=rnd(30, 50)
	v=rnd(100, 500)
	a=rnd(0, int(2*math.pi*100000))
	drops_list[i]=Drops(canv, x0, y0, x, y, r, v, a, t)
	move_drop(i)

def new_hailstone(j): # метод создания градин, которые идут на замену j элемента в массив
	# выбор рандомных значений атрибутов градин
	x=x0=rnd(100, 700) #выбор рандомных значений градины
	y=y0=rnd(100, 500)
	r=rnd(30, 50)
	v=rnd(100, 500)
	a=rnd(0, int(2*math.pi*100000))
	hailstones_list[j]=Hailstones(canv, x0, y0, x, y, r, v, a, t)
	move_hailstone(j)

def move_ball(i): # метод движения шаров
	if balls_list[i].kf!=1:
		balls_list[i].flag+=1
		dx=dy=0
		dx=balls_list[i].v*math.cos(balls_list[i].a/100000)/100
		dy=-balls_list[i].v*math.sin(balls_list[i].a/100000)/100
		balls_list[i].x+=dx
		balls_list[i].y+=dy
		canv.move(balls_list[i].ball, dx, dy)
		rebound_ball(i)
		root.after(10, move_ball, i)
	else:
		new_ball(i)

def move_ball(j): # метод движения шаров
	if balls_list[i].kf!=1:
		balls_list[i].flag+=1
		dx=dy=0
		dx=balls_list[i].v*math.cos(balls_list[i].a/100000)/100
		dy=-balls_list[i].v*math.sin(balls_list[i].a/100000)/100
		balls_list[i].x+=dx
		balls_list[i].y+=dy
		canv.move(balls_list[i].ball, dx, dy)
		rebound_ball(i)
		root.after(10, move_ball, j)
	else:
		new_ball(j)

def rebound_drop(i): # метод отскока шара
	if (drops_list[i].x-drops_list[i].r<=2) or (800-(drops_list[i].x+drops_list[i].r)<=2):
		drops_list[i].a=100000*(math.pi-drops_list[i].a/100000)
	if (drops_list[i].y-drops_list[i].r<=2) or (600-(drops_list[i].y+drops_list[i].r)<=2):
		drops_list[i].a=100000*(2*math.pi-drops_list[i].a/100000)

def rebound_hailstone(j): # метод отскока шара
	if (hailstones_list=[j].x-hailstones_list=[j].r<=2) or (800-(hailstones_list=[j].x+hailstones_list=[j].r)<=2):
		hailstones_list=[j].a=100000*(math.pi-hailstones_list=[j].a/100000)
	if (hailstones_list=[j].y-hailstones_list=[j].r<=2) or (600-(hailstones_list=[j].y+hailstones_list=[j].r)<=2):
		hailstones_list=[j].a=100000*(2*math.pi-hailstones_list=[j].a/100000)

def click(event): # функция обработки события нажатия на левую кнопку мыши
	for i in range(n):
		if ((event.x-drops_list[i].x)**2 + (event.y-drops_list[i].y)**2) <= drops_list[i].r**2 and drops_list[i].kf!=1:
			global count
			count+=1
			cou['text']=count # счётчик нажатий на шарики
			drops_list[i].kill() # метод ball, который отмечает, что шарик "убит"
			new_ball(i)
	for j in range(n):
		if ((event.x-hailstones_list=[j].x)**2 + (event.y-hailstones_list=[j].y)**2) <= hailstones_list=[j].r**2 and hailstones_list=[j].kf!=1:
			global count
			count+=1
			cou['text']=count # счётчик нажатий на шарики
			hailstones_list=[j].kill() # метод ball, который отмечает, что шарик "убит"
			new_ball(j)

t=Timer(1.0, time_counter)
t.start() #через 1 секунду выполнится функция счётчика времени

canv.bind('<Button-1>', click)
create_drops()
create_hailstones()