import pandas as pd
import matplotlib.pyplot as plt
from pyautogui import prompt, confirm
def math(df,y):
    print(''' Please select a number from list:
    1) Standard Deviation \t 2) Mean
    3) Variance \t 4) Median
    5) Mode \t 6) Range
    7) Quartile1 \t 8) Quartile3
    \t 9) all  
    
    SELECTING A NUMBER .....
    ''')
    me = prompt(text = ''' Please select a number from list:
    1) Standard Deviation     2) Mean
    3) Variance    4) Median
    5) Mode       6) Range
    7) Quartile1    8) Quartile3
    9) all
    ''', title = 'Select a number from list')
    if me == '1':
        # standard deviation
        std = df[y].std()
        confirm(text = 'Standard deviation of the data is ' + str(std) , title = ' Standard Deviation')
    if me == '2':
        # mean
        mean = df[y].mean()
        confirm(text = 'Mean of the data is ' + str(mean) , title = ' Mean')
    if me == '3':
        # variance
        var = df[y].var()
        confirm(text = 'Variance of the data is ' + str(var) , title = ' Variance')
    if me == '4':
        # median
        median = df[y].median()
        confirm(text = 'Median of the data is ' + str(median) , title = ' Median ')
    if me == '5':
        # mode
        mode = df[y].mode()
        confirm(text = 'Mode of the data is ' + str(mode) , title = ' Mode ')
    if me == '6':
        # range
        range = df[y].max() - df[y].min()
        confirm(text = 'Range of the data is ' + str(range) , title = ' Range ')
    if me == '7':
        # quartile1
        q1 = df[y].quantile(0.25)
        confirm(text = 'Quartile1 of the data is ' + str(q1) , title = ' Quartile 1 ')
    if me == '8':
        # quartile3
        q3 = df[y].quantile(0.75)
        confirm(text = 'Quartile3 of the data is ' + str(q3) , title = ' Quartile 2 ')
    if me == '9':
        # all
        std = df[y].std()
        mean = df[y].mean()
        var = df[y].var()
        median = df[y].median()
        mode = df[y].mode()
        range = df[y].max() - df[y].min()
        q1 = df[y].quantile(0.25)
        q3 = df[y].quantile(0.75)
        confirm(text = 'Standard deviation of the data is ' + str(std) + '\n' + 'Mean of the data is ' + str(mean) + '\n' + 'Variance of the data is ' + str(var) + '\n' + 'Median of the data is as follows \n ' + str(median) + '\n' + 'Mode of the data is ' + str(mode) + '\n' + 'Range of the data is ' + str(range) + '\n' + 'Quartile1 of the data is ' + str(q1) + '\n' + 'Quartile3 of the data is ' + str(q3) , title = ' All ')



