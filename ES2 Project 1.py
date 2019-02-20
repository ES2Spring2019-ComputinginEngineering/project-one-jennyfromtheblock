#Project 1: Pedulum
#Allie and Yassi

import numpy as np
import math

g = 9.81
l = 1

def update_system(angAcc,theta,angVel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    newTheta = theta + angVel * dt
    newAngVel = angVel + angAcc*dt
    newAngAcc = (g/l) * math.cos((math.pi/2) - theta)
    return newTheta,newAngVel,newAngAcc

def print_system(time,theta,angVel, angAcc):
    print("TIME:     ", time)
    print("Angle: ", theta)
    print("ANGULAR VELOCITY: ", angVel)
    print("ANGULAR ACCELERATION: ", angAcc, "\n")


# initial conditions
theta = [30]
angVel = [0]
angAcc = [0]
time = np.linspace(0,20,21)
print_system(time[0],theta[0],angVel[0],angAcc[0])

for i in range(1, len(time)):
    # update position and velocity using previous values and time step
    newTheta, newAngVel , newAngAcc = update_system(angAcc[i-1],theta[i-1],angVel[i-1],time[i-1],time[i])
    theta.append(newTheta)
    angVel.append(newAngVel)
    angAcc.append(newAngAcc)
    print_system(time[i],theta[i],angVel[i],angAcc[i])
    i += 1