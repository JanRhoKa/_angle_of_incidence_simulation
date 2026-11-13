import numpy as np
from numpy.linalg import norm


def get_angle_of_incident(beam_vector, normal_vector):
    """
        Calculate the angles of incident for each point in the point cloud based on the beam and normal vectors.

    """

    angles = []
    for vectors in zip(beam_vector.T, normal_vector.T):
        u = vectors[0]
        v = vectors[1]

        # calculate the angle of incident if both vectors are not zero
        if (norm(u) * norm(v)) != 0:
            angle = np.arccos(np.dot(u, v) / (norm(u) * norm(v)))
        else:
            angle = np.nan
            
        # transform angle in degree
        angle = np.rad2deg(angle)
        angles.append(angle)
    
    # normalize angles for the interval [0, 90]
    angles = [180 - angle if angle > 90 else angle for angle in angles]

    return angles

    

def get_pulse_width_angles(las_df, angles_simulation, pulse_width_simulation):
    """
        Get the angle of incidence based on the FWHM and the angle of incidence simulation.
    """

    # get pulse width (FWHM)
    curve_width_list = las_df["PulseWidth"].values

    pulse_width_angles_list = []
    for width in curve_width_list:

        # remove all nans from width list
        width = np.nan_to_num(width, nan=-1)

        if width >= 0:     
            
            # get all new estimation of incident angles
            min_index = np.argmin(np.abs(np.array(pulse_width_simulation) - width))
            
            # get all new estimation of incident angles
            pulse_width_angles = angles_simulation[min_index]
            
            # add angles to list
            pulse_width_angles_list.append(pulse_width_angles)
        else:
            pulse_width_angles_list.append(np.nan)

    return pulse_width_angles_list
