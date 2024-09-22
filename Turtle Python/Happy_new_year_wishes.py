import turtle
import time 
import random

t_screen=turtle.Screen()
t_screen.setup(width=600,height=600)
t_screen.title('ANIMATED HAPPY NEW YEAR')
t_screen.bgpic("myni81.gif")

t=turtle.Turtle()

t.up()
t.speed(1)
t.hideturtle()
t.color('yellow')
t.goto(-280,170)
t.down()
t.write("HAPPY",font=('Arial',50,'normal'))

####
t.up()
t.color('blue')
t.goto(-60,90)
t.down()
t.write("NEW",font=('Arial',50,'normal'))
####
t.up()
t.color('red')
t.goto(100,-20)
t.down()
t.write("YEAR",font=('Arial',50,'normal'))
#####
t.up()
t.color('orange')
t.goto(-90,-190)
t.down()
t.write("2021",font=('Arial',70,'normal'))
######
t1=turtle.Turtle()
t1.hideturtle()
t1.speed(0)
#def circle():
    #t1.begin_fill()
    #t1.circle(40)
    #t1.color('white')
    #t1.end_fill()

#t1.up()
#t1.goto(-240,-40)
#t1.down()
#circle()

#######
t1.up()
t1.goto(150,150)
t1.down()
def fireworks():
    for i in range(45):
        t1.pencolor("yellow")
        t1.forward(50)
        t1.backward(50)
        t1.right(8)
    
fireworks()
#####
t1.up()
t1.goto(230,230)
t1.down()
def fireworks():
    for i in range(45):
        t1.pencolor("green")
        t1.forward(30)
        t1.backward(30)
        t1.right(8)
    
fireworks()
#######
t1.up()
t1.goto(100,230)
t1.down()
def fireworks():
    for i in range(45):
        t1.pencolor("white")
        t1.forward(45)
        t1.backward(45)
        t1.right(8)
    
fireworks()
######
t1.up()
t1.goto(0,270)
t1.down()
def fireworks():
    for i in range(45):
        t1.pencolor("pink")
        t1.forward(60)
        t1.backward(60)
        t1.right(8)
    
fireworks()
########
t1.up()
t1.goto(0,0)
t1.down()
def fireworks():
    for i in range(45):
        t1.pencolor("white")
        t1.forward(45)
        t1.backward(45)
        t1.right(8)
    
fireworks()
#############
t1.up()
t1.goto(-190,230)
t1.down()
def fireworks():
    for i in range(45):
        t1.pencolor("yellow")
        t1.forward(55)
        t1.backward(55)
        t1.right(8)
    
fireworks()
############
t1.up()
t1.goto(100,90)
t1.down()
def fireworks():
    for i in range(45):
        t1.pencolor("green")
        t1.forward(30)
        t1.backward(30)
        t1.right(8)
    
fireworks()
#######
t1.up()
t1.goto(-190,100)
t1.down()
def fireworks():
    for i in range(45):
        t1.pencolor("pink")
        t1.forward(35)
        t1.backward(35)
        t1.right(8)
    
fireworks()








turtle.done()












