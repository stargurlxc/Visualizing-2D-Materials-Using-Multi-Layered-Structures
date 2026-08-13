# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 03:15:31 2026

@author: Mariah Ellis

The purpose of this script was to test for evanescence using the functions from propagation_and_transmission_matrix.py.

"""


#testing for evanescence

import numpy as np
import matplotlib.pyplot as plt
from propagation_and_transmission_matrix import Propagation_Matrix, TransmissionMatrix, TR

#thickness of mediums
d = np.arange(0, 150e-8, 10e-9)

#indices:
n = [1.5+0j,
     1.0+0j, 
     1.5+0j ]

lambda0 = 500e-9
parallel_rk = 0

#empty lists to store l8r values in
#42 degrees
Rs12_42 = np.zeros(len(d))
Rp21_42 = np.zeros(len(d))
Ts12_42 = np.zeros(len(d))
Tp21_42 = np.zeros(len(d))

#R and T at 42 degrees
Rs_Ts_42 = np.zeros(len(d))
Rp_Tp_42 = np.zeros(len(d))


#44 degrees
Rs12_44 = np.zeros(len(d))
Rp21_44 = np.zeros(len(d))
Ts12_44 = np.zeros(len(d))
Tp21_44 = np.zeros(len(d))

#R and T at 44 degrees
Rs_Ts_44 = np.zeros(len(d))
Rp_Tp_44 = np.zeros(len(d))

#46 degrees
Rs12_46 = np.zeros(len(d))
Rp21_46 = np.zeros(len(d))
Ts12_46 = np.zeros(len(d))
Tp21_46 = np.zeros(len(d))

#R and T at 46 degrees
Rs_Ts_46 = np.zeros(len(d))
Rp_Tp_46 = np.zeros(len(d))



#loop for 42 degrees
theta1 = np.deg2rad(42)
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
    
    Rs12_42[i] = Ss[0,0]
    Ts12_42[i] = Ss[0,1]
    
    Rp21_42[i] = Sp[1,1]
    Tp21_42[i] = Sp[1,0]
    
    Rs_Ts_42[i] = Ss[0,0] + Ss[0,1]
    Rp_Tp_42[i] = Sp[1,1] + Sp[1,0]
    
#using 42 as the angle 
plt.plot(d/lambda0, Rs12_42, linestyle='dashed', color='blue', label= 'Rs42', )      
plt.plot(d/lambda0, Rp21_42 , linestyle='dashed', color= 'red', label = 'Rp42')                    
plt.plot(d/lambda0, Ts12_42, linestyle='solid', color='blue', label = 'Ts42')                 
plt.plot(d/lambda0, Tp21_42, linestyle='solid', color= 'red', label= 'Tp42') 

#R and T plots for 42 degrees
plt.plot(d/lambda0, Rs_Ts_42, linestyle='dashed', color='black', label= 'RsTs42', linewidth=1 , markersize=.5 )   
plt.plot(d/lambda0, Rp_Tp_42, linestyle='solid', color= 'black', label = 'RpTp42', linewidth=1, markersize=.5 )    


#loops using 44 as the angle
theta2 = np.deg2rad(44)
for i, thickness in enumerate(d):
    #wavelength in terms of lambda
     [P0_44, rk0_44, perpen_rk0_44, parallel_rk, k0] = Propagation_Matrix(1, 1.5, 0, lambda0, parallel_rk, theta2)
     [P1_44, rk1_44, perpen_rk1_44, parallel_rk, k0] = Propagation_Matrix(2, 1.0, thickness, lambda0, parallel_rk,  theta2)
     [P2_44, rk2_44, perpen_rk2_44, parallel_rk, k0] = Propagation_Matrix(3, 1.5, 0, lambda0, parallel_rk, theta2)
     
     [D01s_44, D01p_44, s01s_44, s01p_44, SS01s_44, SS01p_44] = TransmissionMatrix(rk0_44, rk1_44, perpen_rk0_44, perpen_rk1_44)
     [D12s_44, D12p_44, s12s_44, s12p_44, SS12s_44, SS12p_44] = TransmissionMatrix(rk1_44, rk2_44, perpen_rk1_44, perpen_rk2_44)
     
     Ms_44 = P0_44 @ D01s_44 @ P1_44 @ D12s_44 @ P2_44
     Mp_44 = P0_44 @ D01p_44 @ P1_44 @ D12p_44@ P2_44
     #Use TR for extracting power coefficients
     [_, _, Ss_44, Sp_44] = TR(Ms_44, Mp_44, rk0_44, perpen_rk0_44, rk2_44, perpen_rk2_44)
     
     Rs12_44[i] = Ss_44[0,0]
     Rp21_44[i] = Sp_44[1,1]
     Ts12_44[i] = Ss_44[0,1]
     Tp21_44[i] = Sp_44[1,0]   
     
     Rs_Ts_44[i] = Ss_44[0,0] + Ss_44[0,1]
     Rp_Tp_44[i] = Sp_44[1,1] + Sp_44[1,0]
     
#Plots using 44 as the angle 
plt.plot(d/lambda0, Rs12_44, linestyle='dashed', color='blue', label= 'Rs44', marker='o', markersize=.5)      
plt.plot(d/lambda0, Rp21_44 , linestyle='dashed', color= 'red', label = 'Rp44', marker='x', markersize=4)                    
plt.plot(d/lambda0, Ts12_44, linestyle='solid', color='blue', label = 'Ts44',marker='o', markersize=.5)                 
plt.plot(d/lambda0, Tp21_44, linestyle='solid', color= 'red', label= 'Tp44', marker='x', markersize=4) 

#R and T plots using 44 as the angle
plt.plot(d/lambda0, Rs_Ts_44, color='black', label= 'RsTs44', marker='o', markersize=1)   
plt.plot(d/lambda0, Rp_Tp_44, color= 'black', label = 'RpTp44', marker='x' , markersize=1)    
     
#loop using 46 degrees
theta3 = np.deg2rad(46)    #46.2644
for i, thickness in enumerate(d):
    #wavelength in terms of lambda
     
     [P0_46, rk0_46, perpen_rk0_46, parallel_rk, k0] = Propagation_Matrix(1, 1.5, 0, lambda0, parallel_rk, theta2)
     [P1_46, rk1_46, perpen_rk1_46, parallel_rk, k0] = Propagation_Matrix(2, 1.0, thickness, lambda0, parallel_rk,  theta2)
     [P2_46, rk2_46, perpen_rk2_46, parallel_rk, k0] = Propagation_Matrix(3, 1.5, 0, lambda0, parallel_rk, theta2)
     
     [D01s_46, D01p_46, s01s_46, s01p_46, SS01s_46, SS01p_46] = TransmissionMatrix(rk0_46, rk1_46, perpen_rk0_46, perpen_rk1_46)
     [D12s_46, D12p_46, s12s_46, s12p_46, SS12s_46, SS12p_46] = TransmissionMatrix(rk1_46, rk2_46, perpen_rk1_46, perpen_rk2_46)
     
     Ms_46 = P0_46 @ D01s_46 @ P1_46 @ D12s_46 @ P2_46
     Mp_46 = P0_46 @ D01p_46 @ P1_46 @ D12p_46@ P2_46
     #Use TR for extracting power coefficients
     [_, _, Ss_46, Sp_46] = TR(Ms_46, Mp_46, rk0_46, perpen_rk0_46, rk2_46, perpen_rk2_46)
     
     Rs12_46[i] = Ss_46[0,0]
     Rp21_46[i] = Sp_46[1,1]
     Ts12_46[i] = Ss_46[0,1]
     Tp21_46[i] = Sp_46[1,0]   
     
     Rs_Ts_46[i] = Ss_46[0,0] + Ss_46[0,1]
     Rp_Tp_46[i] = Sp_46[1,1] + Sp_46[1,0]
     
#Plots using 46 as the angle 
plt.plot(d/lambda0, Rs12_46, linestyle='dashed', color='blue', label= 'Rs46', marker='o', markersize=3, linewidth=.5)      
plt.plot(d/lambda0, Rp21_46 , linestyle='dashed', color= 'red', label = 'Rp46', marker='x', markersize=4)                    
plt.plot(d/lambda0, Ts12_46, linestyle='solid', color='blue', label = 'Ts46',marker='o', markersize=3)                 
plt.plot(d/lambda0, Tp21_46, linestyle='solid', color= 'red', label= 'Tp46', marker='x', markersize=4) 
#R and T plots
plt.plot(d/lambda0, Rs_Ts_46, linestyle='dashed', color='black', label= 'RsTs46', markersize=3 )   
plt.plot(d/lambda0, Rp_Tp_46, linestyle='solid', color= 'black', label = 'RpTp46', markersize=3 )    

#Pretty-ing the plots!!!
plt.legend(prop={'size':6})
plt.title("Evanescence Test: 1.5 -> 1.0 -> 1.5")
plt.xlabel("d in terms of lambda")
plt.ylabel("Power Coefficients")
plt.ylim(0,1.2)
plt.xlim(0,3)
plt.show()