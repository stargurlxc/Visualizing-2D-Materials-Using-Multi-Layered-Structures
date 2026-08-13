# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:37:59 2026

@author: maria
"""

import yaml 
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


wavelength = []
real = []
imag = []
comp = []


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
    
#interpolating function
real_interp = interp1d(wavelength, real)
imag_interp = interp1d(wavelength, imag)


#table data
plt.plot(wavelength, real)
plt.plot(wavelength, imag)

#interpolaitng the table
values = np.arange(400e-3, 800e-3, 1e-3)

interp_data1 = np.interp(values, wavelength, real)
interp_data2 = np.interp(values,wavelength, imag)

comp_data= np.zeros((len(interp_data1), len(interp_data2)))
#interp graph
plt.scatter(values,real_interp(values), label='n', marker='o')
plt.scatter(values, imag_interp(values),label='k', marker='o')

full_data = interp_data1 + interp_data2*1j
 
comp.append(interp_data1 + interp_data2)

plt.show()