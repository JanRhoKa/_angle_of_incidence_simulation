import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def plot_angle_simulation(time_intervals, sampling_time, convolution_list, angles_simulation, function_name, panel):
    """
        Plotting function for aoi simulation
    """
  
    # angle min and max
    min_angles = angles_simulation.min()
    max_angles = angles_simulation.max()

    # convert time intervals to ns
    time_intervals = time_intervals * sampling_time / 1e-9  

    # set colors
    color_dict = dict(zip(angles_simulation, sns.color_palette("crest", n_colors=len(angles_simulation))))

    peak_pos = np.argmax(convolution_list)
    peak_time = time_intervals[peak_pos]
    
    # plot convolution
    for i, convolution in enumerate(convolution_list):   

        x_time = time_intervals - peak_time

        ax = sns.lineplot(x=x_time, y=convolution, color=color_dict[angles_simulation[i]])
        plt.axvline(x=x_time[np.argmax(convolution)], color=color_dict[angles_simulation[i]], linewidth=0.75, linestyle='dashed')

    # add colorbar
    cbar = ax.figure.colorbar(plt.cm.ScalarMappable(cmap="crest", norm=plt.Normalize(min_angles, max_angles)), ax=ax)
    cbar.set_label('Angle of incidence [deg]')

    # set plot info
    ax.set_xlim((-2, 2))
    ax.set_yticklabels([])
    ax.set_ylabel("Signal amplitude")
    ax.set_xlabel("Time in sample intervals [ns]")
    ax.set_title(f"Simulation of {function_name}")
    ax.text(0, 1.05, panel, fontsize=25, transform=ax.transAxes)

    return ax


def plot_ranging_curve_green(angles_selected, range_list, adjusted_range_list, function_name):
    """
        Plot theoretical ranging offset based on the maximum amplitude

    """

    # plot relation ranging and angles
    ax = sns.lineplot(x=angles_selected, y=range_list, color="#006699")
    ax = sns.lineplot(x=angles_selected, y=adjusted_range_list, color="#007E71")

    # add axis inofrmation
    ax.set_ylim((-0.01, 0.15))
    ax.set_ylabel("Distance [m]")
    ax.set_xlabel("Angle of incidence [deg]")

    # add legend
    ax.legend(handles=[mpatches.Patch(color='#006699', label='Beam distance'), mpatches.Patch(color='#007E71', label='Normal distance')])

    ax.set_title("Ranging for " + function_name)


def plot_houses_attributes(las_df, hue_attribute, hue_norm, cbar_title, title, panel, palette="viridis"):
    """
        Scatter plot of an top view of the point cloud dataset
    """

    ax = sns.scatterplot(x=las_df["y"].values, y=las_df["x"].values, linewidth=0, hue=las_df[hue_attribute], hue_norm=hue_norm, palette=palette, s=10, legend=False)

    # add colorbar
    cbar = ax.figure.colorbar(plt.cm.ScalarMappable(cmap=palette, norm=plt.Normalize(hue_norm[0], hue_norm[1])), ax=ax)
    cbar.set_label(cbar_title)

    # add plot info
    ax.axis('equal')
    ax.set_title(title)
    ax.set_xlabel("Distance [m]")
    ax.set_ylabel("Distance [m]")
    ax.text(0, 1.05, panel, fontsize=25, transform=ax.transAxes)

    return ax