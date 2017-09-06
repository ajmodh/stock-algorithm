import pandas as pd
import pybacktest as pbt
import datetime  as dt

def chande_vidya(close,period):
    up = (close - close.shift()).where(close>close.shift(),other = 0)
    down = (abs(close - close.shift())).where(close<close.shift(),other = 0)
    up = pd.rolling_sum(up, period)
    down = pd.rolling_sum(down, period)
    volatility = abs(up - down) / (up + down)
    vidya = vidya_of_period(close, volatility, period)
    return vidya

def vidya_of_period(close, volatility, period):
    vdya = close.shift(period)
    vdya[int(period - 1)] = close[int(period - 1)]
    factr = alfa(period)
    for index in range(len(vdya)):
        if index >= period:
            vdya[index] = (factr * volatility[index] * close[index]) + ((1 - (factr * volatility[index])) * vdya[index - 1])
    return vdya

def alfa(days):
    return 2.0/ (days + 1)

# for excell export
# print chande_vidya(ohlc.C, 9)


# moving_small = chande_vidya(ohlc.C, 9)
# buy = cover = (ohlc.C > moving_small) & (ohlc.C.shift() < moving_small.shift())
# sell = short = (ohlc.C < moving_small) & (ohlc.C.shift() > moving_small.shift())

# bt = pbt.Backtest(locals(), 'chndvidyaaa')
# location = '/home/sigmasoft6/Desktop/traded_sheet_output/chndvdyaaa.xlsx'
# df = ohlc.copy()
# df['ms'] = moving_small
# df['buy'] = bt.signals['Buy']
# df['sell'] = bt.signals['Sell']
# df.to_excel(location,sheet_name='testing',index=True)