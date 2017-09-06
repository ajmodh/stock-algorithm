import pandas

def sma(price,  period):
    return pandas.rolling_mean(price, period)
