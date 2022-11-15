from turtle_runner import *
from boost import *
from config import *

drawing_turtle = turtle.Turtle()

def draw_endline():

    global drawing_turtle
    
    drawing_turtle.hideturtle()
    drawing_turtle.speed(0)
    drawing_turtle.penup()
    drawing_turtle.goto(width/2-100, height/2)
    drawing_turtle.pendown()
    drawing_turtle.goto(width/2-100, -height/2)
    drawing_turtle.goto(width/2-50, -height/2)
    drawing_turtle.goto(width/2-50, height/2)

    drawing_turtle.left(360/4)

    for i in range(int(height/100)):
        drawing_turtle.fillcolor('black')
        drawing_turtle.begin_fill()
        for i in range(4):
            drawing_turtle.left(360/4)
            drawing_turtle.forward(50)
        drawing_turtle.end_fill()
        drawing_turtle.goto(drawing_turtle.pos()[0], drawing_turtle.pos()[1]-50)
        for i in range(4):
            drawing_turtle.left(360/4)
            drawing_turtle.forward(50)
        drawing_turtle.goto(drawing_turtle.pos()[0], drawing_turtle.pos()[1]-50)

    drawing_turtle.penup()
    drawing_turtle.goto(width/2, height/2)
    drawing_turtle.pendown()

    for i in range(int(height/100)):
        
        for i in range(4):
            drawing_turtle.left(360/4)
            drawing_turtle.forward(50)
        drawing_turtle.end_fill()
        drawing_turtle.goto(drawing_turtle.pos()[0], drawing_turtle.pos()[1]-50)
        drawing_turtle.fillcolor('black')
        drawing_turtle.begin_fill()
        for i in range(4):
            drawing_turtle.left(360/4)
            drawing_turtle.forward(50)
        drawing_turtle.end_fill()
        drawing_turtle.goto(drawing_turtle.pos()[0], drawing_turtle.pos()[1]-50)
    drawing_turtle.penup()

    drawing_turtle.goto(0, height/2-50)
    drawing_turtle.write("기본 : 10~30", font=("Arial", 16, "normal"))

    drawing_turtle.goto(-width/2+100, 210)
    drawing_turtle.write("부스트확률: 12%\n30~49", font=("Arial", 16, "normal"))
    drawing_turtle.goto(-width/2+100, 110)
    drawing_turtle.write("부스트확률: 10%\n40~57", font=("Arial", 16, "normal"))
    drawing_turtle.goto(-width/2+100, 10)
    drawing_turtle.write("부스트확률: 7% \n50~72", font=("Arial", 16, "normal"))
    drawing_turtle.goto(-width/2+100, -90)
    drawing_turtle.write("부스트확률: 5% \n60~90", font=("Arial", 16, "normal"))
    drawing_turtle.goto(-width/2+100, -190)
    drawing_turtle.write("부스트확률: 0.4%\n400~600", font=("Arial", 16, "normal"))

    


def game_setup():
    setup()
    t1.end = False
    t2.end = False
    t3.end = False
    t4.end = False
    t5.end = False

    t1.runner.goto(-width/2+100, 200)
    t2.runner.goto(-width/2+100, 100)
    t3.runner.goto(-width/2+100, 0)
    t4.runner.goto(-width/2+100, -100)
    t5.runner.goto(-width/2+100, -200)

    t1.runner.speed(0)
    t2.runner.speed(0)
    t3.runner.speed(0)
    t4.runner.speed(0)
    t5.runner.speed(0)

draw_endline()

boost1 = Boost(12, (30, 49))
boost2 = Boost(10, (40, 57))
boost3 = Boost(7, (50, 72))
boost4 = Boost(5, (60, 90))
boost5 = Boost(0.4, (400, 600))

t1 = Runner("red", 1, boost1)
t2 = Runner("blue", 2, boost2)
t3 = Runner("orange", 3, boost3)
t4 = Runner("green", 4, boost4)
t5 = Runner("yellow", 5, boost5)

game_setup()