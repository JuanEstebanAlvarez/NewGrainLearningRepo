# This script creates the .data file that GrainLearning program will read

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.stats import linregress
# from sklearn.linear_model import LinearRegression

import seaborn as sns; sns.set(style="white")
from matplotlib import rc
from matplotlib.patches import Circle, Ellipse
from sympy import Symbol,expand, simplify
# For plotting
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

from scipy.interpolate import splev, splrep
#header = "Virgin Powder - Experimental data PA12"
#header1 = "Particle radius R"
header = "time, Temp, deltaL_L0"

#Reading the files from Hejmady experiments
# ---------------------EXPERIMENTS
f1 = open("DilatometerTemperatureJuan.txt", "r")
f2 = open("DilatometerTemperatureNetzch.txt", "r")
#++++++++++++++++++++++++++++++++++++++++++
#Function to read information from file
def extractinfo (fileName):
    lines = fileName.readlines()
    x1 = []
    x2 = []
    for x in lines:
        x1.append(x.split(' ')[0])
        x2.append(x.split(' ')[1])

    x1 = np.array(x1)
    x1 = x1.astype(np.float64)

    x2 = np.array(x2)
    x2 = x2.astype(np.float64)

    fileName.close()
    return x1, x2

#++++++++++++++++++++++++++++++++++++++++++
timeJuan, TemperatureJuan = extractinfo(f1)
timeNetzch, TemperatureNetzch = extractinfo(f2)
fig, ax = plt.subplots()

plt.plot(timeJuan+5,TemperatureJuan,'x',color ='red',label= 'UT Dilatometer')
plt.plot(timeNetzch,TemperatureNetzch,'o',color = 'red',label= 'Netzsch Dilatometer')
circle1 = plt.Circle((150, 180), 10, color='black', fill=False)


DEM_time = np.array([96.0,155.0, 156,160])
DEM_temperature = np.array([125.0,185.0,185,185])


print(linregress(DEM_time, DEM_temperature))

plt.plot(DEM_time,DEM_temperature,'-',color = 'blue',label='DEM')

plt.text(145, 165, 'Dilatation zone', fontsize=12,color='black')
# plt.xlim((140,160))
ax.add_patch(circle1)
plt.ylabel('T [$^\circ$C]')
plt.xlabel('t [min]')
# plt.ylim((120,195))
plt.grid()
plt.legend()
plt.savefig('PA12TemperatureDilatometers.eps', format='eps')
# # --------------------------------------------------

f3 = open("DilatometerShrinkageJuan.txt", "r")
f4 = open("DilatometerShrinkageNiztch.txt", "r")


timeJuan, ShrinkageJuan = extractinfo(f3)
timeNetzch, ShrinkageNetzch = extractinfo(f4)

fig2, ax2 = plt.subplots()

plt.plot(timeJuan+5,ShrinkageJuan,'-x',color ='black',label= 'UT Dilatometer')
plt.plot(timeNetzch,ShrinkageNetzch,'-o',color = 'black',label= 'Netzsch Dilatometer')
# circle1 = plt.Circle((145, 172), 20, color='black',alpha=0.2)

plt.text(140, -4, 'Dilatation zone', fontsize=12,color='black')

plt.ylabel('$\Delta L/ L_0 \\times ^{-3}$ [-]')
plt.xlabel('t [min]')
# plt.ylim((120,195))
plt.grid()
plt.legend()

plt.savefig('ShrinkagePA12.eps', format='eps')


fig3, ax3 = plt.subplots()

NewTimeJuan = ((timeJuan+5)-130)/1000
NewTimeNet = (timeNetzch-130)/1000

plt.plot(NewTimeJuan,ShrinkageJuan,'-x',color ='red',label= 'UT Dilatometer')
plt.plot(NewTimeNet,ShrinkageNetzch,'-o',color = 'red',label= 'Netzsch Dilatometer')

SpecificTime = np.linspace(0.0,0.03,142)


tck = interpolate.splrep(NewTimeJuan, ShrinkageJuan, s=1)
tck2 = interpolate.splrep(NewTimeNet, ShrinkageNetzch, s=1)

ynew = interpolate.splev(SpecificTime, tck, der=0)
ynew2 = interpolate.splev(SpecificTime, tck2, der=0)

plt.plot(SpecificTime,ynew,'-x', color='blue', label='Juan')
plt.plot(SpecificTime,ynew2,'-x', color='green', label = 'Net')

mean_x = np.mean((SpecificTime,SpecificTime), axis=0)
mean_y = np.mean((ynew,ynew2), axis=0)

plt.legend()
plt.plot(mean_x,mean_y, color='black')

fileName = open('Obs_Dilatometer_PA12.dat', 'wb')
np.savetxt(fileName,np.c_[abs(mean_x),mean_y/1000.0],header="time deltaL",fmt='%.5f')

plt.show()