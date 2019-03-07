#Project 1: Pedulum - Data Collection
#Allie and Yassi

from microbit import *
import math
import os

while True:
    if button_a.is_pressed() == True:
        with open('data.txt', 'w') as data: #opens the file to record data
            time0 = running_time() #gets the current running time when button a is pressed
            while True:
                sleep(50)
                x = accelerometer.get_x()
                z = accelerometer.get_z()
                time1 = running_time() #gets the current running time
                data.write(str(time1-time0) + "," + str(x) + "," + str(z)+"\n") #records the time and acceleration values to file

                if button_b.is_pressed()== True: #ends the data collection by closing the file
                    data.close()
                    break