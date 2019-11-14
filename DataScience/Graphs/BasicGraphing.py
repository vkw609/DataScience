# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:37:09 2019
HW2 code skeleton
@author: JRuan
"""

"""
Assignment done by Ashley Abernathy
Homework2
CS3753
Section 002
"""

import matplotlib.pyplot as plt
import numpy as np


#%% load data
import pandas as pd 
measles=pd.read_csv('Measles.csv',header=None).values
mumps=pd.read_csv('Mumps.csv',header=None).values
chickenPox=pd.read_csv('chickenPox.csv',header=None).values

plt.close('all')

#%% Q1. plot annual total measles cases in each year



x = []
y = []

for row in measles:
    x.append(int(row[0]))
    y.append(sum(map(int, row)))



plt.figure()
plt.title('Fig 1: NYC measles cases')
plt.xlabel('Years')
plt.ylabel('Total Cases')
plt.plot(x, y, '-x')

plt.show()

#%% Q2 plot annual total measels and mumps cases in log scale

x2 = []
y2 = []

for row in mumps:
    x2.append(int(row[0]))
    y2.append(sum(map(int, row)))
    
x1 = x + x2

years = list(dict.fromkeys(x1))


plt.figure()
plt.title('Fig 2: Measles and mumps cases in NYC')

plt.xlabel('Years')
plt.ylabel('Total Cases')

plt.plot(years,y,'-bx')
plt.plot(years, y2, '--go')

plt.yscale('log')

plt.legend(["Measles", "Mumps"], loc=1)
# complete this part

plt.show()

#%% Q3 plot average mumps cases for each month of the year

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
jan = []
feb = []
mar = []
apr = []
may = []
jun = []
jul = []
aug = []
sep = []
octo = []
nov = []
dec = []

for row in mumps:
    jan.append(row[1])
    feb.append(row[2])
    mar.append(row[3])
    apr.append(row[4])
    may.append(row[5])
    jun.append(row[6])
    jul.append(row[7])
    aug.append(row[8])
    sep.append(row[9])
    octo.append(row[10])
    nov.append(row[11])
    dec.append(row[12])

mon1 = sum(jan) / len(years)
mon2 = sum(feb) / len(years)
mon3 = sum(mar) / len(years)
mon4 = sum(apr) / len(years)
mon5 = sum(may) / len(years)
mon6 = sum(jun) /len(years)
mon7 = sum(jul)/len(years)
mon8 = sum(aug)/len(years)
mon9 = sum(sep)/len(years)
mon10 = sum(octo)/len(years)
mon11 = sum(nov)/len(years)
mon12 = sum(dec)/len(years)

monthlyTotals = [mon1, mon2, mon3, mon4, 
                 mon5, mon6, mon7, mon8, 
                 mon9, mon10, mon11, mon12]


plt.figure()
plt.title('Fig 3: Average monthly mumps cases')

index = np.arange(len(months))
plt.bar(index, monthlyTotals)
plt.xlabel('Months')
plt.ylabel('Monthly Totals')
plt.xticks(index, months)
plt.show()
# complete this part




#%% Q4 plot monthly mumps cases against measles cases 
mumpsCases = mumps[:, 1:].reshape(41*12)
measlesCases = measles[:, 1:].reshape(41*12)

plt.figure()
plt.title('Fig 4: Monthly mumps vs measles cases')

plt.scatter(mumpsCases,measlesCases)
plt.ylabel('Number of Measle Cases')
plt.xlabel('Number of Mumps Cases')


plt.show()


#%% Q5 plot monthly mumps cases against measles cases in log scale
plt.figure()
plt.title('Fig 5: Monthly mumps vs measles cases (log scale)')


plt.scatter(mumpsCases,measlesCases, s=10)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Number of Measle Cases')
plt.xlabel('Number of Mumps Cases')


plt.show()