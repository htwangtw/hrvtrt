import numpy as np
from scipy.stats import zscore
from scipy import interpolate, signal


def clean_ibi(events, samping_rate, n=2):
    ibi = _ibi(events, samping_rate)
    for _ in range(n):
        # detect outlier and repalce with nan
        outliers = signal_outliers(ibi, samping_rate)
        time = np.cumsum(ibi)
        # interpolate nan
        f = interpolate.interp1d(
            time[~outliers], ibi[~outliers], "cubic", fill_value="extrapolate"
        )
        ibi = f(time)  # update
    return ibi


def _ibi(events, samping_rate):
    """Inter beat interval at msec scale."""
    return np.diff(events) / samping_rate * 1000


def signal_outliers(signal, samping_rate):
    """Number of outliers in Inter beat intervals."""
    return _rolling_mad(signal, int(0.5 * samping_rate))


def _mad(arr):
    """Median Absolute Deviation: a "Robust" version of standard deviation.
    Indices variabililty of the sample.
    https://en.wikipedia.org/wiki/Median_absolute_deviation
    """
    med = np.median(arr)
    return med, np.median(np.abs(arr - med))


def _rolling_mad(arr, window):
    """
    Rolling window MAD outlier detection on 1d array.
    """
    outliers = []
    for i in range(window, len(arr)):
        cur = arr[(i - window) : i]
        med, cur_mad = _mad(cur)
        cur_out = cur > (med + cur_mad * 3)
        idx = list(np.arange((i - window), i)[cur_out])
        outliers += idx
    outliers = list(set(outliers))

    # turn index into boolean
    bool_outliers = np.zeros(arr.shape[0], dtype=bool)
    bool_outliers[outliers] = True
    return bool_outliers
