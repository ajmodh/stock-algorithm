import pandas as pd
import datetime as dt
import time
import pybacktest as pt

nifty_data = pt.load_from_yahoo('^nsei', start = '2014' , adjust_close= True)
nifty_all = pd.read_csv('/home/sigmasoft6/Desktop/indicator/nifty_all.csv')
data = dict(zip(nifty_all['Symbol'], nifty_all['Company']))

def datas(symbols):
    return {symbol: pt.load_from_yahoo(symbol+'.ns') for symbol in symbols}

def strategy_sma(script, period_small = 5, period_long = 10):
    ms = pd.rolling_mean(script.C, period_small)
    ml = pd.rolling_mean(script.C, period_long)
    buy = (ms > ml) & (ms.shift() < ml.shift())
    sell = (ms < ml) & (ms.shift() > ml.shift())
    return buy, sell

def stgy2(script, period_small = 50, period_long = 100):
    ms = pd.rolling_mean(script.C, period_small)
    ml = pd.rolling_mean(script.C, period_long)
    buy = (ms > ml) & (ms.shift() < ml.shift())
    sell = (ms < ml) & (ms.shift() > ml.shift())
    return buy, sell

def trades(stock_stgy,nifty):
    scripts = datas (stock_stgy)
    for scrip in scripts:
        stgy_script = stock_stgy[scrip]
        scripts[scrip]['Buy'], scripts[scrip]['Sell'] = stgy_script(scripts[scrip])
    for index in nifty.index:
        for script in scripts:
            if scripts[script]['Buy'][index]:
                yield ('Buy %s on %s' % (script, index))
            if scripts[script]['Sell'][index]:
                yield ('Sel %s on %s' % (script, index))
        else:
            yield index
            # time.sleep(1)

stock_stgy = {'HDFC':stgy2,'PNB':strategy_sma}
trade = trades(stock_stgy, nifty_data)
for value in trade:
    print value

    # '''
    #     # for sc_index in all_scrips[scrip].index:
    #     for stc, sc_index in zip(all_scrips[scrip]['Buy'], all_scrips[scrip].index):
    #         i = all_scrips[scrip].index.searchsorted(sc_index)
    #         if (index == sc_index) & stc:
    #             print index,scrip
    #             time.sleep(1)
    #     '''