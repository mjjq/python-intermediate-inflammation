"""Module containing mechanism for calculating standard deviation between datasets.
"""

import numpy as np

from inflammation import models, views
from inflammation.csv_data_source import CSVDataSource


def compute_standard_deviation_by_day(data):
    """
    Calculate the standard deviation of inflammation data by day.
    """
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation


def analyse_data_from_data_source(data_source: CSVDataSource):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    data = data_source.load_data()

    graph_data = {
        "standard deviation by day": compute_standard_deviation_by_day(data)
    }

    return graph_data


def analyse_data(data_dir: str):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    data_source = CSVDataSource(data_dir)
    return analyse_data_from_data_source(data_source)



