Version: 1.0
Generation date: 2015-07-20

This archive contains all files necessary to reproduce the software phantom employed at the ISMRM Fiber Tractography Challenge 2015 (http://www.tractometer.org/ismrm_2015_challenge/).

To simulate the dataset, an up-to-date version of MITK Diffusion is necessary (the last binary release 2014.10.02 will not be usable since new features have been added since this release). You should either build the current master of MITK yourself (http://docs.mitk.org/nightly/BuildInstructionsPage.html, make sure that all cmake options necessary for MITK Diffusion are enabled) or wait for the next binary release. Cmake options to enable on the superbuild level are Boost, HDF5 and Vigra as well as later on the MITK build level every option that contains "diffusion".

If a suitable version of MITK Diffusion is running, the simulation is started with the following steps:

1. Switch to the "Synthetic Data" perspective and there to the "Signal Generation" tab in the Fiberfox view.
2. Load the tracts (Fibers.fib) and the template diffusion-weighted image (TemplateDWI.dwi)
3. Use the button in the Fiberfox view to load the parameter file (param.ffp).
4. Check the screenshots in the archive if all options are set correctly, then start the simulation.

Use the user manual to get more information about the parameters and the general usage of Fiberfox (http://docs.mitk.org/nightly/org_mitk_views_fiberfoxview.html).


When using Fiberfox in one of your publications, please cite http://www.ncbi.nlm.nih.gov/pubmed/24323973. 
