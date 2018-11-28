'''
Created on Nov 28, 2018

@author: nw
'''
import turtle
wn = turtle.Screen()
image = "irobot.gif"
wn.addshape(image)
wn.bgcolor("beige")
Roomba = turtle.Turtle()
Roomba.shape(image)
Roomba.speed(8)
Roomba.pensize(5)

def housesquare(Roomba):
    #square that represents part of the shape of a house and fills it with color lightblue
    Roomba.fillcolor("lightblue")
    Roomba.penup()
    Roomba.setposition(-100,-25)
    Roomba.pendown()
    Roomba.pencolor("brown")
    Roomba.begin_fill()
    for i in range(4):
        Roomba.forward(200)
        Roomba.right(90)
    Roomba.end_fill()
def housetriangle(Roomba):
    #equilateral triangle that represents the roof of a house and fills it with color lightblue
    Roomba.fillcolor("lightblue")
    Roomba.begin_fill()
    for i in range(3):
        Roomba.backward(-200)
        Roomba.left(120)
    Roomba.end_fill()

def housedoor(Roomba):
    #a rectangle that represents the door of a house along with a doorknob that it fills with the color brown
    Roomba.penup()
    Roomba.setx(-10)
    Roomba.sety(-225)
    Roomba.pendown()
    Roomba.forward(25)
    Roomba.left(90)
    Roomba.forward(75)
    Roomba.left(90)
    Roomba.forward(25)
    Roomba.left(90)
    Roomba.forward(75)
    Roomba.left(90)
    Roomba.penup()
    Roomba.forward(18)
    Roomba.left(90)
    Roomba.forward(38)
    Roomba.pendown()
    Roomba.pensize(1)
    Roomba.fillcolor("brown")
    Roomba.begin_fill()
    Roomba.circle(2)
    Roomba.end_fill()

def houseatticwindow(Roomba):
    #a circle that represents the attic window of a house along with corresponding window frames
    Roomba.pensize(5)
    Roomba.left(90)
    Roomba.penup()
    Roomba.forward(18)
    Roomba.right(90)
    Roomba.forward(200)
    Roomba.right(90)
    Roomba.forward(9)
    Roomba.pendown()
    Roomba.circle(25)
    Roomba.left(90)
    Roomba.forward(50)
    Roomba.penup()
    Roomba.goto(-1,13)
    Roomba.left(90)
    Roomba.forward(25)
    Roomba.right(90)
    Roomba.forward(25)
    Roomba.right(90)
    Roomba.pendown()
    Roomba.forward(50)
    
def sun(Roomba):
    #a circle that represents the sun and fills in in with the color orange
    Roomba.penup()
    Roomba.setpos(-320,225)
    Roomba.pendown()
    Roomba.fillcolor("orange")
    Roomba.begin_fill()
    Roomba.circle(50)
    Roomba.end_fill()

def lawn(Roomba):
    #little green vertical lines that are meant to represent blades of grass that make up a lawn
    Roomba.right(90)
    Roomba.penup()
    Roomba.forward(485)
    Roomba.pendown()
    Roomba.pencolor("lightgreen")
    Roomba.forward(25)
    Roomba.left(90)
    for i in range(25):
        Roomba.forward(25)
        Roomba.left(90)
        Roomba.forward(25)
        Roomba.left(180)
        Roomba.forward(25)
        Roomba.left(90)
    Roomba.left(90)
    Roomba.forward(25)

def picture():
    #calls the functions that make up the picture
    housesquare(Roomba)
    housetriangle(Roomba)
    housedoor(Roomba)
    houseatticwindow(Roomba)
    sun(Roomba)
    lawn(Roomba)

if __name__ == '__main__':
    picture()
    
wn.exitonclick()
