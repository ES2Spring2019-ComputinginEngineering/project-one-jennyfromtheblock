#Project 1: Pedulum - Data Collection
#Allie and Yassi

from microbit import *
import math
import os

while True:

    if button_a.is_pressed() == True:
        with open('data.txt', 'w') as data:
            time0 = running_time() #get the current running time
            while True:
                display.show(Image.HAPPY)
                sleep(50)
                x = accelerometer.get_x()
                z = accelerometer.get_z()

                time1 = running_time() #get the current running time
                data.write(str(time1-time0) + "," + str(x) + "," + str(z)+"\n")

                if button_b.is_pressed()== True:
                    display.show(Image.HEART)
                    data.close()
                    break