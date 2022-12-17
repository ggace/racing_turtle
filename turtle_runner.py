import turtle
from config import *
import random
import time
from boost import *

import json

def setup():
    global score
    score = 5

class Runner:
    runner:turtle
    number: int
    end: bool = False
    boost:Boost
    default_forward = (10,30)
    boost_on = False

    y = []

    def __init__(self, color:str, number:int, boost=None):
        
        runner = turtle.Turtle()
        runner.up()
        runner.shape("turtle")
        runner.speed(0)
        runner.color(color)
        self.runner = runner
        self.number = number
        self.boost = boost
    def setup(self):
        self.y = []
    def change_boost(self, boost_setting:str):
        boost_split = boost_setting.split(" ")
        self.boost = Boost(float(boost_split[0]), (float(boost_split[1]), float(boost_split[2])))
    def turtleMove(self):
        global score
        self.y.append(self.runner.pos()[0])
        if(self.end):
            return None
        elif(self.runner.pos()[0] <= width/2 - 100):
            self.boost_on = self.check_boost_percentage()
            if(self.boost != None and self.boost_on):
                self.runner.forward(random.randint(self.boost.forward[0], self.boost.forward[1]))
            else:
                self.runner.forward(random.randint(self.default_forward[0], self.default_forward[1]))
            
            
            
            return None
            
        
        self.end = True

        with open('result.json') as f:
            json_object = json.load(f)
        
        json_object[f"{self.number}"] = json_object[f"{self.number}"] + score
        score -= 1

        with open('result.json', 'w') as f:
            json.dump(json_object, f, indent=2)
        
        return self.number

    def check_boost_percentage(self):
        if(self.boost != None):
            now = random.randint(1, 1000)/10
            if(now <= self.boost.percentage):
                return True
        return False