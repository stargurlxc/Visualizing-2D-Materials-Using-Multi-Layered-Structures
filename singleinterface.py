# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:51:35 2026

@author: Mariah Ellis


The purpose of this script was to use the functions from propagation_and_transmission_matrix.py
 to reproduce the graphs on https://en.wikipedia.org/wiki/Fresnel_equations.
"""
#Test case for a single interface

import numpy as np
import matplotlib.pyplot as plt
from propagation_and_transmission_matrix import Propagation_Matrix, TransmissionMatrix, TR

#indices:
n = [1.0+0j,
     1.5+0j, 
     1.5+0j]

angles = range(0,90)

lambdaa = 500e-9
parallel_rk = 0

#empty lists to store values in l8r
rs = []
rp = []
tp = []
ts = []
Rs = []
Rp = []
Ts = []
Tp = []

#chnage indexes to see glass to air
for x, theta in enumerate(angles):  
   #need P0 and P1 for k values, but they have no effect on a single interface system
   [P0, rk0, perpen_rk0, parallel_rk, k0] = Propagation_Matrix(1, n[0], 0, lambdaa, parallel_rk, np.deg2rad(theta))
   [P1, rk1, perpen_rk1, parallel_rk, k0] = Propagation_Matrix(2, n[1], 0, lambdaa, parallel_rk, np.deg2rad(theta))  #only need for calculating rk0 etc

   [D01s, D01p, s01s, s01p, SS01s, SS01p] = TransmissionMatrix(rk0, rk1, perpen_rk0, perpen_rk1)   
   
   Ms = D01s 
   Mp = D01p 
   
   #extracting amplitude and power coefficients
   [ss, sp, Ss, Sp] = TR(Ms, Mp, rk0, perpen_rk0, rk1, perpen_rk1)
   
   rs.append(s01s[0,0])
   rp.append(s01p[0,0])
   ts.append(s01s[0,1])
   tp.append(s01p[0,1])
   
   Rs.append(SS01s[0,0])
   Rp.append(SS01p[0,0])
   Ts.append(SS01s[0,1])
   Tp.append(SS01p[0,1])
   
   
#Amplitude coefficients
# plt.plot(angles, rs, linestyle='dashed', color='skyblue', label= 'rs')
# plt.plot(angles, rp, linestyle='solid', color= 'pink', label = 'rp')
# plt.plot(angles, ts, linestyle='dashed', color='skyblue', label = 'ts')
# plt.plot(angles, tp, linestyle='solid', color= 'pink', label= 'tp')

#Power coefficients
plt.plot(angles, Rs, linestyle='dashed', color='pink', label= 'Rs')
plt.plot(angles, Rp, linestyle='dashed', color= 'skyblue', label = 'Rp')
plt.plot(angles, Ts, linestyle='solid', color='pink', label = 'Ts')
plt.plot(angles, Tp, linestyle='solid', color= 'skyblue', label= 'Tp')

#Pretty-ing the plots!!!
plt.legend(prop={'size':8})
plt.title("NEW Fresnel Power Coefficients (glass to air)")
plt.xlabel("Angle of Incidence (deg)")
plt.ylabel("Power Coefficient")
plt.xlim(0,90)
plt.grid(True)
plt.show()