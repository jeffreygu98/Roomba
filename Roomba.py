'''
Created on Nov 28, 2018

@author: nw
'''
import turtle
width = 500.0
height = 500.0

wn = turtle.Screen()
wn.setup(width, height)
image = "irobot.gif"
wn.addshape(image)
wn.bgcolor("sienna")
Roomba = turtle.Turtle()
Roomba.pencolor("white")
Roomba.pensize(15)
Roomba.shape(image)
Roomba.speed(10)

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

def infinite(turtle):
    while True:
        current = turtle.heading()
        x, y = turtle.pos()
        if (-width/2 < x < width/2) and  (-height/2 < y < height/2):
                turtle.forward(2)
        else:
            turtle.undo()
            turtle.tiltangle(current+34)
            turtle.setheading(current+34)       
     
    

def lawn(Roomba):
    #little green vertical lines that are meant to represent blades of grass that make up a lawn
    infinite(Roomba)
#     Roomba.left(2)
#     move(Roomba,1200)

def picture():
    #calls the functions that make up the picture   
    lawn(Roomba)

if __name__ == '__main__':
    picture()
    
wn.exitonclick()
