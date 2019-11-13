#program file
import turtle
turtle.colormode(225)
bob=turtle.Turtle()
turtle.bgcolor("black")

bob.width(4)
bob.speed(100)

for times in range(90):
    c = (times*3,200,times*3)
    bob.color("orange")
    bob.circle(times*3)
    bob.left(90)

bob.penup()
bob.goto(0,0)
bob.pendown()

for times in range(90):
    c = (times*3,200,times*3)
    bob.color("blue")
    bob.circle(times*3)
    bob.left(90)

bob.penup()
bob.goto(0,0)
bob.pendown()

for times in range(90):
    c = (times*3,200,times*3)
    bob.color("white")
    bob.circle(times*3)
    bob.left(90)

bob.penup()
bob.goto(0,0)
bob.pendown()

for times in range(90):
    c = (times*3,200,times*3)
    bob.color("red")
    bob.circle(times*3)
    bob.left(90)

bob.penup()
bob.goto(0,0)
bob.pendown()

for times in range(90):
    c = (times*3,200,times*3)
    bob.color("silver")
    bob.circle(times*3)
    bob.left(90)

bob.penup()
bob.goto(0,0)
bob.pendown()

for times in range(90):
    c = (times*3,200,times*3)
    bob.color("black")
    bob.circle(times*3)
    bob.left(90)

bob.penup()
bob.goto(0,0)
bob.pendown()

for times in range(90):
    c = (times*3,200,times*3)
    bob.color("black")
    bob.circle(times*3)
    bob.left(90)
