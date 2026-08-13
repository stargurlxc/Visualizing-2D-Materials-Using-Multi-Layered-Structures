# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:47:58 2026

@author: lloyd
"""
import numpy as np
import nk_yaml as lab

fn = "C:\\Users\\maria\\OneDrive\\Desktop\\REU\\Research  Code\\graphene_1L_Weber.yml"
L = np.arange(400,750,10)*1e-3 # wavelength in microns

[nk2, lam] = lab.read_nk(fn,L)


fn = "C:\\Users\\maria\\OneDrive\\Desktop\\REU\\Research  Code\\SiO2_fused_Malitson.yml"

[nk3, lam3] = lab.read_nk(fn,L)


fn = "C:\\Users\\maria\\OneDrive\\Desktop\\REU\\Research  Code\\Si100_Jellison.yml"

[nk4, lam2] = lab.read_nk(fn,L)


