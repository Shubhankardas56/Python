import turtle
import time
import random
# setup game screen
wn=turtle.Screen()
wn.title('Snake Game by SD')
wn.setup(width=600,height=600)
wn.bgcolor('green')
wn.tracer(0) # prevent screen update, we have to update manually
# built snake head
head=turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('black')
head.penup()
head.goto(0,0)
head_direction='stop'   # declaring global variable
delay=0.1
# move function
def move():
    if head_direction =="up":
        y=head.ycor()  # return the y cordinate
        head.sety(y+20)
    if head_direction =="down":
        y=head.ycor()   # return the y cordinate
        head.sety(y-20)
    if head_direction =="left":
        x=head.xcor()    # return the x cordinate
        head.setx(x-20)
    if head_direction =="right":
        x=head.xcor()    # return the x cordinate
        head.setx(x+20)
# move in a one direction
def go_up():
    global head_direction
    if head_direction !='down':
        head_direction='up'
def go_down():
    global head_direction
    if head_direction !='up':
        head_direction='down'
def go_left():
    global head_direction
    if head_direction !='right':
        head_direction='left'
def go_right():
    global head_direction
    if head_direction !='left':
        head_direction='right'
is_push=False
def push():
    global is_push
    if is_push==True:
        is_push=False
    else:
        is_push=True
# keyboard input
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(push, "space")

# Food for snake
food=turtle.Turtle()
food.speed(0)
food.color('red')
food.shapesize(0.6,0.6)
food.shape('circle')
food.penup()
food.goto(0,150)
# Body of snake
segment=[]
# game mainloop
while True:
    wn.update()
    if not is_push:
        # moving the food to random position
        if head.distance(food)<17: 
            food_x=random.randint(-285,285)
            food_y=random.randint(-285,270)
            food.goto(food_x,food_y)
            # adding new segment
            new_segment=turtle.Turtle()
            new_segment.speed(0)
            new_segment.color('yellow')
            new_segment.shape('circle')
            new_segment.shapesize(0.8,0.8)
            new_segment.penup()
            segment.append(new_segment)
        # move the end segment first in reverse order
        for i in range(len(segment)-1,0,-1):
            x=segment[i-1].xcor()
            y=segment[i-1].ycor()
            segment[i].goto(x,y)
        if len(segment)>0:
            x=head.xcor()
            y=head.ycor()
            segment[0].goto(x,y)
        # colide with board
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0) 
            head_direction="stop"
            #clear the segments
            for sg in segment:
                sg.goto(1000,1000)
            segment.clear()
        move()
        time.sleep(delay)
    else:
        wn.update()
wn.mainloop()


