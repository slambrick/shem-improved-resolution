# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:49:53 2024

@author: Sam Lambrick

This script calculates the optimal geometric configuration for the Cambridge
SHeM to achieve the desired beamwidth for the publication "High resolution 
large working distance scanning helium microscopy".
"""

import numpy as np
from numpy import sqrt, pi

f = 710e-6           # Working distance, m
sigma = 80e-6/2.355  # virtual source size (FWHM), m
L = 385e-3           # Skimmer pinhole distance, m
lmd = 0.57e-10       # Helium wavelength, m
phi_x = 300e-9/2.355*sqrt(2) # Target beam standard deviation, m
d = 470e-9           # Diameter of the pinhole, m
theta = 45*pi/180    # Incidece angle
print('Targeting {0:.0f}nm beam standard deviation'.format(phi_x*1e9))
d_0 = sqrt(6)*phi_x
print('Ideal pinhole diameter = {0:.0f}nm'.format(d_0*1e9))

a = 0.42*lmd*d/np.cos(theta)**2
beta_0 = sqrt(3/2)/(f)*sqrt( phi_x**2/2 - a**2/(6*phi_x**2) )
print('Optimal angular source size = {0:.2}rad\n'.format(beta_0))
beta = 2.18e-4
print('Actual pinhole size = {0:.0f}nm, actual angular source size = {0:.2}rad'.format(d*1e9, beta))

# Contributions from each factor
geom = d/(2*sqrt(3))
source= (1/np.cos(theta))*beta*f/sqrt(3)
diff = (1/np.cos(theta))**2 * 0.42*lmd*f/d
fwhm = sqrt(geom**2 + source**2 + diff**2)*2.355

print('Contributions to beam standard deviation from')
print('Geometry = {0:.0f}nm'.format(geom*1e9*2.355))
print('Source = {0:.0f}nm'.format(source*1e9*2.355))
print('Diffraction = {0:.0f}nm'.format(diff*1e9*2.355))
print('Predicted FWHM beamwidth = {0:.0f}nm'.format(fwhm*1e9))

# And do the "verical" axis calculation, this uses the standard form of the
# optimisation without the modifications for non-normal incidence
geom = d/(2*sqrt(3))
source = beta*f/sqrt(3)
diff = 0.42*lmd*f/d
fwhm = sqrt(geom**2 + source**2 + diff**2)*2.355
print('----------------------------')
print('For the vertical scanning direction')
print('Geometry = {0:.0f}nm'.format(geom*1e9*2.355))
print('Source = {0:.0f}nm'.format(source*1e9*2.355))
print('Diffraction = {0:.0f}nm'.format(diff*1e9*2.355))
print('Predicted FWHM beamwidth = {0:.0f}nm'.format(fwhm*1e9))

