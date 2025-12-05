import turtle
import random

t = turtle.Turtle() # creating turtle
t.shape("circle") # making shape circle

s = turtle.Screen() 
s.setup(width=1000, height=1000) # setting a consistent screen size
s.bgcolor("black") 
s.title("Turtle Firework")

colorList = ["red", "orange", "yellow", "purple", "light blue", "light green", "pink"]

t.penup()
t.goto(-500, -350)
t.color("green", "green")
t.pendown()
t.speed(0)

t.begin_fill() # creating grass
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(150)
    t.right(90)
t.end_fill()

# preaparing
t.penup() 
t.goto(300,-300)
t.pendown()

t.speed(5)
t.shapesize(1) # changing circle size
t.color("white","red") # changing line and fill color

t.begin_fill() # creating firework base
for i in range(2):
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.right(90)
t.end_fill()

# setting up for trajectory line
t.color("white","white")
t.penup()
t.forward(20)
t.pendown()
t.left(90)

t.speed(5)

for i in range(30): # drawing trajectory
    t.forward(10)
    t.left(1)

for i in range(30):
    t.forward(8)
    t.left(1)

t.color("yellow", "yellow")
size = 1
for i in range(10):
    t.speed(3)
    size += 0.2
    t.shapesize(size)

trtls = []*36

turtle.delay(0)
for i in range(18):
    trtls.append(t.clone())
    trtls[i].speed(0)
    trtls[i].right(20*i)
    trtls[i].shapesize(0.1)
    trtls[i].pensize(2)
    trtls[i].pencolor(random.choice(colorList))

for j in range(50):
    for i in range(18):
        trtls[i].forward(3)


turtle.done()