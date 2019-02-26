#Project 1: Pendulum
#Allie and Yassi

import matplotlib.pyplot as plt
import numpy as np
import math

g = 9.81
l = 0.3

def update_system(angAcc,theta,angVel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    newTheta = theta + angVel * dt
    newAngVel = angVel + angAcc*dt
    newAngAcc = (g/l) * math.cos((math.pi/2) - newTheta)
    return newTheta,newAngVel,newAngAcc

def print_system(time,theta,angVel, angAcc):
    print("TIME:     ", time)
    print("Angle: ", theta*180/math.pi)
    print("ANGULAR VELOCITY: ", angVel)
    print("ANGULAR ACCELERATION: ", angAcc, "\n")


# initial conditions
theta = [(math.pi)/6]
angVel = [0]
angAcc = [(g/l) * math.cos((math.pi/2) - theta[0])]
time = np.linspace(0,20,20000)
print_system(time[0],theta[0],angVel[0],angAcc[0])

for i in range(1, len(time)):
    # update position and velocity using previous values and time step
    newTheta, newAngVel , newAngAcc = update_system(angAcc[i-1],theta[i-1],angVel[i-1],time[i-1],time[i])
    theta.append(newTheta)
    angVel.append(newAngVel)
    angAcc.append(newAngAcc)
    print_system(time[i],theta[i],angVel[i],angAcc[i])
    i += 1

plt.subplot(3,1,1)
plt.plot(time, theta, 'ro--')

plt.xlabel('Time (seconds)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()