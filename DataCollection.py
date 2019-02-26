#Project 1: Pedulum - Data Collection
#Allie and Yassi

from microbit import *
import math
import os

angles = []

while True:
    sleep(1000)
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    radX = math.atan2(x, z) #Tilt in x-direction
    radY = math.atan2(y, z) #Tilt in y-direction

    degX = radX / math.pi * 180 #Converting angle of x-tilt from radians to degrees
    degY = radY / math.pi * 180 #Converting angle of y-tilt from radians to degrees

    theta = 180 - degY
    angles.append(theta)

    myFile = open('/Users/Yasaman/Documents/GitHub/HW5-ykhorsandian/20plus_words.txt', 'w')


    print(angles)