#Project 1: Pedulum - Data Collection
#Allie and Yassi

from microbit import *
import math
import os

angles = open('angles.txt', 'w')
time = open('time.txt', 'w')

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
            angles.write(str(theta), "\n")
            time.write(str(time1-time0), "\n")

            if button_b.is_pressed()== True:
                myFile.close()