#Project 1: Pedulum - Data Analysis
#Allie and Yassi
#Analysis of data obtained from microbit

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
import math

g = -9.81
l = 0.26
zAcc = []
xAcc = []
time = []
angles = []

#Openning the data file and extracting the recorded data:
with open ("secondTrial.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(",")
        t = float(line[0])
        x_acceleration = float(line[1])
        z_acceleration = float(line[2])
        xAcc.append(x_acceleration)
        zAcc.append(z_acceleration)
        time.append(t)

#Calculating the angle of tilt using acceleration values
for i in range(len(zAcc)):
    radX = math.atan2(xAcc[i],zAcc[i])#Tilt in x-direction
    degX = radX * 180 / math.pi#Converting angle of x-tilt from radians to degrees
    angles.append(degX)

#Converting the lists to np.arrays & applying filter to the raw data:
t = np.asarray(time)
theta = np.asarray(angles)
filt_theta = sig.medfilt(theta,3)
theta_pks, _ = sig.find_peaks(theta)
theta_filt_pks, _ = sig.find_peaks(filt_theta, prominence=50)

#Plotting the angle vs. time graph
plt.subplot(3,1,1)
plt.plot(t, filt_theta, 'r-', t[theta_filt_pks],filt_theta[theta_filt_pks] , 'ko')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Angle (degrees)')
plt.title('Angle vs Time')
plt.xlim((500, 4000)) 
plt.grid()

#Plotting the  acceleration (x-direction) vs. time graph
plt.subplot(3,1,3)
plt.plot(time, xAcc, 'r-') 
plt.xlabel('Time (milliseconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration (x-direction) vs Time')
plt.xlim((500, 4000)) 
plt.grid()
plt.tight_layout()

#Plotting the  acceleration (z-direction) vs. time graph
plt.subplot(3,1,2)
plt.plot(time, zAcc, 'b-') 
plt.xlabel('Time (milliseconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration (z-direction) vs Time')
plt.xlim((500, 4000)) 
plt.grid()
plt.tight_layout()

#Determining period by averaging time differences
peaks = t[theta_filt_pks[1:]]
time_difference = np.diff(peaks)
period = str((np.sum(time_difference)/len(time_difference))/1000)
print("Period: " + period + "s")