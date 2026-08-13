# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:24:56 2026

@author: Mariah Ellis


The purpose of this script was to test for absorption using the functions from propagation_and_transmission_matrix.py.


"""

import numpy as np
import matplotlib.pyplot as plt
from propagation_and_transmission_matrix import Propagation_Matrix, TransmissionMatrix, TR

#thickness of mediums
d = np.arange(0, 500e-9, 10e-9)

#indices:
n = [1.0+0j,
     1.0+0.1j, 
     1.0+0j ]

lambda0 = 500e-9
parallel_rk = 0

#empty lists to store l8r values in
Rs12 = np.zeros(len(d))
Rp21 = np.zeros(len(d))
Ts12 = np.zeros(len(d))
Tp21 = np.zeros(len(d))

#R and T at 42 degrees
Rs_Ts = np.zeros(len(d))
Rp_Tp = np.zeros(len(d))


#loop for 42 degrees
theta1 = np.deg2rad(0)
for i, thickness in enumerate(d):
    [P0, rk0, perpen_rk0, parallel_rk, k0] = Propagation_Matrix(1, n[0], 0, lambda0, parallel_rk, theta1)
    [P1, rk1, perpen_rk1, parallel_rk, k0] = Propagation_Matrix(2, n[1], thickness, lambda0, parallel_rk, theta1)
    [P2, rk2, perpen_rk2, parallel_rk, k0] = Propagation_Matrix(3, n[2], 0, lambda0, parallel_rk,  theta1)
    
    [D01s, D01p, s01s, s01p, SS01s, SS01p] = TransmissionMatrix(rk0, rk1, perpen_rk0, perpen_rk1)
    [D12s, D12p, s12s, s12p, SS12s, SS12p] = TransmissionMatrix(rk1, rk2, perpen_rk1, perpen_rk2)
    
    Ms = D01s @ P1 @ D12s 
    Mp = D01p @ P1 @ D12p 
    
    #Use TR for extracting power coefficients
    [ss, sp, Ss, Sp] = TR(Ms, Mp, rk0, perpen_rk0, rk2, perpen_rk2 )
    
    Rs12[i] = Ss[0,0]
    Ts12[i] = Ss[0,1]
    
    Rp21[i] = Sp[1,1]
    Tp21[i] = Sp[1,0]
    
    Rs_Ts[i] = Ss[0,0] + Ss[0,1]
    Rp_Tp[i] = Sp[1,1] + Sp[1,0]

#using 42 as the angle 
plt.plot(d/lambda0, Rs12, linestyle='dashed', color='blue', label= 'Rs', )      
plt.plot(d/lambda0, Rp21, linestyle='dashed', color= 'red', label = 'Rp')                    
plt.plot(d/lambda0, Ts12, linestyle='solid', color='blue', label = 'Ts')                 
plt.plot(d/lambda0, Tp21, linestyle='solid', color= 'red', label= 'Tp') 

#R and T plots
plt.plot(d/lambda0, Rs_Ts, linestyle='dashed', color='black', label= 'RsTs')   
plt.plot(d/lambda0, Rp_Tp, linestyle='solid', color= 'black', label = 'RpTp', ) 

# Pretty-ing the plots!!!
plt.legend(prop={'size':6})
plt.title("Absorption Test: 1.0 -> 1.0 + 0.1j -> 1.0")
plt.xlabel("d in terms of lambda")
plt.ylabel("Power Coefficients")
plt.xlim(0,1)
plt.show()