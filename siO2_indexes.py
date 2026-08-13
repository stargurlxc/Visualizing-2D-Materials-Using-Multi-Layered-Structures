# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:21:10 2026

@author: Mariah Ellis


The purpose of this script was to create a function that extracted the interpolation of siO2 reflective 
indexes from a yaml file.


"""
import os
import yaml 
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from pathlib import Path


#function for extracting data from yaml files! yippee
def open_yaml_file(file_name: str):
    #empty lists to store values in l8r
    wavelength  = []
    formula_results = []

    file_path = Path(file_name)
    
    with file_path.open('r') as file:
        try:
            data = yaml.safe_load(file)
            #print(data["DATA"])
        except yaml.YAMLError as error: 
            print(f"Error parsing YAML:  {error} ")
        
        
        coefficient_data =  data["DATA"][0]["coefficients"]
        coefficient_values = list(map(float, coefficient_data.split(' ')))
        
        #calculated in microns
        for lambdaa in np.arange(.21, 6.7, 1):
            wavelength.append(lambdaa)

    for x in wavelength:
        n = np.sqrt(1 + (((coefficient_values[1] * (x**2)) / (x**2 - (coefficient_values[2])**2)) + ((coefficient_values[3] * (x**2)) / ((x**2) - (coefficient_values[4])**2)) + ((coefficient_values[5] * (x**2)) / ((x**2) - (coefficient_values[6])**2))))
        formula_results.append(n)
        #table graph
        #plt.plot(wavelength, formula_results)

        #table graph
        #plt.plot(wavelength, formula_results)

    #interpolating function
    interp = interp1d(wavelength, formula_results)

    values = [.25, .6, 1, 1.4,1.7, 2.4, 3.0, 3.6, 4.0, 4.5, 5.5, ]
    #interpolation graph
    #plt.scatter(values, interp(values))
    
    return formula_results