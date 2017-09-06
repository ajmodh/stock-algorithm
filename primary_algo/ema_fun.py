def average(close):
    return sum(close)/len(close)

def smoothning_factor (days):
    return 2.0 / (days + 1)

def ema_fun(close, days):
    ema = [ average(close[index-(days-1):index+1]) if index >= days-1 else None for index in range(len(close))]
    return ema_value(close, ema, days, days)

# Ema of close price and ema of period
def ema_value(close, ema, period, index):
    sf = smoothning_factor(period)
    if index < len(ema):
        ema[index] = (sf * (close[index] - ema[index - 1])) + ema[index - 1]
        ema_value(close, ema, period, index + 1)
    return ema