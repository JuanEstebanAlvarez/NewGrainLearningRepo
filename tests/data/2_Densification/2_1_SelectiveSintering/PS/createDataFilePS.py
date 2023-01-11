# This script creates the .data file that GrainLearning program will read

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
#header = "Virgin Powder - Experimental data PA12"
#header1 = "Particle radius R"
header = "time, a_R, Temp"

#Reading the files from Hejmady experiments
# ---------------------EXPERIMENTS - Virgin Powder
f1 = open("Exp_Hejmady_PS_R60_E19.txt", "r")
lines = f1.readlines()
time = []
aR = []
for x in lines:
    time.append(x.split(' ')[0])
    aR.append(x.split(' ')[1])

time = np.array(time)
time = time.astype(np.float64)

aR = np.array(aR)
aR = aR.astype(np.float64)

f1.close()

# --------------------------------------------------
#Arranging the data from Hejmady at specific time step
Specific_time = np.linspace(0.0, 2.5, num=141)
np.ndarray.sort(time)
# np.ndarray.sort(aR)

tck = interpolate.splrep(time, aR, s=0)
ynew = interpolate.splev(Specific_time, tck, der=0)

# plt.plot(Specific_time,ynew,'bo')

# plt.show()

# # ---------------------
f2 = open("Exp_Hejmady_PS_R60e-6E19_Temperature.txt", "r")
lines = f2.readlines()
time2=[]
Temperature = []
for x in lines:
    time2.append(x.split(' ')[0])
    Temperature.append(x.split(' ')[1])

time2 = np.array(time2)
time2 = time2.astype(np.float64)

Temperature = np.array(Temperature)
Temperature = Temperature.astype(np.float64)

plt.plot(time2,Temperature)
print(np.shape(ynew))
print(np.shape(Temperature))
# plt.show()
# # --------------------------------------------------

plt.show()
# # ---------------------
fileName = open('Obs_PS_R60e-6E19.dat', 'wb')
np.savetxt(fileName,np.c_[Specific_time,abs(ynew),abs(Temperature)],header="time a_r temp",fmt='%.5f')

f1.close()
f2.close()
fileName.close()
