# This script creates the .data file that GrainLearning program will read

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

#header = "Virgin Powder - Experimental data PA12"
#header1 = "Particle radius R"
header = "time, a_R"
# ---------------------EXPERIMENTS - Virgin Powder
# Experiment Number 51: R_mean: 25.84 [micro m]
# Exp51_Rmean = np.array([2.584e-5])
# Exp51_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
# Exp51_aR = np.array([0.0, 0.454, 0.534, 0.627, 0.801, 0.908, 0.988, 1.068, 1.081])

# Experiment Number 91B: R_mean: 28.85 [micro m]
# Exp91B_Rmean = np.array([2.885e-5])
# Exp91B_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 7.0, 9.0, 12.0, 15.0])
# Exp91B_aR = np.array([0.000, 0.410, 0.485, 0.634, 0.746, 0.839, 0.932, 1.081, 1.156, 1.231, 1.286, 1.305, 1.305])

# Experiment Number 91: R_mean: 29.28 [micro m]
# Exp91_Rmean = np.array([2.928e-5])
# Exp91_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 7.0, 9.0, 12.0, 15.0])
# Exp91_aR = np.array([0.000, 0.551, 0.625, 0.772, 0.882, 0.955, 1.029, 1.121, 1.176, 1.231, 1.249, 1.268, 1.268])

#Experiment Number 91: R_mean: 30.44 [micro m]
# Exp91C_Rmean = np.array([3.044e-5])
# Exp91C_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 7.0, 9.0, 12.0, 15.0])
# Exp91C_aR = np.array([0.000, 0.406, 0.459, 0.565, 0.707, 0.813, 0.901, 1.025, 1.096, 1.184, 1.255, 1.272, 1.290])

#Experiment Number 91B: R_mean: 32.1 [micro m]
Exp91D_Rmean = np.array([3.210e-5])
Exp91D_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 7.5, 9.5, 12.5, 15.5])

Exp91D_aR = np.array([0.000, 0.402, 0.503, 0.603, 0.754, 0.855, 0.939, 1.006, 1.089, 1.156, 1.223, 1.274, 1.274, 1.274])

#Experiment Number 21: R_mean: 32.16 [micro m]
# Exp21_Rmean = np.array([3.216e-5])
# Exp21_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
# Exp21_aR = np.array([0.0, 0.421, 0.463, 0.494, 0.603, 0.768, 0.866, 0.957, 1.000, 1.036, 1.091, 1.128, 1.152, 1.170, 1.183])

# #Experiment Number 51: R_mean: 33.14 [micro m]
# Exp51B_Rmean = np.array([3.314e-5])
# Exp51B_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
# Exp51B_aR = np.array([0.0, 0.513, 0.531, 0.638, 0.743, 0.828, 0.846, 0.936, 1.009])
#
# #Experiment Number 81C: R_mean: 33.9 [micro m]
# Exp81C_Rmean = np.array([3.390e-5])
# Exp81C_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0, 12.0, 16.0])
# Exp81C_aR = np.array([0.000, 0.478, 0.570, 0.651, 0.763, 0.835, 0.906, 0.967, 1.028, 1.099, 1.140, 1.211, 1.252, 1.272])
#
# #Experiment Number 91E: R_mean: 35.12 [micro m]
# Exp91E_Rmean = np.array([3.512e-5])
# Exp91E_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 7.5, 9.5, 12.5, 15.5])
# Exp91E_aR = np.array([0.000, 0.414, 0.460, 0.521, 0.674, 0.797, 0.873, 0.950, 1.057, 1.118, 1.195, 1.256, 1.287, 1.287])
#
# #Experiment Number 81: R_mean: 37.90 [micro m]
# Exp81_Rmean = np.array([3.790e-5])
# Exp81_t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0, 12.0, 16.0])
# Exp81_aR = np.array([0.000, 0.273, 0.291, 0.319, 0.428, 0.546, 0.655, 0.765, 0.819, 0.956, 1.029, 1.138, 1.220, 1.247])
# ---------------------
f = open('Obs_3.210e-5.dat', 'wb')

Specific_time = np.linspace(0.0, 20, num=122, endpoint=True)

tck = interpolate.splrep(Exp91D_t, Exp91D_aR, s=0)
ynew = interpolate.splev(Specific_time, tck, der=0)
# f = interp1d(x, y)
# A_Rinterpolated = interp1d(Exp81_t,Exp81_aR, Specific_time)
#
cont = 0

for i in ynew:
    cont = cont + 1
    if i > max(Exp91D_aR):
        ynew[cont-1] = max(Exp91D_aR)


fig, ax = plt.subplots()
ax.plot(Specific_time,ynew,'bo')
ax.plot(Exp91D_t,Exp91D_aR,'ro')
plt.show()

np.savetxt(f,np.c_[Specific_time,abs(ynew)],header="time aR",fmt='%.3f')

# print(Specific_time, A_Rinterpolated)

f.close()
