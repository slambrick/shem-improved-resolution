# shem-improved-resolution
Data and analysis scripts supporting “High resolution large working distance scanning helium microscopy”

## Beamwidth measurement

Data and scripts for the measured beamwidth are in the `beamwidth_measurement` directory. 

 - `Beam_FWHM_sharing.m` matlab live script loads in the raw SHeM data, performs fits of error functions to the data and writes the results to `.csv` files
 - `point1.csv` contains the measured FWHMs and errors for point 1
 - `point2.csv` as above for point 2
 - `Resolution_plot.ipynb` creates the final plot for the paper and calculates the predicted beamwidths
 - `measured_beamwidth.pdf` is the figure of beamwidths for the paper
 - `2021_04_Source_further_350m` contains the raw SHeM data in `.dat`

