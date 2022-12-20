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
f1 = open("Exp_Hejmady_PA12_R125_E192.txt", "r")
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


# plt.plot(time,aR)

# --------------------------------------------------
#Arranging the data from Hejmady at specific time step
Specific_time = np.linspace(0.0, 5.0, num=142)
np.ndarray.sort(time)
# np.ndarray.sort(aR)

tck = interpolate.splrep(time, aR, s=0)
ynew = interpolate.splev(Specific_time, tck, der=0)

# plt.plot(Specific_time,ynew,'bo')

# plt.show()
# ---------------------
f2 = open("Exp_Hejmady_PA12_R125_E192_Temperature.txt", "r")
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
# plt.show()
# --------------------------------------------------
#Arranging the data from Hejmady at specific time step
np.ndarray.sort(time2)

tck2 = interpolate.splrep(time2, Temperature, s=0)
ynew2 = interpolate.splev(Specific_time, tck2, der=0)

print()
plt.plot(Specific_time,ynew2,'bo')

plt.show()
# ---------------------
fileName = open('Obs_R125e-6.dat', 'wb')
np.savetxt(fileName,np.c_[Specific_time,abs(ynew),abs(ynew2)],header="time a_r temp",fmt='%.5f')

# print(Specific_time, A_Rinterpolated)

f1.close()
f2.close()
fileName.close()
