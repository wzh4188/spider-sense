import numpy as np
from time import sleep
import time
from adafruit_servokit import ServoKit
# leg.py

class Leg:
    def __init__(self, hat, channels, current_degrees):
        self.hat = hat
        self.channels = channels
        self.current_degrees = current_degrees

    def move(self, arr_deg):
        self.hat.servo[self.channels[0]].angle = arr_deg[0]
        self.hat.servo[self.channels[1]].angle = arr_deg[1]
        self.hat.servo[self.channels[2]].angle = arr_deg[2]
        self.current_degrees = arr_deg

    def reset_horizontal(self):
        self.hat.servo[self.channels[0]].angle = 90
        self.hat.servo[self.channels[1]].angle = self.current_degrees[1]
        self.hat.servo[self.channels[2]].angle = self.current_degrees[2]

    def change(self, change_degrees):
        # Change the leg's position by the specified degree
        new_degrees = self.current_degrees + change_degrees
        self.move(new_degrees)