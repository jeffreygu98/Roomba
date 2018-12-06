'''
Created on Nov 28, 2018

@author: nw
'''
import turtle
import random
import time
from easygui import *

width = 500.0
height = 500.0
xhistory = [0]*551
coordinates = []
for i in range(-250,251):
    for j in range(-250,251):
        coordinates.append((i,j))
yhistory = [0]*551

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
    
    while True:
        if (coordinates.count(0) == 250000):
            break 
        current = turtle.heading()
        x, y = turtle.pos()
        coord = (x,y)
#         for i in range((int(x)+240),(int(x)+261)):
#             xhistory[i] = 1
#         for i in range((int(y)+240),(int(y)+261)):
#             yhistory[i] = 1
        idx = coordinates.index(coord)
        coordinates[idx] = 0
        print (coordinates)
        if (-width/2 < x < width/2) and  (-height/2 < y < height/2):
                turtle.forward(1)
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
