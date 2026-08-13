# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:37:59 2026

@author: Mariah Ellis

The purpose of this script was to extract the reflective index of graphene as a function call later, from a yaml file.


"""

import yaml 
import numpy as np
import matplotlib.pyplot as plt

def graphene_yaml(file_name: str):
    with open("C:\\Users\\maria\\OneDrive\\Desktop\\REU\\Research  Code\\graphene_1L_Weber.yml", "r") as file:
        
        wavelength = []
        real = []
        imag = []
        try:
            data = yaml.safe_load(file)
           # print(data)
        except yaml.YAMLError as error: 
            print(f"Error parsing YAML:  {error} ")
                  
    raw_data = data["DATA"][0]["data"]
    
    for line in raw_data.splitlines():
        wavelength_values, real_values, imag_values = map(float, line.split())
        
        
        wavelength.append(wavelength_values)
        real.append(real_values)
        imag.append(imag_values)
           
   
      
    # #table data
    plt.plot(wavelength, real)
    plt.plot(wavelength, imag)
    
    #interpolaitng the table
    values = np.arange(400e-3, 800e-3, 1e-3)
    
    real_interp = np.interp(values, wavelength, real)
    imag_interp = np.interp(values,wavelength, imag)
    
    #interp graph
    plt.scatter(values,real_interp(values), label='n', marker='o')
    plt.scatter(values, imag_interp(values),label='k', marker='o')
    
    full_data = real_interp + imag_interp*1j
     
    return full_data


