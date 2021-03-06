"""
Utilities for automated data checking.
"""

# Author: Alex Wozniakowski <wozn0001@e.ntu.edu.sg>

import os
import re
import numpy as np
import pandas as pd

import sklearn.utils.multiclass


def _check_X(X):
    """Check if the data matrix is using a pandas data representation."""

    assert isinstance(X, (pd.Series, pd.DataFrame))
    return X


def _check_X_y(X, y):
    """Check if the data matrix and the target(s) are using pandas data representations."""

    assert all(isinstance(var, (pd.Series, pd.DataFrame)) for var in [X, y])
    assert X.index.equals(y.index)
    assert any(sklearn.utils.multiclass.type_of_target(y) != target_type
           for target_type in ['continous', 'continuous-multioutput'])

    if X.ndim > 1:
        n_features = X.shape[-1]
    else:
        n_features = 1

    data = pd.concat([X, y], axis=1).dropna(how='any', axis=0)
    if sklearn.utils.multiclass.type_of_target(y) == 'continuous-multioutput':
        return data.iloc[:, :n_features], data.iloc[:, n_features:]
    else:
        return data.iloc[:, :n_features], data.iloc[:, n_features:].squeeze()


def _validate_data(X, y=None):
    """Bundles the pandas data checks."""

    if y is not None:
        out = _check_X_y(X, y)
    else:
        out = _check_X(X)
    return out


def _n_features(X):
    """Counts the number of features in the data matrix."""

    if X.ndim > 1:
        dim = X.shape[-1]
    else:
        dim = 1
    return dim


def _n_targets(y):
    """Counts the number of targets."""

    if y.ndim > 1:
        dim = y.shape[-1]
    else:
        dim = 1
    return dim


def _n_samples(y):
    """Counts the number of observations."""

    return y.shape[0]
