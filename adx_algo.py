def sum_of_list_values(from_list, start_index, to_index):
     return sum(from_list[start_index : to_index])

def true_range(from_list):
    tr_list,diffrence_high_low, diffrence_high_prev_close, diffrence_low_prev_close, max_value = [], 0, 0, 0, 0
    for index in range(len(from_list[0])):
        if index == 0:
            tr_list.append("none")
        else:
            diffrence_high_low = (from_list[0][index] - from_list[1][index])
            diffrence_high_prev_close = abs(from_list[0][index] - from_list[2][index-1])
            diffrence_low_prev_close = abs(from_list[1][index] - from_list[2][index-1])
            max_value = max(diffrence_high_low, diffrence_high_prev_close, diffrence_low_prev_close)
            tr_list.append(max_value)
    return tr_list

def plus_directional_moment(from_list):
    dm_list, diff_high_prv_high, diff_prev_low_low, max_value = [], 0, 0, 0
    for index in range(len(from_list[0])):
        if index == 0:
            dm_list.append("none")
        else:
            diff_high_prv_high = from_list[0][index] - from_list[0][index-1]
            diff_prev_low_low = from_list[1][index-1] - from_list[1][index]
            if diff_high_prv_high > diff_prev_low_low:
                 dm_list.append(max(diff_high_prv_high,0))
            else:
                dm_list.append(0)
    return  dm_list

def minus_directional_moment(from_list):
    dm_list,diff_high_prv_high, diff_prev_low_low, max_value  = [], 0, 0 ,0
    for index in range(len(from_list[0])):
        if index == 0:
            dm_list.append("none")
        else:
            diff_high_prv_high = from_list[0][index] - from_list[0][index-1]
            diff_prev_low_low = from_list[1][index-1] - from_list[1][index]
            if diff_prev_low_low > diff_high_prv_high:
                dm_list.append(max(diff_prev_low_low,0))
            else:
                dm_list.append(0)
    return dm_list

def tr_or_dm_of_interval(list_true_range, interval):
     tr_interval,tr_interval_value = [], 0
     tr_interval = ["none" for x in range(interval)]
     tr_interval.append(sum_of_list_values(list_true_range,1,interval+1))
     for index in range(len(list_true_range)):
         if index > interval:
            tr_interval_value = tr_interval[index -1] - (tr_interval[index -1] / interval) + list_true_range[index]
            tr_interval.append(tr_interval_value)
     return tr_interval

def di_or_dx(list_first,list_second,interval):
    di_or_dx_list = []
    di_or_dx_list = ["none" for x in range(interval)]
    for index in range(len(list_first)):
        if index > interval-1:
            di_or_dx_list.append (100 *(list_second[index] / list_first[index]))
    return di_or_dx_list

def difference_two_list(list_first,list_second):
    difference_result = []
    for index in range(len(list_first)):
        if list_first[index] == "none":
            difference_result.append("none")
        else:
            difference_result.append(abs(list_first[index]-list_second[index]))
    return difference_result

def sum_of_two_list(list_first,list_second):
    sum_result = []
    for index in range(len(list_first)):
        if list_first[index] == "none":
            sum_result.append("none")
        else:
            sum_result.append(list_first[index] + list_second[index])
    return sum_result

def adx_from_dx(dx_list, interval):
    adx_list = []
    adx_list = ["none" for x in range((interval*2 -1))]
    adx_list.append(sum_of_list_values(dx_list, interval,2*interval)/interval)
    for index in range(len(dx_list)):
        if index >= (interval*2):
            adx_list.append (((adx_list[index-1] * (interval -1)) + dx_list[index])/interval)
    return adx_list

tr,mdm, pdm,tri, pdmi, mdmi, pdi, mdi, didiff, disum, dx, adx = [],[], [], [], [], [],[], [],[], [], [], []

def adx_resul(values_input, days_period):
    tr = true_range(values_input)
    pdm = plus_directional_moment(values_input)
    mdm = minus_directional_moment(values_input)
    tri = tr_or_dm_of_interval(tr,days_period)
    mdmi = tr_or_dm_of_interval(mdm,days_period)
    pdmi = tr_or_dm_of_interval(pdm, days_period)
    pdi = di_or_dx(tri, pdmi, days_period)
    mdi = di_or_dx(tri, mdmi, days_period)
    didiff = difference_two_list(pdi,mdi)
    disum = sum_of_two_list(pdi,mdi)
    dx = di_or_dx(disum, didiff, days_period)
    adx = adx_from_dx(dx, days_period)
    return adx
