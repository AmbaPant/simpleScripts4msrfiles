This repo contains simple scripts to 
1. run multiple runs of musrfit and save fitted times spectra output data in .dat format
2. extract fitted parameters from .msr files and write in a .txt file
3. plot time spectra saved in .dat
4. plot extracted parameters of .txt file. for example temperature-dependent behavior

------------
what you need to know/do.

make a template msrfile like "tempt-msrfile.msr"

path of your musr data location in tempt-msrfile.msr

revise T and runNumbers 

edit and run run-musrfit-script.py

copy .msr files from "msrfitfiles.txt" and edit "extract..ipynb" file

run "extract..ipynb" in jupyter (or make .py and run)

copy .dat files from "datfitfiles.txt" and edit plot-tSpectra...ipynb and run

edit "plot-Tdependent-...ipynb", put .txt file name created from "extract....ipynb" and run
  


