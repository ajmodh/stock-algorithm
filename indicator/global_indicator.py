def list_print(list):
    for index, value in enumerate(list):
        print(value)

def sma_average(list):
    average = (sum(list))/len(list)
    return average, sum(list)

def ema_smoothning_const(period):
    return 2/(period+1)

def ema(current_close, previous_ema, period):
    smooth_const = ema_smoothning_const(period)
    return ((smooth_const*(current_close - previous_ema)) + previous_ema)

def rate_of_change(current_value,previous_value):
    return ((current_value - previous_value) /previous_value) *100

def true_range(high,low):
    true_range_list = []
    for index in range(len(high)):
        true_range_list.append(high[index] - low[index])
    return true_range_list




