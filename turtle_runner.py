import turtle
from config import *
import random
import time

class Runner:
    runner:turtle
    number: int
    end: bool = False

    def __init__(self, color, number):
        
        runner = turtle.Turtle()
        runner.up()
        runner.shape("turtle")
        runner.speed(0)
        runner.color(color)
        self.runner = runner
        self.number = number
        
    
    def turtleMove(self):
        if(self.end):
            return None
        elif(self.runner.pos()[0] <= width/2 - 100):
            self.runner.forward(random.randint(10, 50))
            
            time.sleep(0.001)
            
            return None
            
        
        self.end = True
        
        return self.number