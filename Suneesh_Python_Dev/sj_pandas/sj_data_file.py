import pandas as pd


class SJDataFile:

    def __init__(self, filename):
        self._filename = filename
        self._df = pd.read_csv(filename)

    @property
    def filename(self):
        return self._filename

    @property
    def data(self):
        return self._df
