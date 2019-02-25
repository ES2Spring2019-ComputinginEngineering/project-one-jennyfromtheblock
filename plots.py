#Project 1: Pedulum
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

# initial conditions
theta = [(math.pi)/6]
angVel = [0]
angAcc = [(g/l) * math.cos((math.pi/2) - theta[0])]
time = np.linspace(0,10,10000)

for i in range(1, len(time)):
    # update position and velocity using previous values and time step
    newTheta, newAngVel , newAngAcc = update_system(angAcc[i-1],theta[i-1],angVel[i-1],time[i-1],time[i])
    theta.append(newTheta)
    angVel.append(newAngVel)
    angAcc.append(newAngAcc)
    i += 1
    
plt.subplot(3,1,1)
plt.plot(time, theta, 'ro--') 

plt.xlabel('Time (seconds)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()

plt.subplot(3,1,2)
plt.plot(time, angVel, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,3)
plt.plot(time, angAcc, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()