import numpy as np

def p_heavy(t, tau):
    """
    Heavy tailed curve from the Carlsson et al. paper.
    """

    y = np.zeros_like(t)
    y[t>0] = (t[t>0] / tau)**2 * np.exp(-t[t>0] / tau)
    return y


def p_gauss(t, FWHM):
    """
    Gaussian pulse based on the FWHM maximum.
    """
    
    # transform FWHM into e**-2 threshold
    sigma = FWHM / (2 * np.sqrt(2*np.log(2)))

    return np.exp(-t**2 / (2 * sigma**2))


def p_homotpie(t, tau, FWHM, homotopie_term):
    """
    Homotopie between p and p_G for analysis of waveform influence on ranging
    """
    
    return homotopie_term * p_heavy(t, tau) + (1-homotopie_term) * p_gauss(t - 2 * tau, FWHM)


def h(t, alpha, w0):
    """ Incidence angle function. """

    # set basic parameters
    c = 299792458
    nanosecond = 1e-9  

    return np.cos(alpha) * np.sqrt(np.pi) * w0 * c / np.sin(alpha) * np.exp(-((c * t * nanosecond) / (w0 * np.tan(alpha)))**2)
            

def pulse_width(convolution):
    """ Get echo pulse width at e^{-2} -> T_{e^{-2}}. """

    return np.diff(np.where(np.diff(np.sign(convolution - convolution.max()/np.exp(2)))))[0][0]


def improved_angle_simulation(angles_selected, sampling_time, range, beam_divergence, FWHM=1.5, homotopie_term=0):
    """
        Angle of incidence simulation based on convolution of heavy-tailed curve and incidence angle function.
    """

    # set basic parameters
    nanosecond = 1e-9  

    # adjust oversampling depending on sampling time 1 ns vs 0.5 ns
    if sampling_time / nanosecond > 1:
        oversampling = 64
    else:
        oversampling = 32

    # time intervals selected by oversampling in units of ns
    time_intervals = np.arange(-100, 100, (sampling_time / oversampling) / nanosecond) 

    # set data based on scanner and paper 
    tau = FWHM / (2*np.sqrt(2*np.log(2)))
    footprint_radius = (range * beam_divergence) / 2  
    

    convolution_list, signal_width_simulation = [], []
    for angle in np.deg2rad(angles_selected):

        # create convolution as outlined in the angle of incidence paper
        if homotopie_term == 0:
            convolution = np.convolve(p_gauss(time_intervals, FWHM), h(time_intervals, angle, footprint_radius), mode='same')
        elif homotopie_term < 1:
            convolution = np.convolve(p_homotpie(time_intervals, tau, FWHM, homotopie_term), h(time_intervals, angle, footprint_radius), mode='same')
        else:
            convolution = np.convolve(p_heavy(time_intervals, tau), h(time_intervals, angle, footprint_radius), mode='same')

        # add convolution to list
        convolution_list.append(convolution)

        # get width of the signal
        signal_width_simulation.append(pulse_width(convolution))

    # adjust back to sample intervals due to oversamping
    signal_width_simulation = np.r_[signal_width_simulation]
    signal_width_simulation = signal_width_simulation / oversampling

    # transform signal width to ns
    signal_width_simulation = signal_width_simulation * sampling_time / nanosecond

    return convolution_list, time_intervals, signal_width_simulation

