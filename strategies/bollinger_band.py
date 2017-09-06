import pandas as pd

def bollinger_band(series,sdv_factor, avg_period, period):
    sma = pd.rolling_mean(series, avg_period)
    standard_dev = pd.rolling_std(series, period, ddof = 0)
    upper_band = sma + standard_dev * sdv_factor
    lower_band = sma - standard_dev * sdv_factor
    bandwidth = upper_band - lower_band
    return upper_band, lower_band