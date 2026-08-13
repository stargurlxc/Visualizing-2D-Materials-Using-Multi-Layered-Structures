# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:28:49 2026

@author: Mariah Ellis


The purpose of this script was to create functions that will calculate propagation, 
transmission, and scattering matrices, to calculate the Fresnel reflection and
transmission coefficients of  a multi-layered structure. Reflection and transmission 
are separated into s-polarization and p-polarization.


The propagation matrix calculates the incidence/reflection/transmission of light in 
separate mediums. In order to calculate reflection and transmission of light in a multi-layered 
system using this script, all propagation matrices need to be called before the transmission matrices.


The transmission matrix calculates the incidence/reflection/transmission of light from one interface to another.
The TransmissionMatrix function inputs are based off of what the Propagation_Matrix produces. 


"""

import numpy as np

#input order: 
#number of layers, index of medium, thickness of medium, parallel component of k (typically set to 0), incidient angle need to be terms of rad
def Propagation_Matrix(layer, n, d, wavelength, parallel_rk, incident_angle):    
    rk = n
    k0 = (2 * np.pi) / wavelength
    if layer == 1:
        parallel_rk = n.real * np.sin(incident_angle)      #has to be real
        
    perpen_rk =  np.sqrt(rk**2 - parallel_rk**2 + 0j)   #complex to avoid scalar error
    
    element00 = np.exp(-1j * k0 * perpen_rk * d)
    element11 = np.exp(+1j * k0 * perpen_rk * d)   # k0 * rk's = k
    
    prop_matrix =  np.array([[element00, 0],
                      [0, element11]])
    
    return prop_matrix, rk, perpen_rk, parallel_rk, k0
    
#inputs are automatically calculated from the propagation matrices
def TransmissionMatrix(rk1, rk2, perpen_rk1, perpen_rk2):  
    #rs and ts setup
    num_s = perpen_rk1 - perpen_rk2     
    denom_s = perpen_rk1 + perpen_rk2
    
    #rp and tp setup
    num_p = (rk2/rk1)*perpen_rk1 - (rk1/rk2)*perpen_rk2
    denom_p = (rk2/rk1)*perpen_rk1 + (rk1/rk2)*perpen_rk2
    
    rs12 = num_s / denom_s
    rs21 = -num_s / denom_s
    ts12 = (2 * perpen_rk1) / denom_s
    ts21 = (2 * perpen_rk2) / denom_s 
    
    rp12 = num_p / denom_p
    rp21 = -num_p / denom_p
    tp12 = (2 * perpen_rk1) / denom_p
    tp21 = (2 * perpen_rk2) / denom_p        
    
    #d matrix
    p_matrix = (1 / tp12) * (np.array([[1, rp12],
                       [rp12, 1]]))
    s_matrix = (1 / ts12) * np.array([[1, rs12],
                       [rs12, 1]])
    
    #scattering matrix
    scattering_p_matrix = np.array([[rp12, tp12],
                       [tp21, rp21]])
    scattering_s_matrix = np.array([[rs12, ts12],
                       [ts21, rs21]])
    
    Rs12 = (abs(rs12))**2
    Rs21 = (abs(rs21))**2
    Rp12 = (abs(rp12))**2
    Rp21 = (abs(rp21))**2
    
    Ts12 = ((np.conjugate(perpen_rk2)/ np.conjugate(perpen_rk1)) * (abs(ts12)**2)).real
    Ts21 = ((np.conjugate(perpen_rk2)/ np.conjugate(perpen_rk1)) * (abs(ts21)**2)).real     #kz is the perpendicular component
    Tp12 = ((rk1**2 / (abs(rk1)**2)) * ((np.conjugate(rk2)**2)/(abs(rk2)**2)) * ((perpen_rk2 /perpen_rk1) * (abs(tp12)**2))).real
    Tp21 = (((rk1**2 / (abs(rk1)**2)) * ((np.conjugate(rk2)**2)/(abs(rk2)**2)) * (perpen_rk2 /perpen_rk1)) * (abs(tp21)**2)).real

    sPower_matrix = np.array([[Rs12, Ts12],
                          [Ts21 ,Rs21]])
    
    pPower_matrix = np.array([[Rp12, Tp12],
                              [Tp21, Rp21]])      
   
    return s_matrix, p_matrix, scattering_s_matrix, scattering_p_matrix, sPower_matrix, pPower_matrix

#used to calculate r, t, R, T from the M's
def TR(Ms, Mp, rk0, perpen_rk0, rk3, perpen_rk3):
    
    rs12 = Ms[0,1] / Ms[0,0]
    rs21 = -1 * Ms[0,1] / Ms[0,0]
    
    rp12 = Mp[0,1] / Mp[0,0]
    rp21 = -1 * Mp[0,1] / Mp[0,0]
    
    ts12 = 1 / Ms[0,0]
    ts21 = np.linalg.det(Ms)/ Ms[0,0]
    
    tp12 = 1 / Mp[0,0]
    tp21 = np.linalg.det(Mp)/ Mp[0,0]  #calculates det of matrix
    
    #Power coefficients for M amplitude coefficients
    Rs12 = abs(rs12)**2
    Rs21 = abs(rs21)**2
    Rp12 = abs(rp12)**2
    Rp21 = abs(rp21)**2
    Ts12 = ((np.conjugate(perpen_rk3)/ np.conjugate(perpen_rk0)) * (abs(ts12)**2)).real
    Ts21 = ((np.conjugate(perpen_rk3)/ np.conjugate(perpen_rk0)) * (abs(ts21)**2)).real     #kz is the perpendicular component
    Tp12 = ((rk0**2 / (abs(rk0)**2)) * ((np.conjugate(rk3)**2)/(abs(rk3)**2)) * ((perpen_rk3 /complex(perpen_rk0)) * (abs(tp12)**2))).real
    Tp21 = (((rk0**2 / (abs(rk0)**2)) * ((np.conjugate(rk3)**2)/(abs(rk3)**2)) * (perpen_rk3 /perpen_rk0)) * (abs(tp21)**2)).real
    
    scattering_p_matrix = np.array([[rp12, tp12],
                       [tp21, rp21]])
    scattering_s_matrix = np.array([[rs12, ts12],
                       [ts21, rs21]])
    
    scattering_sPower_matrix = np.array([[Rs12, Ts12],
                          [Ts21 ,Rs21]])
    
    scattering_pPower_matrix = np.array([[Rp12, Tp12],
                              [Tp21, Rp21]])    
    
    return scattering_s_matrix, scattering_p_matrix, scattering_sPower_matrix, scattering_pPower_matrix