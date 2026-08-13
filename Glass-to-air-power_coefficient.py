# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:09:58 2026

@author: Mariah ELlis


The purpose of this script was to replicate plots on https://en.wikipedia.org/wiki/Fresnel_equations.
More specifically, to calculate the Fresnel power coefficients going from glass to air. 


"""

import numpy as np
import matplotlib.pyplot as plt


#loop for incidient angles
angles = []
for angle in range(-1,90):
    angle+=1 
    angles.append(np.deg2rad(angle))

#mediums (glass to air)
n1 = 1.5
n2 = 1.0

#index ratio
ratio = n2 / n1

#empty lists to store values l8r
transmission_angle_values = []
rs_values = []
ts_values = []
rp_values = []
tp_values = []

Rs_values = []
Ts_values = []
Rp_values = []
Tp_values = []

for theta_incident in angles:
    sin_of_theta = np.sin(theta_incident)
    cos_of_theta = np.cos(theta_incident)
    
    
    #calculating transmission angle (changed/bent/altered angle)
    #separate transmission angle for complex values
    transmission_angle = np.sqrt(complex(1 - np.square((n1/n2) * sin_of_theta)))
   

    #s polarization!   (reflected perpendicular to the plane)
    #amplitude reflection coefficient
    r_s = (n1*cos_of_theta - n2*transmission_angle) / (n1*cos_of_theta + n2*transmission_angle) 
    #amplitude(?) transmission coefficient
    t_s = (2 * n1 * cos_of_theta) / (n1*cos_of_theta + n2*transmission_angle)

    
    #p polarization   (reflected in the plane )
    r_p = ((n2 * cos_of_theta) - (n1 * transmission_angle)) /  ((n2 * cos_of_theta) + (n1 * transmission_angle))
    t_p = (2 * n1 * cos_of_theta) / ((n2 * cos_of_theta) + (n1 * transmission_angle))
    
    
    #transmittances/reflectances graph
    #power reflection coefficient
    Rs = abs(np.square(r_s))
    Rp = abs(np.square(r_p))
    
    #power transmission coefficient 
    Ts = ((n2 * transmission_angle) / (n1 * cos_of_theta)) * (abs(np.square(t_s)))
    Tp = ((n2 * transmission_angle) / (n1 * cos_of_theta)) * (abs(np.square(t_p)))

    #store values to the previously empty lists 
    transmission_angle_values.append(transmission_angle)
    rs_values.append(r_s)
    ts_values.append(t_s)
    rp_values.append(r_p)
    tp_values.append(t_p)
    
    Rs_values.append(Rs)
    Ts_values.append(Ts)
    Rp_values.append(Rp)
    Tp_values.append(Tp)

#calculate brewsters angle; special angle where rp = 0   
brewster_angle = np.arctan(n2/n1)
b = np.rad2deg(brewster_angle)

#change radians back to degrees for plotting
angles_in_degrees = np.rad2deg(angles)
    

Rs_graph = plt.plot(angles_in_degrees, Rs_values, color='blue', linestyle='dashed', linewidth=2, label='Rs')
Ts_graph = plt.plot(angles_in_degrees, Ts_values, color='blue', linestyle='solid', linewidth=2, label='Ts')
Rp_graph = plt.plot(angles_in_degrees, Rp_values,  color='red', linestyle='dashed', linewidth=2, label='Rp')
Tp_graph = plt.plot(angles_in_degrees, Tp_values, color='red', linestyle='solid', linewidth=2, label='Tp')

#brewster's angle plot
b_angle = plt.axvline(b, color='lightgreen',linestyle='dashed', label='Brewsters angle')

#Pretty-ing the plot!!
plt.legend(prop={'size':8})
plt.title("Fresnel Transmittances/Reflectances  (Glass to Air)")
plt.xlabel("Angle of Incidence (deg)")
plt.ylabel("Power Coefficient")
plt.ylim(0, 1)
plt.xlim(0, 90)
plt.grid(True)    
plt.show()