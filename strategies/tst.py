# import pandas as pd
# import datetime as dt
#
# location = '/home/sigmasoft6/Desktop/indicator/nifty.xlsx'
# ohlc1 = pd.read_excel(location, 0)
# ohlc1.index = ohlc1['Date']
# del ohlc1['Date']
# start = ohlc1.index.searchsorted(dt.date(2015,01,01))
# # end = ohlc1.index.searchsorted(dt.date(2015,12,30))
# ohlc = ohlc1[start:]
#
# def return_day(series, period):
#          return (series - series.shift(period  - 1))/ series.shift() *100
#
# # def get_data(yr, mo):
# #     for days in range(1,32):
# #         yr = str(yr)
# #         mo = str(mo)
# #         day = str(days)
# #         dat_def = yr+'-'+mo+'-'+day
# #         # print dat_def
# #         # if ohlc[ohlc.index == '2015-01-01']:
# #         return dat_def
#
# lis = [2015]
#
#
# # ohlc['return'] = return_day(ohlc.C, 5)
# # for year in range(1,len(lis)+1):
# for month in range(1,13):
#     # mo = month
#     # yr = 2015
#     mo = month
#     if mo < 12:
#        print ohlc[ohlc.index.searchsorted(dt.date(2015,month+1,1))-1:ohlc.index.searchsorted(dt.date(2015,month+1,1))]
#     # print ohlc_nw#ohlc[ohlc_nw.index == ohlc_nw.index[-1]] #== ohlc[ohlc.index == dat]
#
# # print get_data(2015, 11)
# # mo = "02"
# # yr = "2015"
# # dat = yr+'-'+mo+'-04'
# # ohlc = ohlc['2015-01-02':'2015-01-30']
# # print ohlc[ohlc.index == ohlc.index[-1]]
# # print ohlc[ohlc.index.searchsorted(dt.date(2015,2,1))-1:ohlc.index.searchsorted(dt.date(2015,2,1))]


ls = [(1,'SMA','ACC',12),(2,'SMA','BCC',6),(3,'SMA','ACC',15),(4,'EMA','BCC',15)]
ms = [(1,'SMA','ACC',12),(2,'SMA','BCC',6),(3,'SMA','ACC',15),(4,'EMA','BCC',15)]
result= {}
rs = {}
for row in ms:
    if row[1] in rs:
        if row[2] in rs[row[1]]:
            rs[row[1]][row[2]].append((row[3],row[0]))
        else:
            rs[row[1]][row[2]] = [(row[3],row[0])]
    else:
         rs[row[1]] = {row[2]:[(row[3],row[0])]}


for row in ls:
	if row[1] in result:
		if row[2] in result[row[1]]:
			result[row[1]][row[2]].append(row[0:])
		else:
			result[row[1]][row[2]] = [row[0:]]
	else:
		result[row[1]] = {row[2]: [row[0:]]}



print result
print rs