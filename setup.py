import turtle
from config import *

t1 = turtle.Turtle()
t1.up()
t1.shape("turtle")
t1.speed(0)
t1.color("red")

t2 = turtle.Turtle()
t2.up()
t2.shape("turtle")
t2.speed(0)
t2.color("blue")

t3 = turtle.Turtle()
t3.up()
t3.shape("turtle")
t3.speed(0)
t3.color("orange")

t4 = turtle.Turtle()
t4.up()
t4.shape("turtle")
t4.speed(0)
t4.color("green")

t5 = turtle.Turtle()
t5.up()
t5.shape("turtle")
t5.speed(0)

t1.goto(-width/2+100, 200)
t2.goto(-width/2+100, 100)
t3.goto(-width/2+100, 0)
t4.goto(-width/2+100, -100)
t5.goto(-width/2+100, -200)

t1.speed(100)
t2.speed(100)
t3.speed(100)
t4.speed(100)
t5.speed(100)