import turtle
from config import *
from setup import *
import random

turtle.setup(width=width, height=height)

def turtleMove(turtle: turtle):
    if(turtle.pos()[0] <= width/2 - 100):
        turtle.forward(random.randint(10, 50))
        return False

    return True

end1 = False
end2 = False
end3 = False
end4 = False
end5 = False

def result(num):
    print(num)

while not(end1 and end2 and end3 and end4 and end5):
    if(not end1):
        if turtleMove(t1):
            end1 = True
            result(1)

    if(not end2):
        if turtleMove(t2):
            end2 = True
            result(2)
    
    if(not end3):
        if turtleMove(t3):
            end3 = True
            result(3)
    
    if(not end4):
        if turtleMove(t4):
            end4 = True
            result(4)
    
    if(not end5):
        if turtleMove(t5):
            end5 = True
            result(5)
