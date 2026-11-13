# Estimation of Incidence Angles and Ranging Accuracy via Simulation of Full-Waveform LiDAR

Dataset and simulation used in the study "Estimation of Incidence Angles and Ranging Accuracy via Simulation of Full-Waveform LiDAR" (Rhomberg-Kauert et al., 2026a).

## Study Abstract
Topo-bathymetric LiDAR has become a standard 3D geodata acquisition technique in geosciences with a wide range of applications in terrestrial and aquatic landscapes. In particular, the usage of short laser pulses with medium-sized footprints for bathymetric applications has seen growing attention over the past decade. These LiDAR configurations have shown higher relative changes in echo pulse width in relation to angle of incidence compared to standard topographic LiDAR using more collimated near-infrared lasers. Although angle-dependent changes in amplitude have been well documented, quantification of such a relation for the echo pulse width is still not entirely solved. By focusing on LiDAR with short and broad pulses, we can therefore use the higher relative changes of such systems together with numerical simulations to
quantify the relationship between the echo pulse width and the angle of incidence. The simulation developed in this study can be used to estimate neighborhood-independent angles of incidence from the recorded waveform, which enables the angle of incidence calculation during waveform processing. These waveform-derived angles are comparable to established methods based on the local point neighborhood, but generally display a higher variance leading to a mean absolute error of about 10° when compared to neighborhood-based angles of incidence. Using the developed simulation, we also explore angle-dependent shifts of the peak amplitude linked to potential ranging offsets. There, we were able to show ranging offsets of up to 12 cm for strongly asymmetric laser pulses at angles of 80° and no offsets for symmetric laser pulses, which provides new insights into the correctness of topo-bathymetric LiDAR systems. In conclusion, we present a detailed simulation framework which can be used to estimate incidence angles and quantify potential ranging offsets.

## Code setup

To run the notebooks and the provided code of the method, the following folder structure has to be implemented after downloading the files (to do: add link to dataset):

### _angle_of_incidence_simulation
- data
  - houses_processed.txt
  - houses.txt
- method
  - __init__.py
  - angle_of_incident.py
  - new_angle_simulation.py
  - plotting.py
  - ranging.py
- ranging_beam_div_range.ipynb
- rooftop_VQ880.ipynb
  

## References
Rhomberg-Kauert, J., Pöppl, F., Dammert, L., Pfennigbauer, M., & Mandlburger, G. (2026). Estimation of Incidence Angles and Ranging Accuracy via Simulation of Full-Waveform LiDAR. PFG–Journal of Photogrammetry, Remote Sensing and Geoinformation Science, 1-20; https://doi.org/10.1007/s41064-025-00375-6

Rhomberg-Kauert, J., Pöppl, F., Laasch, H., Pfennigbauer, M., & Mandlburger, G. (2026). Improved reflectance calculation in full-waveform LiDAR considering the angle of incidence. ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 11, 101-110; https://doi.org/10.5194/isprs-annals-XI-1-2026-101-2026
