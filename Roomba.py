'''
Created on Nov 28, 2018

@author: nw and jg
'''
import turtle
import random
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
# Roomba.speed(10)



def move(turtle, distance):
    turtle.speed(0)
    distance = float(distance)
    for i in range(0, abs(int(distance/2))):
        x, y = turtle.pos()
        print(x)
        print(y)
        if (-width/2 < x < width/2) and  (-height/2 < y < height/2):
            if distance < 0:
                turtle.forward(-2)
            else:           
                turtle.forward(2)
        else:
            turtle.undo()
            break

def custom(turtle):
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
        if (-width/2 < x < width/2) and  (-height/2 < y < height/2):
                turtle.forward(2)
        else:
            turtle.undo()
            turtle.setheading(current+angle)

def freeroam(turtle):
    
    # sets how long the Roomba runs
    length = float(integerbox("How long would you like the Roomba to run (in seconds)?"))
    start = time.time()
    while True:
        if time.time() > start + length:
            break
        current = turtle.heading()
        x, y = turtle.pos()
        if (-width/2 < x < width/2) and  (-height/2 < y < height/2):
                turtle.forward(2)
        else:
            turtle.undo()
            angle = random.randint(-180,180)
            turtle.setheading(current+angle) 

def complete(turtle):
    global num_uncleaned
    clean = False
    while True:
        if(num_uncleaned == 0):
            break
            
        current = turtle.heading()
        x, y = turtle.pos()
        coord = (int(x)+249,int(y)+249)
        print("current coords: ",int(coord[0]),int(coord[1]))
        for i in range(50):
            for j in range(50):
                xclean = coord[0]+i
                yclean = coord[1]+j
                if 0<=xclean<500 and 0<=yclean<500 and (i**2+j**2 <= 25**2):
                    if not clean_grid[xclean,yclean]:
                        clean_grid[xclean,yclean] = True
                        num_uncleaned-=1
        print("num of coords: ",num_uncleaned)
        print(250000-np.sum(clean_grid))
#         if(len(coordinates)<100):
#             clean = True
        if (-width/2 < x < width/2) and (-height/2 < y < height/2):
                turtle.forward(25)
        else:
            turtle.undo()
            angle = random.randint(-180,180)
            turtle.setheading(current+angle)     
    
def home(turtle, x, y):
    turtle.penup()
    turtle.speed(1)
    turtle.goto(x,y)


if __name__ == '__main__':
    
    # Optional setting: Roomba's home coordinates; default is 0,0
    
    complete(Roomba)
    
#     homeset = buttonbox(msg="Would you like to set Roomba's home coordinates or use the default settings ?", title = "Home Settings", choices = ["Custom", "Default"])
#     if homeset == "Custom":
#         homex = integerbox(msg="Roomba's home x-coordinate (-250 to 250)", lowerbound = -250, upperbound = 250)
#         homey = integerbox(msg="Roomba's home y-coordinate (-250 to 250)", lowerbound = -250, upperbound = 250)
#     else:    
#         homex = 0
#         homey = 0
#       
#     # Specify running mode for Roomba
#       
#     type = buttonbox(msg="Please choose Roomba's running mode.", title = "Running mode", choices =["Free-roam (random bump)", "Custom bump angle"])
#   
#     if type=="Free-roam (random bump)":
#         freeroam(Roomba)
#     if type =="Custom bump angle":
#         custom(Roomba)
    
    # Return Roomba to its home; final goodbyes
    home(Roomba, homex, homey)
    msgbox("Your home is now clean. Good-bye!")
    
    # Exit the program with click
    wn.exitonclick()
