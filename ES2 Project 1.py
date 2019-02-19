#Project 1: Pedulum
#Allie and Yassi

import numpy as np

def update_system(acc,pos,vel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    posNext = pos+vel*dt+1/2*acc*dt
    velNext = vel+acc*dt
    return posNext,velNext

def print_system(time,pos,vel):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

# initial conditions
pos = [0]
vel = [0]
acc = [0,1,2,3,4,4,2,2,1,0,0,0,0,-1,-1,-2,-2,-2,-3,-4,-4]
time = np.linspace(0,20,21)
print_system(time[0],pos[0],vel[0])

i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext = update_system(acc[i],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    print_system(time[i],pos[i],vel[i])
    i += 1