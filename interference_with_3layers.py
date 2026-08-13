# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:34:14 2026

@author: Mariah Ellis


The purpose of this script was to test for interference for a three layer system, starting 
from glass, to air, back to glass (indexes 1.5 -> 1.0 -> 1.5) 
using the functions from propagation_and_transmission_matrix.py


"""


import numpy as np
import matplotlib.pyplot as plt
from fixed_prop_and_trans_matrix import Propagation_Matrix, TransmissionMatrix, TR


#thickness of mediums as a list
d = np.arange(0, 500e-9, 10e-9)

wavelength = np.arange(400e-09, 750e-9, 100e-9)

#indices:
n = [1.5+0j,
     1.0+0j, 
     1.5+0j ]

lambda0 = 500e-9
parallel_rk = 0

#empty lists to store values in later
Rs12_0 = np.zeros(len(d))
Rp21_0 = np.zeros(len(d))
Ts12_0 = np.zeros(len(d))
Tp21_0 = np.zeros(len(d))

Rs12_35 = np.zeros(len(d))
Rp21_35 = np.zeros(len(d))
Ts12_35 = np.zeros(len(d))
Tp21_35 = np.zeros(len(d))

#adding them together for each angle
Rs_Ts_0 = np.zeros(len(d))
Rs_Ts_35 = np.zeros(len(d))
Rp_Tp_0 = np.zeros(len(d))
Rp_Tp_35 = np.zeros(len(d))


theta1 = np.deg2rad(0)
for i, thickness in enumerate(d): 
    #wavelength in terms of lambda
    [P0, rk0, perpen_rk0, parallel_rk, k0] = Propagation_Matrix(1, n[0], 0, lambda0, parallel_rk, theta1)
    [P1, rk1, perpen_rk1, parallel_rk, k0] = Propagation_Matrix(2, n[1], thickness, lambda0, parallel_rk, theta1)
    [P2, rk2, perpen_rk2, parallel_rk, k0] = Propagation_Matrix(3, n[2], 0, lambda0, parallel_rk,  theta1)
    
    [D01s, D01p, s01s, s01p, SS01s, SS01p] = TransmissionMatrix(rk0, rk1, perpen_rk0, perpen_rk1)
    [D12s, D12p, s12s, s12p, SS12s, SS12p] = TransmissionMatrix(rk1, rk2, perpen_rk1, perpen_rk2)
    
    Ms = D01s @ P1 @ D12s  #first and last propagation matrix won't affect results
    Mp = D01p @ P1 @ D12p 
    
    [ss, sp, Ss, Sp] = TR(Ms, Mp, rk0, perpen_rk0, rk2, perpen_rk2 )
    
    Rs12_0[i] = Ss[0,0]
    Ts12_0[i] = Ss[0,1]
    
    Rp21_0[i] = Sp[1,1]
    Tp21_0[i] = Sp[1,0]
    
    Rs_Ts_0[i] = Ss[0,0] + Ss[0,1]
    Rp_Tp_0[i] = Sp[1,1] + Sp[1,0]
        
    
#using 0 as the angle 
plt.plot(d/lambda0, Rs12_0, linestyle='dashed', color='blue', label= 'Rs0', linewidth=3)      
plt.plot(d/lambda0, Rp21_0 , linestyle='dashed', color= 'red', label = 'Rp0')                    
plt.plot(d/lambda0, Ts12_0, linestyle='solid', color='blue', label = 'Ts0', linewidth=3)                 
plt.plot(d/lambda0, Tp21_0, linestyle='solid', color= 'red', label= 'Tp0')                      

plt.plot(d/lambda0, Rs_Ts_0, linestyle='dashed', color='black', label= 'RsTs at 0', linewidth=3 )   
plt.plot(d/lambda0, Rp_Tp_0, linestyle='solid', color= 'black', label = 'RpTp at 0' )                
    
theta2 = np.deg2rad(35.2644)    
for i, thickness in enumerate(d):
    #wavelength in terms of lambda
     
     [P0_35, rk0_35, perpen_rk0_35, parallel_rk, k0] = Propagation_Matrix(1, 1.5, 0, lambda0, parallel_rk, theta2)
     [P1_35, rk1_35, perpen_rk1_35, parallel_rk, k0] = Propagation_Matrix(2, 1.0, thickness, lambda0, parallel_rk,  theta2)
     [P2_35, rk2_35, perpen_rk2_35, parallel_rk, k0] = Propagation_Matrix(3, 1.5, 0, lambda0, parallel_rk, theta2)
     
     [D01s_35, D01p_35, s01s_35, s01p_35, SS01s_35, SS01p_35] = TransmissionMatrix(rk0_35, rk1_35, perpen_rk0_35, perpen_rk1_35)
     [D12s_35, D12p_35, s12s_35, s12p_35, SS12s_35, SS12p_35] = TransmissionMatrix(rk1_35, rk2_35, perpen_rk1_35, perpen_rk2_35)
     
     
     Ms_35 = P0_35 @ D01s_35 @ P1_35 @ D12s_35 @ P2_35
     Mp_35 = P0_35 @ D01p_35 @ P1_35 @ D12p_35@ P2_35
     
     [_, _, Ss_35, Sp_35] = TR(Ms_35, Mp_35, rk0_35, perpen_rk0_35, rk2_35, perpen_rk2_35)
     
     Rs12_35[i] = Ss_35[0,0]
     Rp21_35[i] = Sp_35[1,1]
     Ts12_35[i] = Ss_35[0,1]
     Tp21_35[i] = Sp_35[1,0]   
     
     Rs_Ts_35[i] = Ss_35[0,0] + Ss_35[0,1]
     Rp_Tp_35[i] = Sp_35[1,1] + Sp_35[1,0]

     
# using 35.2644 as the angle
plt.plot(d/lambda0, Rs12_35, linestyle='dashed', color='blue', label= 'Rs35', marker='o', markersize=4)                 
plt.plot(d/lambda0, Rp21_35 , linestyle='solid', color= 'red', label = 'Rp35', marker='o', markersize=4)              
plt.plot(d/lambda0, Ts12_35, linestyle='dashed', color='blue', label = 'Ts35', marker='x', markersize=4)  
plt.plot(d/lambda0, Tp21_35, linestyle='solid', color= 'red', label= 'Tp35', marker='x', markersize=4)               

plt.plot(d/lambda0, Rs_Ts_35, linestyle='dashed', color='black', label = 'RsTs35', marker ='x', markersize=4)
plt.plot(d/lambda0, Rp_Tp_35, linestyle='solid', color= 'black', label= 'RpTp35', marker ='.', markersize=5)


#Pretty-ing the plots!!!
plt.legend(prop={'size':8})
plt.title("Interference Test: 1.5 -> 1.0 -> 1.5")
plt.xlabel("d in terms of lambda")
plt.ylabel("Power Coefficient")
plt.show()