# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:16:02 2026

@author: Mariah Ellis


The purpose of this script was to produce a plot of Graphene contrast 
while looping over the thickness of Graphene, while keeping SiO2 at either 90nm, 200nm, or 300nm



"""

import numpy as np
import matplotlib.pyplot as plt
from fixed_prop_and_trans_matrix import Propagation_Matrix, TransmissionMatrix, TR
import nk_yaml as lab
from cplot import plot_contrast


L = np.arange(400,750,1) # wavelength in microns

#graphene indexes
fn = "C:\\Users\\maria\\OneDrive\\Desktop\\REU\\Research  Code\\graphene_1L_Weber.yml"
[nk2, lam] = lab.read_nk(fn, L*1e-3)

#siO2 indexes
fn = "C:\\Users\\maria\\OneDrive\\Desktop\\REU\\Research  Code\\SiO2_fused_Malitson.yml"
[nk3, lam3] = lab.read_nk(fn, L*1e-3)

#si100 indexes
fn = "C:\\Users\\maria\\OneDrive\\Desktop\\REU\\Research  Code\\Si100_Jellison.yml"
[nk4, lam2] = lab.read_nk(fn, L*1e-3)

#getting vacuum indexes
fn = "C:\\Users\\maria\\OneDrive\\Desktop\\REU\\matrix2by2.py"
[nk1, lam] = lab.read_nk(fn, L*1e-3)

#thicknesses in nm
siO2_thickness = 90  
graphene_thickness = np.arange(0, 100, 1) 

parallel_rk = 0
incident_angle = np.deg2rad(0)

air_Rs12 = np.zeros((len(graphene_thickness), len(L)))
air_Rp12 = np.zeros((len(graphene_thickness), len(L)))
air_Ts12 = np.zeros((len(graphene_thickness), len(L)))
air_Tp12 = np.zeros((len(graphene_thickness), len(L)))

graphene_Rs12 = np.zeros((len(graphene_thickness), len(L)))
graphene_Rp12 = np.zeros((len(graphene_thickness), len(L)))
graphene_Ts12 = np.zeros((len(graphene_thickness), len(L)))
graphene_Tp12 = np.zeros((len(graphene_thickness), len(L)))


for n in range(2):
    for jj, thickness in enumerate(graphene_thickness):
        for ii, lam in enumerate(L):                    #looping over wavelength
            #air
            [P0, rk0, perpen_rk0, parallel_rk, k0] = Propagation_Matrix(1, nk1[ii], 0, lam, parallel_rk, incident_angle)
            #graphene                                                       2.6 + 1.3j
            if n == 1:
                [P1, rk1, perpen_rk1, parallel_rk, k0] = Propagation_Matrix(2, nk1[ii], thickness, lam, parallel_rk, incident_angle)
            else:
                [P1, rk1, perpen_rk1, parallel_rk, k0] = Propagation_Matrix(2, nk2[ii], thickness, lam, parallel_rk, incident_angle)
            #siO2
            [P2, rk2, perpen_rk2, parallel_rk, k0] = Propagation_Matrix(3, nk3[ii], siO2_thickness, lam, parallel_rk,  incident_angle)
            #si100
            [P3, rk3, perpen_rk3, parallel_rk, k0] = Propagation_Matrix(4, nk4[ii], 0, lam, parallel_rk,  incident_angle)
            
            [D01s, D01p, s01s, s01p, SS01s, SS01p] = TransmissionMatrix(rk0, rk1, perpen_rk0, perpen_rk1)
            [D12s, D12p, s12s, s12p, SS12s, SS12p] = TransmissionMatrix(rk1, rk2, perpen_rk1, perpen_rk2)
            [D23s, D23p, s23s, s23p, SS23s, SS23p] = TransmissionMatrix(rk2, rk3, perpen_rk2, perpen_rk3)
            
            Ms = D23s @ P2 @ D12s @ P1 @ D01s    #s polarization
            Mp = D23p @ P2 @ D12p @ P1 @ D01p    #p polarization
            
            #use rk's of first and last propagation matrices
            [ss, sp, Ss, Sp] = TR(Ms, Mp, rk0, perpen_rk0, rk3, perpen_rk3 )
            
            
            #layer 2 is same medium as layer 1
            if n == 1:
                air_Rs12[jj, ii] = Ss[0,0]
                air_Ts12[jj, ii] = Ss[0,1]
                
                air_Rp12[jj, ii] = Sp[0,0]
                air_Tp12[jj, ii] = Sp[0,1]
            #layer 2 is graphene
            else:
                graphene_Rs12[jj, ii] = Ss[0,0]
                graphene_Ts12[jj, ii] = Ss[0,1]
            
                graphene_Rp12[jj, ii] = Sp[0,0]
                graphene_Tp12[jj, ii] = Sp[0,1]
                
contrast = (air_Rs12 - graphene_Rs12 ) / air_Rs12


plot_contrast(graphene_thickness, L, contrast, '_')  
plt.xlabel("Graphene thickness (nm)")
plt.ylabel("λ (nm)")
plt.title("Graphene Contrast using 90 nm SiO₂")
plt.show()