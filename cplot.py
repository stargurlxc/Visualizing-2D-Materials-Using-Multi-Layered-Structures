# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:16:01 2026

@author: lloyd
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_contrast(x_data, y_data, xy_data, c_type):
    xy_data = np.rot90(xy_data)
    
    match c_type:
        case "bp":
            #force color scaellimts to be symmetrical positive and negative
            # so we can use the bipolar tabel red os + abd blue is -
            xy_min = np.min(xy_data)
            xy_max = np.max(xy_data)
            abs_max = max(abs(xy_min), abs(xy_max))
            plt.imshow(xy_data, 
                       extent=[np.amin(x_data), np.max(x_data), 
                               np.amin(y_data), np.max(y_data),],
                       cmap='coolwarm', vmin = -abs_max, vmax = abs_max,
                       aspect='auto')
        case "_":
            plt.imshow(xy_data, 
                       extent=[np.amin(x_data), np.max(x_data), 
                               np.amin(y_data), np.max(y_data),],
                       aspect='auto')


    plt.colorbar(label='Contrast')
    
    # #Pretty-ing the plots!!!
    # plt.legend(prop={'size':8})
    # plt.title("Reflectivity of air/graphene/SiO2/Si")
    # plt.xlabel("SiO2 thickness (nm)")
    # plt.ylabel("λ (nm)")
    # plt.show()