import turtle # importing turtle

t = turtle.Turtle()

def polygon(side, length, color): # defining function
    angle = (360/side) # calculating exterior angle
    
    try:
        t.color(color, color)
    except t.TurtleGraphicsError:
        print("please enter a valid color name")
        return

    t.begin_fill()
    for i in range(side): # setting up for loop
        t.forward(length)
        t.right(angle)
    t.end_fill()

side = int(input("enter the number of sides")) # input number of sides
length = int(input("enter the lenght of each side")) # input lenght of sides
color = (input("enter the color of your shape")).strip() # input color


polygon(side, length, color) # calling function

turtle.done()