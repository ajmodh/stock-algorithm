def maximum_of_list_period(from_list,index_from,index_to):
    return max(from_list[index_from:index_to])

def minimum_of_list_period(from_list,index_from,index_to):
    return min(from_list[index_from:index_to])

def highest_high_or_lower_low(lower_or_higher,from_list, days):
    index_from, index_to, to_list = 0, 0, []
    for index in range(len(from_list)):
        if index >= days:
            to_list.append(lower_or_higher(from_list ,index -days, index))
        else:
            to_list.append("none")
        index +=1
    return to_list

def period_since_higer_or_lower(high_low_list,higher_high_or_lower_low_list,days):
    to_list, index_of_value = [], 0
    for index, value in enumerate(higher_high_or_lower_low_list):
        if  value == "none":
            to_list.append("none")
        else:
            index_of_value = high_low_list[index-days:index].index(value)
            to_list.append((days) -index_of_value)
    return to_list

def aroon_up_down(period_higher_or_lower, days):
    aroon_up_down_list = []
    for values in period_higher_or_lower:
        if values == "none":
            aroon_up_down_list.append("none")
        else:
            aroon_up_down_list.append (int(((days -values + 0.0) /days) *100))
    return aroon_up_down_list

# get aroon of high low and its day
def aroon_all(high,low,days):
    higher_high, period_higher_high, aroon_up, lower_low, period_lower_low, aroon_down = [], [], [], [], [], []
    higher_high = highest_high_or_lower_low(maximum_of_list_period, high , days)
    period_higher_high = period_since_higer_or_lower(high, higher_high ,days)
    aroon_up = aroon_up_down(period_higher_high,days)

    lower_low = highest_high_or_lower_low(minimum_of_list_period, low, days)
    period_lower_low = period_since_higer_or_lower(low, lower_low,days)
    aroon_down = aroon_up_down(period_lower_low, days)
    return  higher_high, period_higher_high, aroon_up, lower_low, period_lower_low, aroon_down