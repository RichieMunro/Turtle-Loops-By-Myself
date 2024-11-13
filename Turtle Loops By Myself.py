import turtle
wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Exercise 6 Triangle Loop")

richie = turtle.Turtle()
richie.color("blue")
richie.pensize(7) 

for f in [richie.forward(50), richie.left(120), richie.forward(50), richie.left(120), richie.forward(50), richie.left(120)]:
    triangle = richie
    print(triangle) 

richie.penup()
richie.forward(100)
richie.pendown()

for f in [richie.forward(50), richie.left(120), richie.forward(50), richie.left(120), richie.forward(50), richie.left(120)]:
    triangle = richie
    print(triangle) 

richie.penup()
richie.forward(100)
richie.pendown()

for f in [richie.forward(50), richie.left(90), richie.forward(50), richie.left(90), richie.forward(50), richie.left(90), richie.forward(50),richie.left(90)]:
    square = richie
    print(square)

wn.mainloop