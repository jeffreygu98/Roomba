'''
Created on Nov 28, 2018

@author: nw
'''
import turtle
wn = turtle.Screen()
wn.bgcolor("beige")
Nicolas = turtle.Turtle()
Nicolas.shape("turtle")
Nicolas.speed(8)
Nicolas.pensize(5)

def housesquare(Nicolas):
    #square that represents part of the shape of a house and fills it with color lightblue
    Nicolas.fillcolor("lightblue")
    Nicolas.penup()
    Nicolas.setposition(-100,-25)
    Nicolas.pendown()
    Nicolas.pencolor("brown")
    Nicolas.begin_fill()
    for i in range(4):
        Nicolas.forward(200)
        Nicolas.right(90)
    Nicolas.end_fill()

def housetriangle(Nicolas):
    #equilateral triangle that represents the roof of a house and fills it with color lightblue
    Nicolas.fillcolor("lightblue")
    Nicolas.begin_fill()
    for i in range(3):
        Nicolas.backward(-200)
        Nicolas.left(120)
    Nicolas.end_fill()

def housedoor(Nicolas):
    #a rectangle that represents the door of a house along with a doorknob that it fills with the color brown
    Nicolas.penup()
    Nicolas.setx(-10)
    Nicolas.sety(-225)
    Nicolas.pendown()
    Nicolas.forward(25)
    Nicolas.left(90)
    Nicolas.forward(75)
    Nicolas.left(90)
    Nicolas.forward(25)
    Nicolas.left(90)
    Nicolas.forward(75)
    Nicolas.left(90)
    Nicolas.penup()
    Nicolas.forward(18)
    Nicolas.left(90)
    Nicolas.forward(38)
    Nicolas.pendown()
    Nicolas.pensize(1)
    Nicolas.fillcolor("brown")
    Nicolas.begin_fill()
    Nicolas.circle(2)
    Nicolas.end_fill()

def houseatticwindow(Nicolas):
    #a circle that represents the attic window of a house along with corresponding window frames
    Nicolas.pensize(5)
    Nicolas.left(90)
    Nicolas.penup()
    Nicolas.forward(18)
    Nicolas.right(90)
    Nicolas.forward(200)
    Nicolas.right(90)
    Nicolas.forward(9)
    Nicolas.pendown()
    Nicolas.circle(25)
    Nicolas.left(90)
    Nicolas.forward(50)
    Nicolas.penup()
    Nicolas.goto(-1,13)
    Nicolas.left(90)
    Nicolas.forward(25)
    Nicolas.right(90)
    Nicolas.forward(25)
    Nicolas.right(90)
    Nicolas.pendown()
    Nicolas.forward(50)
    
def sun(Nicolas):
    #a circle that represents the sun and fills in in with the color orange
    Nicolas.penup()
    Nicolas.setpos(-320,225)
    Nicolas.pendown()
    Nicolas.fillcolor("orange")
    Nicolas.begin_fill()
    Nicolas.circle(50)
    Nicolas.end_fill()

def lawn(Nicolas):
    #little green vertical lines that are meant to represent blades of grass that make up a lawn
    Nicolas.right(90)
    Nicolas.penup()
    Nicolas.forward(485)
    Nicolas.pendown()
    Nicolas.pencolor("lightgreen")
    Nicolas.forward(25)
    Nicolas.left(90)
    for i in range(25):
        Nicolas.forward(25)
        Nicolas.left(90)
        Nicolas.forward(25)
        Nicolas.left(180)
        Nicolas.forward(25)
        Nicolas.left(90)
    Nicolas.left(90)
    Nicolas.forward(25)

def picture():
    #calls the functions that make up the picture
    housesquare(Nicolas)
    housetriangle(Nicolas)
    housedoor(Nicolas)
    houseatticwindow(Nicolas)
    sun(Nicolas)
    lawn(Nicolas)

if __name__ == '__main__':
    picture()
    
wn.exitonclick()