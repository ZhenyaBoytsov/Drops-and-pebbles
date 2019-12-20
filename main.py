#import balls
import frog
import math
import tkinter as tk
import sys
import tkinter.simpledialog
import pickle
import os.path
import random 

class MainWindow(tk.Frame):
    
    username = ''
    userresult = 0
    result = {}
    timer = 10

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        super()._root().geometry('800x600')  
        self.topFrame = tk.Frame(super()._root())
        self.lblUserName = tk.Label(self.topFrame)
        self.lblBestResult = tk.Label(self.topFrame)
        self.lblTimer = tk.Label(self.topFrame)
        self.topFrame.pack(side=tk.TOP, fill=tk.BOTH)        
        self.lblUserName.pack(side = tk.LEFT)        
        self.lblBestResult.pack(side = tk.LEFT)
        self.lblTimer.pack(side = tk.RIGHT)

        self.canv = tk.Canvas(super()._root(), bg='white')        
        self.canv.pack(fill=tk.BOTH, expand=True)
                
        self.mainmenu = tk.Menu(super()._root())
        super()._root().config(menu=self.mainmenu)
        self.mainmenu.add_command(label='Начать игру', command=self.startgame)
        self.mainmenu.add_command(label='Результаты', command=self.viewresult)
        self.mainmenu.add_command(label='Выход', command=self.endgame)

                    
    def update_timer(self):        
        self.timer+=-1
        self.lblTimer.configure(text="Осталось: " + str(self.timer) + " секунд", font="Arial 16")
        if (self.timer > 0):
            super()._root().after(1000, self.update_timer)
        else:
            self.writeresult('datafile.pkl', random.randrange(1,100))                 

    def startgame(self):        
        self.username = tk.simpledialog.askstring('', 'Введите имя:', parent=super()._root())
        if len(self.username) > 0:
            #загружаем предыдущие результаты
            self.result = self.readresult('datafile.pkl')                     
            self.lblUserName.config(text='Игрок: ' + self.username, font="Arial 16")            
            if self.username in self.result:
                self.lblBestResult.config(text='    Лучший результат: ' + str(self.result[self.username]), font="Arial 16")
            else:
                self.lblBestResult.config(text='    Лучший результат: 0', font="Arial 16")

            #запускаем игру
            
            self.update_timer()

                                
    def viewresult(self):
        win = tk.Toplevel(super()._root())
        win.geometry('400x300')
        win.title('Результаты')
        bottomFrame = tk.Frame(win)
        bottomFrame.pack(side = tk.BOTTOM, fill=tk.BOTH)
        lb = tk.Listbox(win)
        lb.configure(font="Courier 8")
        lb.pack(fill=tk.BOTH, expand=True)
        btnClose = tk.Button(bottomFrame, text='Закрыть', command=win.destroy)
        btnClose.pack()

        self.result = self.readresult('datafile.pkl')
       
        l = list(self.result.items())
        l.sort(key = lambda i:i[1], reverse = True)
        for obj in l:
            lb.insert(tk.END, '{0:25}{1:10}'.format(str(obj[0]), str(obj[1])))

    def readresult(self, filename):
        result = {}
        if os.path.exists(filename) == True: 
            file = open(filename, 'rb')
            result = pickle.load(file)
            file.close()
            return result
        
        return result
                          
    def writeresult(self, filename, newresult):
        if os.path.exists(filename) == False: 
            file = open(filename, 'wb')                    
            d = {}
            pickle.dump(d, file)
            file.close()
        
        if len(self.username) > 0:
            if self.username not in self.result:
                self.result[self.username] = newresult
            elif newresult > self.result[self.username]:
                self.result[self.username] = newresult
        
            file = open(filename, 'wb')
            pickle.dump(self.result, file)
            file.close()

    def endgame(self):
        self.writeresult('datafile.pkl', random.randrange(1,100))# временный вывод результата  
        super()._root().destroy()

    
if __name__ == '__main__':        
    MyGame = MainWindow()
    MyGame.master.title("Игра")      
    MyGame.master.geometry('800x600')        
    MyGame.mainloop()   





