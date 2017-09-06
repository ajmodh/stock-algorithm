import pandas as pd
clo = [
8284,
8395.45,
8378.4,
8127.35,
8102.1,
8234.6,
8284.5,
8323,
8299.4,
8277.55,
8494.15,
8513.8,
8550.7,
8695.6,
8729.5,
8761.4,
8835.6,
8910.5,
8914.3,
8952.35,
8808.9,
8797.4,
8756.55,
8723.7,
8711.7,
8661.05,
8526.35,
8565.55,
8627.4
]
hi = [
8294.7,
8410.6,
8445.6,
8327.85,
8151.2,
8243.5,
8303.3,
8332.6,
8356.65,
8326.45,
8527.1,
8530.75,
8570.95,
8707.9,
8741.85,
8774.15,
8866.4,
8925.05,
8985.05,
8966.65,
8996.6,
8840.8,
8837.3,
8792.85,
8838.45,
8726.2,
8605.55,
8646.25,
8651.95
]

lo = [
8248.75,
8288.7,
8363.9,
8111.35,
8065.45,
8167.3,
8190.8,
8245.6,
8267.9,
8236.65,
8380.55,
8452.25,
8531.5,
8574.5,
8689.6,
8727,
8795.4,
8825.45,
8874.05,
8861.25,
8775.1,
8751.1,
8726.65,
8704.4,
8683.65,
8645.55,
8516.35,
8470.5,
8593.65
]

date = [
1-01-15,
2-01-15,
5-01-15,
6-01-15,
7-01-15,
8-01-15,
9-01-15,
12-01-15,
13-01-15,
14-01-15,
15-01-15,
16-01-15,
19-01-15,
20-01-15,
21-01-15,
22-01-15,
23-01-15,
27-01-15,
28-01-15,
29-01-15,
30-01-15,
2-02-15,
3-02-15,
4-02-15,
5-02-15,
6-02-15,
9-02-15,
10-02-15,
11-02-15
]
df = pd.DataFrame()
df['Date'] = date
df['High'] = hi
df['Low'] = lo
df['Close'] = clo

def psar(barsdata, iaf = 0.02, maxaf = 0.2):
    length = len(barsdata)
    dates = list(barsdata['Date'])
    high = list(barsdata['High'])
    low = list(barsdata['Low'])
    close = list(barsdata['Close'])
    psar = close[0:len(close)]
    psarbull = [None] * length
    psarbear = [None] * length
    bull = True
    af = iaf
    ep = low[0]
    hp = high[0]
    lp = low[0]
    for i in range(2,length):
        if bull:
            psar[i] = psar[i - 1] + af * (hp - psar[i - 1])
        else:
            psar[i] = psar[i - 1] + af * (lp - psar[i - 1])
        reverse = False
        if bull:
            if low[i] < psar[i]:
                bull = False
                reverse = True
                psar[i] = hp
                lp = low[i]
                af = iaf
        else:
            if high[i] > psar[i]:
                bull = True
                reverse = True
                psar[i] = lp
                hp = high[i]
                af = iaf
        if not reverse:
            if bull:
                if high[i] > hp:
                    hp = high[i]
                    af = min(af + iaf, maxaf)
                if low[i - 1] < psar[i]:
                    psar[i] = low[i - 1]
                if low[i - 2] < psar[i]:
                    psar[i] = low[i - 2]
            else:
                if low[i] < lp:
                    lp = low[i]
                    af = min(af + iaf, maxaf)
                if high[i - 1] > psar[i]:
                    psar[i] = high[i - 1]
                if high[i - 2] > psar[i]:
                    psar[i] = high[i - 2]
        if bull:
            psarbull[i] = psar[i]
        else:
            psarbear[i] = psar[i]
    return {"dates":dates, "high":high, "low":low, "close":close, "psar":psar, "psarbear":psarbear, "psarbull":psarbull}

print psar(df)
