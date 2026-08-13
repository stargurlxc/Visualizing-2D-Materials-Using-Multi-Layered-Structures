# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:41:35 2026

@author: Mariah ELlis


The purpose of this script was to replicate plots on https://en.wikipedia.org/wiki/Fresnel_equations.
More specifically, to calculate the graph on Fresnel amplitude coefficients going from glass to air. 


"""

import numpy as np
import matplotlib.pyplot as plt 


#loop for incidient angles
angles = []
for angle in range(-1,90):
    angle+=1 
    angles.append(np.deg2rad(angle))

transmission_angle_values = []

#indices (medium change)
n1 = 1.5
n2 = 1.0

#index ratio
ratio = n2 / n1


#empty lists to store values l8r
rs_values = []
ts_values = []
rp_values = []
tp_values = []


#looping over the angles, and storing them to the empty lists
for theta_incident in angles:
    sin_of_theta = np.sin(theta_incident)
    cos_of_theta = np.cos(theta_incident)
    
    
    # calculating transmission angle (changed/bent/altered angle)
    #separate transmission angle for complex values
   # z = complex(1 - np.square((n1/n2) * sin_of_theta))
    transmission_angle = np.sqrt((1 - np.square((n1/n2) * sin_of_theta)) )  #might need to cut off past a certain value to account for total internal reflection
   

    #s polarization!   (reflected perpendicular to the plane)
    #amplitude reflection
    r_s = (n1*cos_of_theta - n2*transmission_angle) / (n1*cos_of_theta + n2*transmission_angle) 
    #amplitude(?) transmission
    t_s = (2 * n1 * cos_of_theta) / (n1*cos_of_theta + n2*transmission_angle)

    
    #p polarization   (reflected in the plane )
    r_p = ((n2 * cos_of_theta) - (n1 * transmission_angle)) /  ((n2 * cos_of_theta) + (n1 * transmission_angle))
    t_p = (2 * n1 * cos_of_theta) / ((n2 * cos_of_theta) + (n1 * transmission_angle))   #check this, max value should be 3???
    
    
    #store values to the previously empty lists 
    transmission_angle_values.append(transmission_angle)
    rs_values.append(r_s)
    ts_values.append(t_s)
    rp_values.append(r_p)
    tp_values.append(t_p)


#calculate brewsters angle; special angle where rp = 0   
brewster_angle = np.arctan(n2/n1)
b = np.rad2deg(brewster_angle)

#change radians back to degrees for plotting? might be unneccessary
angles_in_degrees = np.rad2deg(angles)


#Plots
rs_graph = plt.plot(angles_in_degrees, rs_values, color='blue',linestyle='dashed', linewidth=1, label='rs')
ts_graph = plt.plot(angles_in_degrees, ts_values, color='blue',linestyle='solid', linewidth=1, label='ts')
rp_graph = plt.plot(angles_in_degrees, rp_values, color='red',linestyle='dashed', linewidth=1, label='rp') 
tp_graph = plt.plot(angles_in_degrees, tp_values, color='red',linestyle='solid', linewidth=1, label='tp') 

#special case plots
#brewster's angle plot
plt.axvline(b, color='lightgreen',linestyle='dashed', label='Brewsters angle')


#Pretty-ing the plot!!
plt.legend(prop={'size':8})
plt.title("Fresnel Amplitude Coefficients  (Glass to Air)")
plt.xlabel("Angle of Incidence (deg)")
plt.ylabel("Amplitude Coefficient")
plt.ylim(-0.5, 3.0)
plt.xlim(0,90)
plt.grid(True)
plt.show()