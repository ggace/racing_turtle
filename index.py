import turtle
from config import *
from setup import *
import keyboard
import pyautogui
import winsound as sd

from matplotlib import pyplot as plt

def beepsound(frequency:int, duration:int):
    sd.Beep(frequency, duration) # winsound.Beep(frequency, duration)

turtle.setup(width=width, height=height)

end1 = False
end2 = False
end3 = False
end4 = False
end5 = False

game_start = False

loop = True

x = []
i = 0

while(loop):
    
    if(keyboard.is_pressed("s")):
        game_start = True
    elif(keyboard.is_pressed("q")):
        if(pyautogui.confirm('정말 종료하시겠습니까?') == "OK"):
            loop = False

    if(game_start):
        x = []
        y = []
        i=0

        t1.setup()
        t2.setup()
        t3.setup()
        t4.setup()
        t5.setup()

        game_setup()
        beepsound(2000, 500)
        time.sleep(0.5)
        beepsound(2000, 500)
        time.sleep(0.5)
        beepsound(2000, 500)
        time.sleep(0.5)
        beepsound(3000, 1000)



        while not(t1.end and t2.end and t3.end and t4.end and t5.end):
            
            t1_statue = t1.turtleMove()
            t2_statue = t2.turtleMove()
            t3_statue = t3.turtleMove()
            t4_statue = t4.turtleMove()
            t5_statue = t5.turtleMove()

            x.append(i)
            y.append(width/2 - 100)

            if(t1_statue!=None):
                print(t1_statue)
            if(t2_statue!=None):
                print(t2_statue)
            if(t3_statue!=None):
                print(t3_statue)
            if(t4_statue!=None):
                print(t4_statue)
            if(t5_statue!=None):
                print(t5_statue)
            
            i+=1
        print()
        plt.plot(x, y, color='#7f7f7f')
        plt.plot(x, t1.y, color='r')
        plt.plot(x, t2.y, color='b')
        plt.plot(x, t3.y, color='#ff7f0e')
        plt.plot(x, t4.y, color='g')
        plt.plot(x, t5.y, color='y')

        plt.show()

        game_start = False
exit()