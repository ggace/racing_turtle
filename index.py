import turtle
from config import *
from setup import *
import keyboard
import pyautogui
import winsound as sd

from matplotlib import pyplot as plt

import socket

def beepsound(frequency:int, duration:int):
    sd.Beep(frequency, duration) # winsound.Beep(frequency, duration)

def list_to_str(lists):
    text = ""
    for s in lists:
        text += s + " "
    
    return text

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

with socket.socket() as sock:
    sock.connect(('127.0.0.1', 7788))
    while loop:
        res = sock.recv(1024)
        print(f"SERVER> {res.decode()}")
        result_data = res.decode().split("/")
        if(res.decode() == "finish"):
            print("\nSYSTEM> socket server was closed")
            print("SYSTEM> disconnecting from server\n")
            sock.close()
            loop = False
            break
        elif(result_data[0] == "change"):
            t1.change_boost(result_data[1])
            t2.change_boost(result_data[2])
            t3.change_boost(result_data[3])
            t4.change_boost(result_data[4])
            t5.change_boost(result_data[5])

            sock.sendall("end".encode())
        elif(result_data[0] == "go"):
            game_start = True
            
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

                result = ""

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
                        result += str(t1_statue)
                    if(t2_statue!=None):
                        print(t2_statue)
                        result += str(t2_statue)
                    if(t3_statue!=None):
                        print(t3_statue)
                        result += str(t3_statue)
                    if(t4_statue!=None):
                        print(t4_statue)
                        result += str(t4_statue)
                    if(t5_statue!=None):
                        print(t5_statue)
                        result += str(t5_statue)
                    
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
                
                sock.sendall(result.encode())
        res = None
        print("")

        


    
exit()