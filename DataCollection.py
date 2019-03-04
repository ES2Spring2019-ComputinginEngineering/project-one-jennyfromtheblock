#Project 1: Pedulum - Data Collection
#Allie and Yassi

from microbit import *
import math
import os

myFile = open('angles.txt', 'w')
angles = []
time = []

while True:
    if button_a.is_pressed() == True:
        time0 = running_time() #get the current running time
        while True:
            sleep(50)
            x = accelerometer.get_x()
            z = accelerometer.get_z()
            radX = math.atan2(x, z) #Tilt in x-direction
            degX = radX / math.pi * 180 #Converting angle of x-tilt from radians to degrees

            if degX > 0:
                theta = - degX + 180
            else:
                theta = - (degX + 180)

            time1 = running_time() #get the current running time
            time.append(time1-time0)
            angles.append(theta)
            myFile.write(str(theta))
            myFile.write("\n")
            print(angles)

            if button_b.is_pressed()== True:
                myFile.close()