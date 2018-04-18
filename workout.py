# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 08:21:39 2018

@author: Magnus
"""
import re
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = r'C:\Magnus Documents\Python\Personal'

# Read in the raw data into a dict
with open(path + '\\workoutLog.csv', 'r') as f:
    
    # Here all the lines are read -> not good if file is large.
    lines = f.readlines()
    
    for line, i in zip(lines, range(len(lines))):
        
        if re.match('DATA', line) is not None:
            
            dataStarts = i+1
            
    data = csv.reader(lines[dataStarts:], delimiter = ';')
    
    dict = {}
    
    i = 0
    for row in data:
        
        if i == 0:
            
            for item in row:
                
                dict[item] = []
                
        else:
            
            for item, j in zip(row, range(len(row))):
                
                dict[list(dict.keys())[j]].append(item)
                
        
        i += 1
        
    
    
# Process the data by 'total weight moved' for plotting
dict_total = {}

# First I did this exclusively for a Benchpress list, but this is a semi-
# general function that performs the same task for all dictionary keys that
# has the same structure.
def processPlot(dictionary):
    '''
    This function...
    '''
    emptyList = []
    
    for i in range(len(dictionary)):
        
        if dictionary[i] == '':
            emptyList.append(np.nan)
            
        else:
            calc = re.findall(r'\b\d+\b', dictionary[i])
            calcAdd = 0
            
            for i in range(0, len(calc), 2):
                calcAdd = calcAdd + int(calc[i])*int(calc[i+1])
            
            emptyList.append(calcAdd)
            
    return emptyList

# Process all the data into lists with total weight moved numbers
dict_total['Benchpress'] = processPlot(dict['Benchpress'])
dict_total['Curls'] = processPlot(dict['Curls'])
dict_total['Deadlift'] = processPlot(dict['Deadlift'])
dict_total['Dips'] = processPlot(dict['Dips'])
dict_total['Press'] = processPlot(dict['Press'])
dict_total['Pullups'] = processPlot(dict['Pullups'])
dict_total['Rows'] = processPlot(dict['Rows'])
dict_total['Squat'] = processPlot(dict['Squat'])


#plt.plot(Benchpress, 'p')


# Formatting the dates
Dates = []
dateFormat = "%Y-%m-%d"

for date in dict['Date']:
    Dates.append(datetime.strptime(date, dateFormat))

# Plotting with dates
for key in list(dict_total.keys()):
    plt.plot_date(Dates, dict_total[key])
    plt.legend(list(dict_total.keys()))
    plt.xticks(rotation = 90)
plt.grid()
plt.show()
















#Benchpress = []
#for i in range(len(dict['Benchpress'])):
#    
#    if dict['Benchpress'][i] == '':
#        Benchpress.append(np.nan)
#        
#    else:
#        calc = re.findall(r'\b\d+\b', dict['Benchpress'][i])
#        calcAdd = 0
#        
#        for i in range(0, len(calc), 2):
#            calcAdd = calcAdd + int(calc[i])*int(calc[i+1])
#        
#        Benchpress.append(calcAdd)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


