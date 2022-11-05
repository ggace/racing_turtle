from turtle_runner import *
from config import *

def draw_endline():
    
    drawing_turgle = turtle.Turtle()

    drawing_turgle.hideturtle()
    drawing_turgle.speed(0)
    drawing_turgle.penup()
    drawing_turgle.goto(width/2-100, height/2)
    drawing_turgle.pendown()
    drawing_turgle.goto(width/2-100, -height/2)
    drawing_turgle.goto(width/2-50, -height/2)
    drawing_turgle.goto(width/2-50, height/2)

    drawing_turgle.left(360/4)

    for i in range(int(height/100)):
        drawing_turgle.fillcolor('black')
        drawing_turgle.begin_fill()
        for i in range(4):
            drawing_turgle.left(360/4)
            drawing_turgle.forward(50)
        drawing_turgle.end_fill()
        drawing_turgle.goto(drawing_turgle.pos()[0], drawing_turgle.pos()[1]-50)
        for i in range(4):
            drawing_turgle.left(360/4)
            drawing_turgle.forward(50)
        drawing_turgle.goto(drawing_turgle.pos()[0], drawing_turgle.pos()[1]-50)

    drawing_turgle.penup()
    drawing_turgle.goto(width/2, height/2)
    drawing_turgle.pendown()

    for i in range(int(height/100)):
        
        for i in range(4):
            drawing_turgle.left(360/4)
            drawing_turgle.forward(50)
        drawing_turgle.end_fill()
        drawing_turgle.goto(drawing_turgle.pos()[0], drawing_turgle.pos()[1]-50)
        drawing_turgle.fillcolor('black')
        drawing_turgle.begin_fill()
        for i in range(4):
            drawing_turgle.left(360/4)
            drawing_turgle.forward(50)
        drawing_turgle.end_fill()
        drawing_turgle.goto(drawing_turgle.pos()[0], drawing_turgle.pos()[1]-50)
draw_endline()

t1 = Runner("red", 1)
t2 = Runner("blue", 2)
t3 = Runner("orange", 3)
t4 = Runner("green", 4)
t5 = Runner("yellow", 5)

t1.runner.goto(-width/2+100, 200)
t2.runner.goto(-width/2+100, 100)
t3.runner.goto(-width/2+100, 0)
t4.runner.goto(-width/2+100, -100)
t5.runner.goto(-width/2+100, -200)

t1.runner.speed(100)
t2.runner.speed(100)
t3.runner.speed(100)
t4.runner.speed(100)
t5.runner.speed(100)

