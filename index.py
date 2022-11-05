import turtle
from config import *
from setup import *
from matplotlib import pyplot

turtle.setup(width=width, height=height)



end1 = False
end2 = False
end3 = False
end4 = False
end5 = False

i = 0

x = []

turtle1_x = []
turtle2_x = []
turtle3_x = []
turtle4_x = []
turtle5_x = []

def result(num):
    print(num)

while not(t1.end and t2.end and t3.end and t4.end and t5.end):
    t1_statue = t1.turtleMove()
    t2_statue = t2.turtleMove()
    t3_statue = t3.turtleMove()
    t4_statue = t4.turtleMove()
    t5_statue = t5.turtleMove()
    
    print("" if t1_statue==None else t1_statue, end="")
    print("" if t2_statue==None else t2_statue, end="")
    print("" if t3_statue==None else t3_statue, end="")
    print("" if t4_statue==None else t4_statue, end="")
    print("" if t5_statue==None else t5_statue, end="")


    x.append(i)
    turtle1_x.append(t1.runner.pos()[0])
    turtle2_x.append(t2.runner.pos()[0])
    turtle3_x.append(t3.runner.pos()[0])
    turtle4_x.append(t4.runner.pos()[0])
    turtle5_x.append(t5.runner.pos()[0])

    pyplot.plot(turtle1_x, color='r')
    pyplot.plot(turtle2_x, color='b')
    pyplot.plot(turtle3_x, color='y')
    pyplot.plot(turtle4_x, color='g')
    pyplot.plot(turtle5_x, color='k')

    pyplot.pause(0.1)

    i += 1

input()