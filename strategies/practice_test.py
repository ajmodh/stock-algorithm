import pandas as pd
import pybacktest as pbt
import ema
lst = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
lst2= [100,99,98,97,96,95,94,93,92,91]

nifty_data = pbt.load_from_yahoo('^nsei', start = '2015' , adjust_close= True)

def convert_to_prcentage(price, percentage):
    return (price * percentage) / 100.0

def optimization_values(entry_price = 100, stop_loss = 5, profit_target = 20, trail_trigger = 3, trail_stop = 6, type='%'):
    if type == '%':
        stop_loss = convert_to_prcentage(entry_price, stop_loss)
        profit_target = convert_to_prcentage(entry_price, profit_target)
        trail_trigger = convert_to_prcentage(entry_price, trail_trigger)
        trail_stop = convert_to_prcentage(entry_price, trail_stop)
    optimization_value ={
        'entry_price': entry_price,
        'stop_loss': stop_loss,
        'profit_target': profit_target,
        'trail_trigger': trail_trigger,
        'trail_stop': trail_stop
    }
    return optimization_value

def optimization_parameters(current_price= 101, optimizations_value = optimization_values(), position='long'):
    loss_stop = 0
    profit_stop = 0

    #for long position
    if position == 'long':
        if current_price < optimizations_value['entry_price'] + optimizations_value['trail_trigger']:
            loss_stop = optimizations_value['entry_price'] - optimizations_value['stop_loss']
        else:
            loss_stop = current_price-optimizations_value['trail_stop']
        profit_stop = optimizations_value['entry_price'] + optimizations_value['profit_target']

    #for short position
    else:
        if current_price > optimizations_value['entry_price'] - optimizations_value['trail_trigger']:
            loss_stop = optimizations_value['entry_price'] + optimizations_value['stop_loss']
        else:
            loss_stop = current_price + optimizations_value['trail_stop']
        profit_stop = optimizations_value['entry_price'] - optimizations_value['profit_target']
    return loss_stop, profit_stop

def sma_cross(ohlc, period_small = 5, period_long = 10):
    ms = pd.rolling_mean(ohlc.C, period_small)
    ml = pd.rolling_mean(ohlc.C, period_long)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    # bt = pbt.Backtest(locals(), "Sma Crossover")
    return locals()

def ema_cross(ohlc, period_small = 5, period_long = 10):
    ml = ema.expon_moving_avg(ohlc.C, period_small)
    ms = ema.expon_moving_avg(ohlc.C, period_long)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    # bt = pbt.Backtest(locals(), "Sma Crossover")
    return locals()

# for i in lst:
#     sl, pt = optimization_parameters(current_price= i, optimizations_value= optimization_values(entry_price=99))
#     print "stock_price=" ,i ,"stoploss=", sl ,"profit target=",pt
# print optimization_values(entry_price=99)
#==========================================


def optimization(stock_strategy_out, optimizations=0):
    data_buy = stock_strategy_out['buy']
    data_sell = stock_strategy_out['sell']
    data_price, entry_price, position = stock_strategy_out['ohlc'].C, 0, 'none'
    stop_loss , profit_target = 0, 0
    for date in data_buy.index.date:
        message = 'none'
        if data_buy[date] == True:
            entry_price = data_price[date]
            if position == 'short':
                message = "Square off and long"
            else:
                message = "Long"
            position = 'long'
            stop_loss = 0
            profit_target = 0
        elif data_sell[date] == True:
            entry_price = data_price[date]
            if position == 'long':
                message = "Square off and Sort"
            else:
                message = "Sort"
            position = 'short'
            stop_loss = 0
            profit_target = 0
        if position != 'none':
            if position == 'short':
                if data_price[date] > stop_loss and stop_loss != 0:
                    message = "stoploss hit!!! square off and take new position"
                    position = 'none'
                    stop_loss = 0
                    profit_target = 0
                elif data_price[date] < profit_target and profit_target != 0:
                    message = "Profit target achive!!! square off and take new position"
                    position = 'none'
                    stop_loss = 0
                    profit_target = 0
            elif position == 'long':
                if data_price[date] < stop_loss and stop_loss != 0:
                    message = "Stoploss hit!!! square off and take new position"
                    position = 'none'
                    stop_loss = 0
                    profit_target = 0
                elif data_price[date] > profit_target and profit_target != 0:
                    message = "Profit target achived!!! square off and take new position"
                    position = 'none'
                    stop_loss = 0
                    profit_target = 0
            if position != 'none':
                stop_loss, profit_target = optimization_parameters(current_price = data_price[date], optimizations_value = optimization_values(entry_price=entry_price, stop_loss= 50, profit_target= 100, trail_trigger= 10, trail_stop= 20, type= 'Rs'), position=position)
        yield [str(date), data_price[date], message, position, stop_loss, profit_target]

#==========================================

for i in optimization(sma_cross(nifty_data)):
    print i
#==========================================
# data_buy = sma_cross(nifty_data)['buy']
# data_sell = sma_cross(nifty_data)['sell']
# data_price, entry_price, position = nifty_data.C, 0, 'none'
# stop_loss , profit_target = 0, 0
# for date in data_buy.index.date:
#     # print date, 'buy=>', sma_cross(nifty_data)['buy'][date],'shell=>', sma_cross(nifty_data)['sell'][date]
#     print date, '===>', data_price[date]
#     if data_buy[date] == True:
#         entry_price = data_price[date]
#         if position == 'short':
#             print "Square off and long"
#         else:
#             print "Long"
#         position = 'long'
#         stop_loss = 0
#         profit_target = 0
#     elif data_sell[date] == True:
#         entry_price = data_price[date]
#         if position == 'long':
#             print "Square off and Sort"
#         else:
#             print "Sort"
#         position = 'short'
#         stop_loss = 0
#         profit_target = 0
#     if position != 'none':
#         if position == 'short':
#             if data_price[date] > stop_loss and stop_loss != 0:
#                 print "stoploss hit!!! square off and take new position"
#                 position = 'none'
#                 stop_loss = 0
#                 profit_target = 0
#             elif data_price[date] < profit_target and profit_target != 0:
#                 print "Profit target achive!!! square off and take new position"
#                 position = 'none'
#                 stop_loss = 0
#                 profit_target = 0
#         elif position == 'long':
#             if data_price[date] < stop_loss and stop_loss != 0:
#                 print "Stoploss hit!!! square off and take new position"
#                 position = 'none'
#                 stop_loss = 0
#                 profit_target = 0
#             elif data_price[date] > profit_target and profit_target != 0:
#                 print "Profit target achived!!! square off and take new position"
#                 position = 'none'
#                 stop_loss = 0
#                 profit_target = 0
#         if position != 'none':
#                 stop_loss, profit_target = optimaization_parameters(current_price = data_price[date], optimizations_value = optimization_values(entry_price=entry_price, stop_loss= 50, profit_target= 100, trail_trigger= 10, trail_stop= 20, type= 'Rs'), position=position)
#                 print 'stop loss ===>',stop_loss, 'Profit Target ===>', profit_target
# ==========================================