import pandas as pd

def average_gain_loss(gain, avg_gain, index, period):
    if index <= len(gain) -1:
        avg_gain[int(index)] = ((avg_gain[int(index - 1)] * (period - 1)) + gain[int(index)]) / period
        average_gain_loss(gain, avg_gain, index + 1, period)
    return avg_gain

def rsi(price, period):
    change = price - price.shift()
    gain = change.where(change > 0, other = 0)
    loss = (-change).where(change < 0, other = 0)
    loss[0] = 'NaN'
    gain[0] = 'NaN'
    avg_gain = pd.rolling_mean(gain, period)
    avg_gain = average_gain_loss(gain, avg_gain, period + 1, period)
    avg_loss = pd.rolling_mean(loss, period)
    avg_loss = average_gain_loss(loss, avg_loss, period + 1, period)
    rs = avg_gain / avg_loss
    rsi = (100 - (100 / (1 + rs))).where(avg_loss != 0, other = 100)
    return rsi