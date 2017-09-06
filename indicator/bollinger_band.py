import statistics
def standard_deviation(list):
    return statistics.pstdev(list)

def average(list, period):
    return (sum(list))/period

def upper_lower_bandwidth(sma, stand_deviation):
    upper, lower, bandwidth = 0, 0, 0
    upper = sma + (2* stand_deviation)
    lower = sma - (2* stand_deviation)
    bandwidth = upper - lower
    return upper, lower, bandwidth

def bollinger_band(close_list, days):

    sma_list, standard_deviation_list, upperband, lowerband, bandwidth = [], [], [], [], []
    standard_deviation_list = ["none" for index in range(days-1)]
    sma_list , upperband , lowerband, bandwidth = ["none" for index in range(days-1)], ["none" for index in range(days-1)], ["none" for index in range(days-1)], ["none" for index in range(days-1)]

    for index, value in enumerate(close_list):
        if index >= days-1:
            sma_list.append(average(close_list[index-(days-1):index+1],days))
            standard_deviation_list.append(standard_deviation(close_list[index-(days-1):index+1]))
            upper_value, lower_value, bandwidth_value = upper_lower_bandwidth(sma_list[index],standard_deviation_list[index])
            upperband.append(upper_value)
            lowerband.append(lower_value)
            bandwidth.append(bandwidth_value)
    return sma_list, standard_deviation_list,upperband, lowerband, bandwidth




