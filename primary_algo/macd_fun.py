def smoothing_const(days):
     return (2.0 / (days + 1))

def average_list(list):
    return sum(list)/len(list)

# EMA Value for MACD
def expon_moving_avg(list, days):
    ema_index = [index if index > days - 1 else None if index != (days - 1) else average_list(list[index - (days-1) : index+1]) for index in range(days)]
    def expon_mov_value(index):
        if index <= len(list) -1:
            ema_value =  smoothing_const(days) * (list[index] - ema_index[index -1]) + ema_index[index -1]
            ema_index.append(ema_value)
            expon_mov_value(index + 1)
    expon_mov_value(days)
    return ema_index

def diffrence_list(first_list, second_list):
        return  [ema_small_value - ema_long_value if ema_long_value != None else None for ema_small_value, ema_long_value in zip(first_list, second_list) ]

# for Printing MACD of Stock Prices for Example use close value for that
#=======================================================================
# ema_small = expon_moving_avg(close, 12)
# ema_long = expon_moving_avg(close, 26)
#print diffrence_list(ema_small,ema_long)
# print [1 if index > 11 else None if index != 11 else average_list(ema_small[index - 11 : index + 1]) for index in range(len(ema_small))]