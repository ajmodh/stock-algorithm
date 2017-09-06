#headers==========================
import pandas as pd
import pybacktest as pt
import macd
import ema
import rsi
import json
import matplotlib.pyplot as plt
# script = 'WOCKPHARMA.NS'
# script = 'SIEMENS.NS'
script = '^nsei'
# stg = "MACD"
# stg = "RSI"
stg = "_MACD_EMA_"
ohlc = pt.load_from_yahoo(script, adjust_close = True)
#=================================

#strategy=========================
def macd_sma_combination(price, macd_small, macd_long, signal, sma_period):
    value_macd = macd.macd(price, macd_small, macd_long)
    value_signal = pd.rolling_mean(value_macd, signal)
    value_sma = pd.rolling_mean(price, sma_period)
    buy = cover = (value_macd > value_signal) & (value_macd.shift() < value_signal.shift()) & (price > value_sma)
    sell = short = (value_macd < value_signal) & (value_macd.shift() > value_signal.shift()) & (price < value_sma)
    del cover
    del short
    return value_macd, value_signal, value_sma, buy, sell

def rsi_sma_combination(price, rsi_period, rsi_low_limit, rsi_up_limit, sma_period):
    value_rsi = rsi.rsi(price, rsi_period)
    value_sma=  pd.rolling_mean(price, sma_period)
    buy = cover = (value_rsi > rsi_low_limit) & (value_rsi.shift() < rsi_low_limit) & (price > value_sma)
    sell = short = (value_rsi < rsi_up_limit) & (value_rsi.shift() > rsi_up_limit) & (price < value_sma)
    del cover
    del short
    return value_rsi, value_sma, buy, sell

def macd_ema_anding(price, macd_small, macd_long, signal, ema_period):
    value_ema = ema.expon_moving_avg(price, ema_period)
    value_macd = macd.macd(price, macd_small, macd_long)
    value_signal = pd.rolling_mean(value_macd, signal)
    buy = cover = (value_macd > value_signal) & (value_macd.shift() < value_signal.shift()) & (price > value_ema) & (price.shift() < value_ema.shift())
    sell = short = (value_macd < value_signal) & (value_macd.shift() > value_signal.shift()) & (price < value_ema) & (price.shift() > value_ema.shift())
    del cover
    del short
    return value_ema, value_macd, value_signal, buy, sell
#=================================

