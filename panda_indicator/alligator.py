import pybacktest
#===== start declaration header
import pandas as pd
import numpy as np
#===== end declaration header

#===== start import excel sheet
location_worksheet = '/home/sigmasoft6/Desktop/ALLIGATOR.xlsx'
df = pd.read_excel(location_worksheet,0)
#===== end import excel sheet

#===== start average of list
def average(li):
    return sum(li)/len(li)

def average_list(list,day):
    return [average(list[index-(day-1):index+1]) if index>=day-1 else None for index in range(len(list))]
#===== end average of list

#===== start
def alligarot_calculate(sma_lips_period, sma_teeth_period, sma_jaw_period, lips_moved, teeth_moved, jaw_moved):
    df['high_low_diff_avg'] = (df['High']+df['Low'])/2
    df['sma_for_lips'] = average_list(list(df['high_low_diff_avg']), sma_lips_period)
    df['sma_for_teeth'] = average_list(list(df['high_low_diff_avg']),sma_teeth_period)
    df['sma_for_jaw'] = average_list(list(df['high_low_diff_avg']),sma_jaw_period)
    df['lips_out'] = df['sma_for_lips'].shift(lips_moved-1)
    df['teeth_out'] = df['sma_for_teeth'].shift(teeth_moved-1)
    df['jaw_out'] = df['sma_for_jaw'].shift(jaw_moved-1)
    return df

print alligarot_calculate(5,8,13,3,5,8)

