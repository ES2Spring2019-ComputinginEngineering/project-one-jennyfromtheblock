#Project 1: Pedulum - Data Analysis
#Allie and Yassi

import matplotlib.pyplot as plt
import numpy as np
import math

g = -9.81
l = 0.365

myFile = open("Test1anglesES2.txt", "r")
contents = myFile.read()

print(type(contents))