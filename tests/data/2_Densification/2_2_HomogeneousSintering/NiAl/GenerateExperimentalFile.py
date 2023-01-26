# This script creates the .data file that GrainLearning program will read

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.stats import linregress


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
f1 = open("TemperatureProfileNiAl.txt", "r")
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
time, Temperature = extractinfo(f1)
fig, ax = plt.subplots()

plt.plot(time,Temperature,'x',color ='red',label= 'NiAL data')
# circle1 = plt.Circle((130, 1050), 2000, color='black',alpha=0.2)


DEM_time = np.array([100.0,125, 140,150])
DEM_temperature = np.array([1000.0,1400,1400,1400])


print(linregress(DEM_time, DEM_temperature))

plt.plot(DEM_time,DEM_temperature,'-',color = 'blue',label='DEM')

plt.text(120, 1150, 'Dilatation zone', fontsize=12,color='black')
# plt.xlim((140,160))
# ax.add_patch(circle1)
plt.ylabel('T [$^\circ$C]')
plt.xlabel('t [min]')
# plt.ylim((120,195))
plt.grid()
plt.legend()
plt.savefig('TemperatureNiAl.eps', format='eps')
# # --------------------------------------------------
#
f3 = open("ShrinkageNiAl.txt", "r")
#
#
time, Shrinkage = extractinfo(f3)
# timeNetzch, ShrinkageNetzch = extractinfo(f4)
#
fig2, ax2 = plt.subplots()
#
plt.plot(time,Shrinkage-1,'-x',color ='black',label= 'NiAl data')
# plt.plot(timeNetzch,ShrinkageNetzch,'-o',color = 'black',label= 'Netzsch Dilatometer')
# # circle1 = plt.Circle((145, 172), 20, color='black',alpha=0.2)
#
plt.text(40, -0.2, 'Dilatation zone', fontsize=12,color='black')
#
plt.ylabel('$\Delta L/ L_0 $ [-]')
plt.xlabel('t [min]')
# # plt.ylim((120,195))
plt.grid()
plt.legend()
#
plt.savefig('ShrinkageNiAl.eps', format='eps')






plt.show()