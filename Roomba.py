'''
Created on Nov 28, 2018

@author: nw
'''
import turtle
import time
from easygui import *

width = 500.0
height = 500.0

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

def infinite(turtle, angle, timer, length):
    while True:
        if time.time() > timer + length:
            break
        current = turtle.heading()
        x, y = turtle.pos()
        if (-width/2 < x < width/2) and  (-height/2 < y < height/2):
                turtle.forward(2)
        else:
            turtle.undo()
            turtle.setheading(current+angle)       
     
def home(turtle, x, y):
    turtle.penup()
    turtle.speed(1)
    turtle.goto(x,y)


if __name__ == '__main__':
    # sets the angle of movement
    angle = float(integerbox("Please put the angle you wish the Roomba to travel with."))
    
    # sets how long the Roomba runs
    length = float(integerbox("How long would you like the Roomba to run (in seconds)?"))
    
    # Optional setting: Roomba's home coordinates; default is 0,0
    homex = 0
    homey = 0
    homex = integerbox(msg="Roomba's home x-coordinate (-250 to 250)", lowerbound = -250, upperbound = 250)
    homey = integerbox(msg="Roomba's home y-coordinate (-250 to 250)", lowerbound = -250, upperbound = 250)
    
    # set timer start
    start = time.time()
    
    # Roomba run program
    infinite(Roomba, angle, start, length)
    
    # Return Roomba to its home
    home(Roomba, homex, homey)
    
    # Exit the program with click
    wn.exitonclick()
