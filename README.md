# basinsdatadirs
BASINS HUC data file move

The old BASINS HUC directory structure had a directory for each 8 digit HUC. The data files were in each HUC directory. The new deliverable from RESPEC has all the files in a single parent directory. This program creates directories named by the first 8 digits of the new file name. Then it moves the new files into their proper directory. 
