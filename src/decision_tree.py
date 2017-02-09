"""Implement a decision tree in python."""

import numpy as np


def convert_csv(filename):
    """Covert from csv."""
    data = np.loadtxt(filename,
                      delimiter=',',
                      unpack=True,
                      skiprows=1,
                      usecols=(0, 1, 2, 3, 4))
    return data.transpose()


class Clf(object):
    """."""

    def __init__(self, iterable):
        """Initialize clf."""
        self.dataset = iterable
        self._size = len(iterable)
        self.num_cols = len(iterable[0])

    def _purity(self, splits, classes):
        """Determine the purity."""
        g_val = 0.0
        for split in splits:
            h_val = 0
            for class_val in classes:
                if len(split) != 0:
                    proportion = [row[-1] for row in split].count(class_val) / len(split)
                    h_val += (proportion * (1.0 - proportion))
            g_val += len(split) / self._size * h_val
        return g_val

    def _split(self, col_idx, boundary_val):
        """Split column data based on a boundary (data coordinate)."""
        left, right = [], []
        for row in self.dataset:
            if row[col_idx] <= boundary_val:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def _find_best_split(self, dataset, columns=[]):
        """Return the decision boundary where the total purity of both sides is best."""
        best_split = None
        best_purity = 1
        for col_idx in columns:
            for row_idx, row in enumerate(dataset):
                boundary_val = dataset[row_idx][col_idx]
                purity = self._purity(self._split(col_idx, boundary_val), (0, 1))
                if purity < best_purity:
                    best_purity = purity
                    best_split = (col_idx, boundary_val)
        return best_split
