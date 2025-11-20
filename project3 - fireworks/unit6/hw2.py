import turtle # importing turtle

t = turtle.Turtle() # creating turtle
t.shape("circle") # making shape circle

s = turtle.Screen() # creating screen
s.bgcolor("black") # making screen black

# preaparing
t.penup() 
t.goto(200,-200)
t.pendown()

t.shapesize(1) # changing circle size
t.color("white","red") # changing line and fill color

t.begin_fill() # creating firework base
for i in range(2):
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)

t.end_fill()

t.color("white","white") # changing color for shooting out

t.penup()
t.forward(10)
t.pendown()
t.speed(9) # setting speed
t.left(90)

for i in range(30): # drawing trajectory
    t.forward(10)
    t.left(1)

for i in range(30):
    t.forward(8)
    t.left(2)
    
turtle.done()