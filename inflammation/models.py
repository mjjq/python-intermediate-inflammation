"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import json
import numpy as np

class Patient:
    def __init__(self, name):
        self.name = name

def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=",")


def load_json(filename):
    """Load a numpy array from a JSON document.

    Expected format:
    [
        {
            observations: [0, 1]
        },
        {
            observations: [0, 2]
        }
    ]

    :param filename: Filename of CSV to load

    """
    with open(filename, "r", encoding="utf-8") as file:
        data_as_json = json.load(file)
        return [np.array(entry["observations"]) for entry in data_as_json]


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    
    :param data: 2D array of values to perform mean
    :returns: 1D array of values contains means along first axis of data
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.
    
    :param data: Array of values to perform max
    :returns: 1D array of values contains maxes along first axis of data
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.
    
    :param data: Array of values to perform min
    :returns: 1D array of values contains mins along first axis of data
    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.

    :param data: 2D array to be normalised
    :returns: Normalised 2D array
    """
    maxima = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / maxima[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised
  
def standard_deviation(data):
    """Computes and returns standard deviation for data."""
    if len(data)==0:
        return {'standard deviation': 0.0}
    
    mmm = np.mean(data, axis=0)
    devs = []
    for entry in data:
        devs.append((entry - mmm) * (entry - mmm))

    s_dev2 = sum(devs) / len(data)
    return {'standard deviation': s_dev2}

  
def standard_deviation(data):
    """Computes and returns standard deviation for data."""
    if len(data)==0:
        return {'standard deviation': 0.0}
    
    mmm = np.mean(data, axis=0)
    devs = []
    for entry in data:
        devs.append((entry - mmm) * (entry - mmm))

    s_dev2 = sum(devs) / len(data)
    return {'standard deviation': s_dev2}

def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.

    :param data: 2D array to be normalised
    :returns: Normalised 2D array
    """
    maxima = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / maxima[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised