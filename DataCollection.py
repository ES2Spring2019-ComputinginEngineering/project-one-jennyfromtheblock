#Project 1: Pedulum - Data Collection
#Allie and Yassi

from microbit import *
import math
import os

myFile = open('/Users/Yasaman/Documents/GitHub/project-one-jennyfromtheblock/angles.txt', 'w')
angles = []

while True:
    sleep(1000)
    x = accelerometer.get_x()
    z = accelerometer.get_z()
    radX = math.atan2(x, z) #Tilt in x-direction
    degX = radX / math.pi * 180 #Converting angle of x-tilt from radians to degrees

    if degX > 0:
        theta = - degX + 180
    else:
        theta = - (degX + 180)

    angles.append(theta)
    myFile.write(str(theta))
    myFile.write("\n")
    print(angles)