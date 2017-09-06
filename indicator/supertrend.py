def true_range(high_list,low_list):
    true_range_list = []
    for index in range(len(high_list)):
        true_range_list.append(high_list[index] - low_list[index])
    return true_range_list

def average_tr(true_range_list, days):
    average_tr_list, addition = [], 0
    average_tr_list = [0 for x in range(days-1)]
    for index in range(len(true_range_list)):
            if index >= days-1:
                addition = sum(true_range_list[index -(days-1):index+1])
                average_tr_list.append(addition/days)
    return average_tr_list

def upper_lower_band_basic_values(high, low, mpf, atr):
    return (((high+low)/2) + (mpf * atr)), (((high+low)/2) - (mpf * atr))

def upper_lower_band_basic(high_list, low_list, multiplie, atr_list):
    upperband_list,lowerband_list, upperband_value, lowerband_value = [], [], 0, 0
    for index, values in enumerate(atr_list):
        if values == 0:
            upperband_list.append(0)
            lowerband_list.append(0)
        else:
            upperband_value, lowerband_value = upper_lower_band_basic_values(high_list[index],low_list[index], multiplie, atr_list[index])
            upperband_list.append(upperband_value)
            lowerband_list.append(lowerband_value)
    return upperband_list, lowerband_list

def upper_band_values(upper_band_basic, upperband, close):
    if(upper_band_basic < upperband or close > upperband):
        return upper_band_basic
    else:
        return upperband

def lower_band_values(lower_band_basic, lowerband, close):
    if (lower_band_basic > lowerband or close < lowerband):
        return lower_band_basic
    else:
        return lowerband

def upper_lower_band(upper_band_basic_list,lower_band_basic_list, close):
    upper_band_list, lower_band_list = [], []
    for index, values in enumerate(upper_band_basic_list):
        if values == 0:
            upper_band_list.append(0)
            lower_band_list.append(0)
        else:
            upper_band_list.append(upper_band_values(upper_band_basic_list[index], upper_band_list[index-1], close[index-1]))
            lower_band_list.append(lower_band_values(lower_band_basic_list[index], lower_band_list[index-1], close[index-1]))
    return upper_band_list, lower_band_list

def supertrend_values(prev_super, prev_up, cur_up, prev_low, cur_low, cur_close):
    if((prev_super == prev_up) & (cur_close <= cur_up)):
        return cur_up
    else:
        if((prev_super == prev_up) & (cur_close >= cur_up)):
            return cur_low
        else:
            if((prev_super == prev_low) & (cur_close >= cur_low)):
                return cur_low
            else:
                if((prev_super == prev_low) & (cur_close <= cur_low)):
                    return cur_up
                else:
                    return 0

def supertrend_result(close_list, upperband_list, lowerband_list):
    supertrend_list = []
    for index, values in enumerate(upperband_list):
        if values == 0:
            supertrend_list.append(0)
        else:
            supertrend_list.append(supertrend_values(supertrend_list[index -1],upperband_list[index -1],upperband_list[index],lowerband_list[index -1],lowerband_list[index],close_list[index]))
    return supertrend_list

def super_trend(high, low, close, days, muliplier):
    tr_list = true_range(high, low)
    atr_list = average_tr(tr_list, days)
    upperband_basic, lowerband_basic = upper_lower_band_basic(high, low, muliplier, atr_list)
    upperband, lowerband = upper_lower_band(upperband_basic,lowerband_basic, close)
    super_trend = supertrend_result(close, upperband, lowerband)
    return tr_list, atr_list, upperband_basic, lowerband_basic, upperband, lowerband, super_trend
