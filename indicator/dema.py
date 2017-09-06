def sma(close_list, days):
    sma_list, from_index = [], 0
    for index, value in enumerate(close_list):
        if index<days -1:
            sma_list.append("none")
        else:
            sma_list.append(sum(close_list[from_index:index+1])/days)
            from_index +=1
    return sma_list
def smoothning_const(days):
    var_smooth_const = 2.0/(days +1)
    return var_smooth_const, 1 -var_smooth_const

def ema_dema(close, sma_list , days_ema,days_dema):
    smooth_const_ema, smooth_const_1_ema = smoothning_const(days_ema)
    smooth_const_dema, smooth_const_1_dema = smoothning_const(days_dema)
    ema_list, dema_list = [], []
    for index, value in enumerate(close):
        if index < days_ema-1:
            ema_list.append("none")
            dema_list.append("none")
        else:
            if index == days_ema-1:
                ema_list.append(sma_list[index])
            else:
                ema_list.append((value *smooth_const_ema) + (ema_list[index -1] *smooth_const_1_ema))


            if index < (days_ema -1) + (days_dema -1):
                dema_list.append("none")
            else:
                if index == (days_ema -1) + (days_dema -1):
                    dema_list.append(ema_list[index])
                else:
                    dema_list.append((ema_list[index] *smooth_const_dema) + (dema_list[index -1] *smooth_const_1_dema))


    return ema_list, dema_list

def ema_dema_result(close, days_for_ema, days_for_dema):
    sma_list, ema_list, dema_list = [], [], []
    sma_list = sma(close, days_for_ema)
    ema_list, dema_list = ema_dema(close,sma_list,days_for_ema, days_for_dema)
    return ema_list ,dema_list

def tema_from_dema(dema_list, days_tema):
    smooth_const_tema, smooth_const_1_tema = smoothning_const(days_tema)
    tema_list, none_index = [], 0
    for index, values in enumerate(dema_list):
        if values == "none":
            tema_list.append("none")
            none_index = index +1
        else:
            if index < none_index + days_tema-1:
                tema_list.append("none")
            else:
                if index == none_index +(days_tema-1):
                    tema_list.append(dema_list[index])
                else:
                    tema_list.append((dema_list[index] *smooth_const_tema) + (tema_list[index -1] *smooth_const_1_tema))
    return tema_list