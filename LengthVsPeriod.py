#Project 1: Pendulum
#Allie & Yassi
#Relationship between pendulum length and period

import matplotlib.pyplot as plt
import numpy as np

#The values of period and pendulum length as previously calculated
lengths = np.asarray([0.38, 0.26, 0.28, 0.30, 0.33])
realPeriods = np.asarray([1.144, 0.832, 1.09, 0.904, 0.968])
simulatedPeriods = np.asarray([1.262, 1.045, 1.08, 1.122, 1.176])

#Plotting the period vs. pendulum length
plt.figure()
plt.plot(lengths, simulatedPeriods,'ro',lengths, realPeriods,'bo' ) 
plt.ylabel('Period (seconds)')
plt.xlabel('Pendulum Length (m)')
plt.title('Period vs. Pendulum Length')
plt.xlim((0, 0.5)) 
plt.grid()
plt.tight_layout()

#Plotting the log function of period vs. pendulum length
plt.figure()
plt.loglog(lengths, simulatedPeriods,'ro',lengths, realPeriods,'bo' ) 
plt.ylabel('Period (seconds)')
plt.xlabel('Pendulum Length (m)')
plt.title('Period vs. Pendulum Length (Log Function)')
plt.xlim((0, 0.5)) 
plt.grid()
plt.tight_layout()