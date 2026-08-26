# shem-improved-resolution
Data and analysis scripts supporting “High resolution large working distance scanning helium microscopy”

## Beamwidth measurement

Data and scripts for the measured beamwidth are in the `beamwidth_measurement` directory. 

 - `Beam_FWHM_sharing.m` matlab live script loads in the raw SHeM data, performs fits of error functions to the data and writes the results to `.csv` files
 - `point1.csv` contains the measured FWHMs and errors for point 1
 - `point2.csv` as above for point 2
 - `Resolution_plot.ipynb` creates the final plot for the paper and calculates the predicted beamwidths
 - `measured_beamwidth.pdf` is the figure of beamwidths for the paper
 - `estimated_SNR.pdf` is the figure of the SNR estimate as a function of working distance for the paper
 - `2021_04_Source_further_350m` contains the raw SHeM data as Matlab `.mat` files

## SHeM micrographs

Raw SHeM micrograph data for all the 2D micrographs shown in the paper are in the `shem_images` directory.

## Scripts

Some helper scripts are also included
 - `angular_acceptance.py` estimates the Delta K acceptence of the new high resolution pinhole plate
 - `do_optimisation.py` calculates the optimal parameters and predicts the beamwidth
 - `quick_resolution_plot.py` creates a graph showing resolution as a function of working distance for figure 1
