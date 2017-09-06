import pandas as pd

def stochastics_oscilator(high, low, close, period):
    higher_high = pd.rolling_max(high, period)
    lower_low = pd.rolling_min(low, period)
    stochastics_osci = (close - lower_low) / (higher_high - lower_low) * 100
    return stochastics_osci
