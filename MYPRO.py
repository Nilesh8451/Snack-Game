import random
import sys
import time
import pygame
from Tkinter import *
import tkMessageBox

class Snake():
    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = 'RIGHT'
        self.changeDirectionTo = self.direction

    def changeDirtTo(self,dir):
        if dir=="RIGHT" and not self.direction=="LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self,foodpos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10
        self.body.insert(0,list(self.position))
        if self.position == foodpos:
            return 1
        else:
            self.body.pop()
            return 0

    def checkcollision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1
        for bodypart in self.body[1:]:
            if self.position == bodypart:
                return 1
        return 0

    def getHeadPos(self):
        return self.position

    def getbody(self):
        return self.body

class FoodMaker():
    def __init__(self):
        self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self,b):
        self.isFoodOnScreen = b


def MAIN():
 v1=v.get()
 if(v1==1):
    v1=15
    print "LEVEL:-EASY"
 elif(v1==2):
    v1=25
    print "LEVEL:-MEDIUM"
 else:
    v1=40
    print "LEVEL:-HIGH"

 window = pygame.display.set_mode((500,500))
 pygame.display.set_caption("SNAKE")
 fps = pygame.time.Clock()

 score = 0
 snake = Snake()
 foodMaker = FoodMaker()

 def gameOver():
    pygame.quit()

    print "Your Score is:-",score
    sys.exit()


 while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirtTo('RIGHT')
            if event.key == pygame.K_UP:
                snake.changeDirtTo('UP')
            if event.key == pygame.K_DOWN:
                snake.changeDirtTo('DOWN')
            if event.key == pygame.K_LEFT:
                snake.changeDirtTo('LEFT')
    foodPos = foodMaker.spawnFood()
    if(snake.move(foodPos)==1):
        score+=10
        foodMaker.setFoodOnScreen(False)
    window.fill(pygame.Color(225,225,225))
    for pos in snake.getbody():
        pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(window, pygame.Color(225,0,0), pygame.Rect(foodPos[0],foodPos[1],10, 10))
    if(snake.checkcollision()==1):
        gameOver()

    pygame.display.set_caption("SNAKE.... | Score: "+ str(score))
    pygame.display.flip()

    fps.tick(v1)

def NEW():

    w=Tk()
    name1=name.get()
    print "PLAYER :-",name1
    w.title('START PAGE.....')
    w.configure(background='blue')
    l1=Label(w,text='SNAKE GAME',bg="red",font="Verdana 25 bold")
    l1.pack(side=TOP)
    l2=Button(w,text="PLAY NOW",fg="blue",bg="green",command=MAIN)
    l2.pack(ipadx=20,ipady=15,padx=100,pady=100)
    l3=Button(w,text="EXIT",fg="blue",bg="yellow",command=quit)
    l3.pack(ipadx=20,ipady=15,padx=70,pady=70)

    w.mainloop()



w1=Tk()
w1.title('REGISTER')
w1.configure(background='blue')

l1=Label(w1,text='REGISTER',bg="red",font="Verdana 20 bold")
l1.pack(side=TOP)
name=StringVar()
v=IntVar()
l1=Label(w1,text='ENTER NAME',bg="yellow",fg="red",font="verdana 10 bold")
l1.pack(ipadx=20,ipady=15,padx=10,pady=10)
l2=Entry(w1,textvariable=name,font="verdana 20 bold")
l2.pack(ipadx=10,ipady=10,padx=100,pady=10)
l1=Label(w1,text='Select the level of game',bg="yellow",fg="red",font="verdana 10 bold")
l1.pack(ipadx=20,ipady=15,padx=100,pady=10)
r1=Radiobutton(w1,text="EASY",variable=v,value=1,fg="red",font="verdana 10 bold")
r1.pack(ipadx=5,ipady=5,padx=100,pady=10)
r1=Radiobutton(w1,text="MEDIUM",variable=v,value=2,fg="red",font="verdana 10 bold")
r1.pack(ipadx=5,ipady=5,padx=100,pady=10)
r1=Radiobutton(w1,text="HIGH",variable=v,value=3,fg="red",font="verdana 10 bold")
r1.pack(ipadx=5,ipady=5,padx=100,pady=10)
l3=Button(w1,text="GO",fg="blue",bg="yellow",font="verdana 15 bold",command=NEW)
l3.pack(ipadx=20,ipady=15,padx=10,pady=10)
w1.mainloop()