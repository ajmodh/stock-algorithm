# for testing pandas and numpy
import sys
import pandas as pd
import numpy as np
from numpy  import random
s = pd.Series([1,3,5,None,4,2]) - pd.Series([1,2,3,1,1,2])
#print s
s = np.random.randn(6,5)
dates = pd.date_range('20130201', periods=6)
df = pd.DataFrame(s,index=dates, columns=list('ABCDE'))
#print df

#print s

#print pd.DataFrame([[1,2],[11,12]],index=['aa','bb'],columns= ['a','b'])
excl = pd.ExcelFile('/home/sigmasoft6/Downloads/MACDTutorial.xlsx')
#df =excl.parse(0)

#1=============================================================
names = ['Bob','Jessica']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
#df.to_csv('/home/sigmasoft6/Downloads/births1880.csv',index=False,header=True)
#Location = '/home/sigmasoft6/Desktop/Nifty.csv'
#2==============================================================
#random.seed(10)
random_names = [names[random.randint(0,len(names))]  for i in range(10)]
brthd = [random.randint(1,100) for i in range(10)]
dataa = zip(random_names,brthd)
df1 = pd.DataFrame(data=dataa,columns=['name','brth'])
#print df1
#print df1["brth"].unique()
name = df1.groupby('name')
df1 = name.sum()
#print df1
#3==============================================================
#rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')
#df.to_excel('/home/sigmasoft6/Desktop/lesson3.xlsx',index=False)

#location = '/home/sigmasoft6/Desktop/lesson3.xlsx'

#df = pd.read_excel(location, 0)
#print (df.head())
#df['Names'] = df.Names.apply(lambda x: x.upper())
#col1 = df['Names'][1]
# print (col1)
#df['Names'][10] = 'tandsdvdia'
#col1 = df['Names'][10]
# print (col1)

#4===============================================================

d = [x for x in range(10)]
df4 = pd.DataFrame(d)
df4.columns = ["num"]
df4['num1']=[x for x in range(10)]
df4['num1'] = df4['num1']+10
#print df4.loc[0:4]
#print df4.ix[:3,['num1','num']]
#print df4.tail()

#5================================================================

d = {'one':[1,1],'two': [2,2,]}
i = ['a', 'b']

df5 = pd.DataFrame(data=d, index=i)
#print df5.T

#6================================================================

d = {'one':[1,1,1,1,1],
     'two':[2,2,2,2,2],
     'letter': ['a','a','b','b','c']}
df6 = pd.DataFrame(data=d)
#print df6.groupby(['letter','one'],as_index= False).sum()

#7================================================================

states = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL']
data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = pd.date_range('1/1/2012', periods=10)
df7_1 = pd.DataFrame(data, index=idx, columns=['Revenue'])
df7_1['State'] = states
#df7_1['mean']= abs(df7_1['Revenue']- df7_1['Revenue'].mean())
grp = df7_1.groupby(['State',lambda x:x.month])
df7_1['neww'] = grp.transform(lambda x: x)
#print df7_1

#10=================================================================

#d = [1,2,3,4,5,6,7,8,9]
#df10 = pd.DataFrame(d, columns = ['Number'])
#df10.to_excel('/home/sigmasoft6/Desktop/lesson10.xlsx',sheet_name='testing',index=True)
#print "Done"
location = '/home/sigmasoft6/Desktop/lesson10.xlsx'
df10 = pd.read_excel(location,0)
print df10.head()