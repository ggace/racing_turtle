import turtle
from config import *
from setup import *
import keyboard

turtle.setup(width=width, height=height)

end1 = False
end2 = False
end3 = False
end4 = False
end5 = False

game_start = False

loop = True

while(loop):
    
    if(keyboard.is_pressed("s")):
        game_start = True
    elif(keyboard.is_pressed("q")):
        
        loop = False

    if(game_start):
        game_setup()
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
        game_start = False
        print()
exit()