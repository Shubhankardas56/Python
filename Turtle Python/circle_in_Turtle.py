import turtle
import math
import random
t1=turtle.Turtle()
r=50
rand=["red","green","blue","violet","grey","orange","yellow"]
cont=True
while cont:
    for i in range(18):
        t1.speed(0)
        t1.begin_fill()
        random_color=random.choice(rand)
        t1.fillcolor(random_color)
        t1.circle(r)
        t1.right(20)
        t1.end_fill()
    choice=input("press y to continue: ")
    if choice=='y':
        continue
    else:
        break