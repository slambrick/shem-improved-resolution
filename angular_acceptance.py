#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:05:27 2026

@author: Sam Lambrick

This script performs a quick estimation of the effect on the detection of
diffraction of the angular acceptence of the new high-resolution pinhole-
plate.
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants (SI units)
k_B = 1.380649e-23       # Boltzmann constant [J/K]
hbar = 1.054571817e-34   # Reduced Planck constant [J·s]
u_to_kg = 1.66053906660e-27  # Atomic mass unit [kg]

# Experimental parameters
T = 293.15              # Temperature [K] (20°C)
theta_in_deg = 45.0     # Incidence angle [degrees]
theta_center_deg = 45.0 # Detector center angle [degrees]

# Material parameters for LiF
LiF_lattice_parameter = 4.027e-10  # [m] (4.027 Å)

# Calculate helium atom properties
m_He = 4.0026 * u_to_kg  # Mass of helium-4 atom [kg]
E = (5.0 / 3.0) * k_B * T  # Energy of thermal helium [J]
p = np.sqrt(2 * m_He * E)  # Momentum [kg·m/s]
k = p / hbar  # Wavevector magnitude [m^-1]

# Calculate reciprocal lattice spacing for LiF [110] direction
# For cubic lattice, [110] direction has period d = a / sqrt(2)
d_110 = LiF_lattice_parameter / np.sqrt(2)
G = 2 * np.pi / d_110  # Reciprocal lattice spacing [m^-1]

# Convert incidence angle to radians
theta_in = np.radians(theta_in_deg)

# Calculate the positions in outgoing angles for the diffraction peaks
# For reflection geometry, ΔK = k (sin(theta_out) - sin(theta_in)) = n * G
# => sin(theta_out) = sin(theta_in) + (n * G / k)

# Find valid diffraction orders
n_values = np.arange(-10, 11)  # Range of orders to check
valid_peaks = []

for n in n_values:
    sin_theta_out = np.sin(theta_in) + (n * G / k)
    if -1.0 <= sin_theta_out <= 1.0:
        theta_out = np.degrees(np.arcsin(sin_theta_out))
        # Only keep positive angles between 0 and 90 degrees
        if 0 <= theta_out <= 90:
            valid_peaks.append((n, theta_out))

# Detector acceptance parameters
detector_acceptance = 37/2  # Half-acceptance in degrees
detector_min = theta_center_deg - detector_acceptance
detector_max = theta_center_deg + detector_acceptance

# Calculate K range for detector acceptance (in Å^-1)
detector_min_rad = np.radians(detector_min)
detector_max_rad = np.radians(detector_max)
K_min = k * (np.sin(detector_min_rad) - np.sin(theta_in)) / 1e10
K_max = k * (np.sin(detector_max_rad) - np.sin(theta_in)) / 1e10
K_range = K_max - K_min

# Create figure and axis using OOP
fig, ax = plt.subplots(figsize=(10, 6))
for n, angle in valid_peaks:
    ax.axvline(x=angle, color='blue', linestyle='--', linewidth=1.5)
    ax.text(angle, 0.95, f'n={n}', ha='center', va='top', fontsize=10)

# Define conversion functions between angle and K (in Å^-1)
def angle_to_K(theta_deg):
    theta_rad = np.radians(theta_deg)
    return k * (np.sin(theta_rad) - np.sin(theta_in)) / 1e10  # Convert to Å^-1

def K_to_angle(K_val):
    return np.degrees(np.arcsin(K_val * 1e10 / k + np.sin(theta_in)))

# Create secondary x-axis at the top for K values in Å^-1
ax2 = ax.secondary_xaxis('top', functions=(angle_to_K, K_to_angle))
ax2.set_xlabel('K (Å$^{-1}$)')

# Add detector aperture shaded area
ax.axvspan(detector_min, detector_max, color='red', alpha=0.3, label=f'Detector acceptance (45° ± {detector_acceptance}°)')
ax.set_xlabel('Outgoing Angle (degrees)', fontsize=12)
ax.set_ylabel('Arbitrary', fontsize=12)
ax.set_title('Diffraction Peaks for LiF [110] Direction\n(SHeM, He beam at 20°C, 90° scattering geometry)', fontsize=13, pad=20)
ax.set_xlim(0, 90)
ax.set_ylim(0, 1)
ax.grid(True, alpha=0.3)
ax.legend()

print("Diffraction peaks for LiF [110] direction:")
print("-" * 50)
for n, angle in valid_peaks:
    K_peak = n * G / 1e10  # Convert to Å^-1
    print(f"Order n={n:2d}: θ_out = {angle:6.2f}°, K = {K_peak:.4f} Å^-1")
print("-" * 50)

print(f"\nDetector acceptance range: {detector_min:.1f}° to {detector_max:.1f}°")
print(f"Corresponding K range: {K_min:.4f} Å^-1 to {K_max:.4f} Å^-1")
print(f"K range width: {K_range:.4f} Å^-1")

plt.show()