# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:47:41 2026

@author: Mariah Ellis

The purpose of this script was to extract graphene indexes and wavelength from a yaml file. 


"""

import yaml 
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


wavelength = []
real = []
imag = []
comp = []

 #thickness of mediums as an array
d = np.arange(0, 800e-9, 10e-9)

def graphene_yaml(file_name: str): 
    with open("C:\\Users\\maria\\OneDrive\\Desktop\\REU\\Research  Code\\graphene_1L_Weber.yml", "r") as file:
        try:
            data = yaml.safe_load(file)
            print(data)
        except yaml.YAMLError as error: 
            print(f"Error parsing YAML:  {error} ")
                  
    raw_data = data["DATA"][0]["data"]
    
    
    
    for line in raw_data.splitlines():
        wavelength_values, real_values, imag_values = map(float, line.split())
        
        wavelength.append(wavelength_values)
        real.append(real_values)
        imag.append(imag_values)
    for i, value in enumerate(d):
        
        #interpolating function
        real_interp = interp1d(wavelength, real)
        imag_interp = interp1d(wavelength, imag)
        
        
        #table data
        plt.plot(wavelength, real)
        plt.plot(wavelength, imag)
        
        #interpolaitng the table
        values = [400e-3, 410e-3, 420e-3, 430e-3,  440e-3, 450e-3, 460e-3, 470e-3, 480e-3, 
                           490e-3, 500e-3, 510e-3, 520e-3, 530e-3, 540e-3, 550e-3, 560e-3, 570e-3, 580e-3, 590e-3, 600e-3]
        
        interp_data_real = np.interp(values, wavelength, real)
        interp_data_imag = np.interp(values, wavelength, imag)
        #interp graph
        plt.scatter(values,real_interp(values), label='n', marker='o')
        plt.scatter(values, imag_interp(values),label='k', marker='o')
        
        plt.show()
        
        return interp_data_real, interp_data_imag