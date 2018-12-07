'''
Created on Nov 28, 2018

@author: nw and jg
'''
import turtle
import random
import math
import time
from easygui import *
import numpy as np

width = 500.0
height = 500.0
clean_grid = np.zeros((500,500),dtype = np.bool)
print(clean_grid.shape)
num_uncleaned = int(width*height)

wn = turtle.Screen()
wn.setup(width, height)
image = "irobot.gif"
wn.addshape(image)
wn.bgcolor("sienna")
Roomba = turtle.Turtle()
Roomba.pencolor("white")
Roomba.pensize(50)
Roomba.shape(image)
Roomba.speed(0)

def custom(turtle):
    global num_uncleaned
    # sets the angle of movement
    angle = float(integerbox(msg="Please put the angle (-180 to 180) you wish the Roomba to travel with.", lowerbound = -180, upperbound = 180))
    
    # sets how long the Roomba runs
    length = float(integerbox("How long would you like the Roomba to run (in seconds)?"))
    start = time.time()
    while True:
        if time.time() > start + length:
            break
        current = turtle.heading()
        x, y = turtle.pos()
        coord = (int(x)+249,int(y)+249)
        print("current coords: ",int(coord[0]),int(coord[1]))
        for i in range(50):
            for j in range(50):
                xclean = coord[0]+i
                yclean = coord[1]+j
                if 0<=xclean<500 and 0<=yclean<500 and (i**2+j**2 <= 30**2):
                    if not clean_grid[xclean,yclean]:
                        clean_grid[xclean,yclean] = True
                        num_uncleaned-=1
        print("num of coords: ",num_uncleaned)
        if (-width/2 < x < width/2) and  (-height/2 < y < height/2):
                turtle.forward(2)
        else:
            turtle.undo()
            turtle.setheading(current+angle)
    
    # Return Roomba to its home; final goodbyes
    home(Roomba, homex, homey)
    msgbox("Roomba has cleaned "+str(int((((250000-num_uncleaned)/250000)*100)))+"% of your home in "+str(int(length))+" seconds. Good-bye!")

def freeroam(turtle):
    global num_uncleaned
    # sets how long the Roomba runs
    length = float(integerbox("How long would you like the Roomba to run (in seconds)?"))
    start = time.time()
    while True:
        if time.time() > start + length:
            break
        current = turtle.heading()
        x, y = turtle.pos()
        coord = (int(x)+249,int(y)+249)
        print("current coords: ",int(coord[0]),int(coord[1]))
        for i in range(50):
            for j in range(50):
                xclean = coord[0]+i
                yclean = coord[1]+j
                if 0<=xclean<500 and 0<=yclean<500 and (i**2+j**2 <= 30**2):
                    if not clean_grid[xclean,yclean]:
                        clean_grid[xclean,yclean] = True
                        num_uncleaned-=1
        print("num of coords: ",num_uncleaned)
        if (-width/2 < x < width/2) and  (-height/2 < y < height/2):
                turtle.forward(2)
        else:
            turtle.undo()
            angle = random.randint(-180,180)
            turtle.setheading(current+angle) 
    
    # Return Roomba to its home; final goodbyes
    home(Roomba, homex, homey)
    msgbox("Roomba has cleaned "+str(int((((250000-num_uncleaned)/250000)*100)))+"% of your home in "+str(int(length))+" seconds. Good-bye!")

def complete(turtle):
    global num_uncleaned
    clean = False
    cleanage = integerbox("What percent of the floor would you like Roomba to clean (0-95)", lowerbound = 0, upperbound = 95)
    start = time.time()
    while True:
        if(int((((250000-num_uncleaned)/250000)*100)) > (cleanage-1)):
            break
                
        current = turtle.heading()
        x, y = turtle.pos()
        coord = (int(x)+249,int(y)+249)
        print("current coords: ",int(coord[0]),int(coord[1]))
        for i in range(50):
            for j in range(50):
                xclean = coord[0]+i
                yclean = coord[1]+j
                if 0<=xclean<500 and 0<=yclean<500 and (i**2+j**2 <= 30**2):
                    if not clean_grid[xclean,yclean]:
                        clean_grid[xclean,yclean] = True
                        num_uncleaned-=1
        print("num of coords: ",num_uncleaned)
#         if(len(coordinates)<100):
#             clean = True
        if (-width/2 < x < width/2) and (-height/2 < y < height/2):
                turtle.forward(1)
        else:
            turtle.undo()
            angle = random.randint(-180,180)
            turtle.setheading(current+angle)     
    end = time.time()
    
    # Return Roomba to its home; final goodbyes
    home(Roomba, homex, homey)
    msgbox("Roomba has cleaned "+str(int((((250000-num_uncleaned)/250000)*100)))+"% of your home in "+str(int(end-start))+" seconds. Good-bye!")

def home(turtle, x, y):
    turtle.penup()
    turtle.speed(1)
    turtle.goto(x,y)


if __name__ == '__main__':
    
    # Optional setting: Roomba's home coordinates; default is 0,0
    
    homeset = buttonbox(msg="Would you like to set Roomba's home coordinates or use the default settings ?", title = "Home Settings", choices = ["Custom", "Default"])
    if homeset == "Custom":
        homex = integerbox(msg="Roomba's home x-coordinate (-250 to 250)", lowerbound = -250, upperbound = 250)
        homey = integerbox(msg="Roomba's home y-coordinate (-250 to 250)", lowerbound = -250, upperbound = 250)
    else:    
        homex = 0
        homey = 0
       
    # Specify running mode for Roomba
       
    type = buttonbox(msg="Please choose Roomba's running mode.", title = "Running mode", choices =["Free-roam (random bump)", "Custom bump angle", "Custom percentage"])
   
    if type=="Free-roam (random bump)":
        freeroam(Roomba)
    if type =="Custom bump angle":
        custom(Roomba)
    if type == "Custom percentage":
        complete(Roomba)
    
    # Exit the program with click
    wn.exitonclick()
