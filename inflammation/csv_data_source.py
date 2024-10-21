import glob
import os

from inflammation.models import load_csv

class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data(self):
        """
        Acquire data from a directory, format it into a list

        :param data_dir: Directory containing the data of .csv files (filenames must
        start with "inflammation")

        :return: List of data from each file.
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation csv's found in path {self.data_dir}")
        return map(load_csv, data_file_paths)