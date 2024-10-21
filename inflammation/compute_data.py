"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


def gather_data(data_dir: str):
    """
    Acquire data from a directory, format it into a list

    :param data_dir: Directory containing the data of .csv files (filenames must
    start with "inflammation")

    :return: List of data from each file.
    """
    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation csv's found in path {data_dir}")
    return map(models.load_csv, data_file_paths)

def compute_standard_deviation_by_day(data):
    """
    Calculate the standard deviation of inflammation data by day.
    """
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation

def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    data = gather_data(data_dir)

    graph_data = {
        "standard deviation by day": compute_standard_deviation_by_day(data)
    }

    return graph_data
