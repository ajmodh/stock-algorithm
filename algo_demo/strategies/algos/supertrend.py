import pandas as pd

def supertrand(data, period = 10, multiplier = 3):
    h_l = data.H - data.L
    h_cp = abs(data.H - data.C.shift())
    l_cp = abs(data.L -data.C.shift())
    data1 = pd.DataFrame()
    data1['h_l'] = h_l
    data1['h_cp'] = h_cp
    data1['l_cp'] = l_cp
    tr = data1[["h_l", "h_cp", "l_cp"]].max(axis=1)
    atr = pd.rolling_mean(tr, period)
    upperband_basic = ((data.H + data.L)/2) + (multiplier * atr)
    lowerband_basic = ((data.H + data.L) / 2) - (multiplier * atr)
    upperband = upperband_find(upperband_basic, data.C, period)
    lowerband = lowerband_find(lowerband_basic, data.C, period)
    supertrnd = supertrand_find(upperband, lowerband, data.C, period)
    return supertrnd

def upperband_find(upband_basic, close, period):
    uprband = upband_basic * 1
    for index in range(len(upband_basic)):
        if (index > period - 1):
            if(upband_basic[index] < uprband[index - 1] or close[index - 1] > uprband[index - 1]):
                uprband[index] = upband_basic[index]
            else:
                uprband[index] = uprband[index - 1]
    return uprband

def lowerband_find(lowerband_basis, close, period):
    lwrband = lowerband_basis * 1
    for index in range(len(lowerband_basis)):
        if(index > period - 1):
            if (lowerband_basis[index] > lwrband[index - 1] or close[index - 1] < lwrband[index - 1]):
                lwrband[index] = lowerband_basis[index]
            else:
                lwrband[index] = lwrband[index - 1]
    return lwrband

def supertrand_find(uperband, lowerband, close, period):
    supertrand = uperband * 1
    for index in range(len(uperband)):
        if (index > period - 1):
            if ((supertrand[index -1] == uperband[index -1]) & (close[index] < uperband[index])):
                supertrand[index] = uperband[index]
            else:
                if((supertrand[index -1] == uperband[index -1]) & (close[index] > uperband[index])):
                    supertrand[index] = lowerband[index]
                else:
                    if((supertrand[index -1] == lowerband[index -1]) & (close[index] > lowerband[index])):
                        supertrand[index] = lowerband[index]
                    else:
                        if((supertrand[index -1] == lowerband[index -1]) & (close[index] < lowerband[index])):
                            supertrand[index] = uperband[index]
                        else:
                            supertrand[index] = 0
    return supertrand
