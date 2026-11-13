import numpy as np


def get_range_shift(time_intervals, sampling_time, convolution_list,angles_simulation):
    """
        _summary_
    """

    # convert time intervals to ns (from SI)
    time_intervals = time_intervals * sampling_time / 1e-9   
    
    # add all info to lists
    peak_pos = np.argmax(convolution_list[0])
    peak_time = time_intervals[peak_pos]

    range_list, adjusted_range_list = [], []
    for i, convolution in enumerate(convolution_list):

        time_between_peaks = time_intervals[np.argmax(convolution)] - peak_time

        range_list.append(time_between_peaks * 1e-9 * 299792458)
        adjusted_range_list.append(time_between_peaks * 1e-9 * 299792458 * np.cos(np.deg2rad(angles_simulation[i])))

    return range_list, adjusted_range_list