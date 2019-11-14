# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:42:10 2019

Ashley Abernathy
HW3
CS3753
Data Science
"""

#%% import necessary modules
import numpy as np
import pandas as pd
from matplotlib.pyplot import *

#%% load the data and setup some variables

data = pd.read_csv('diseases.csv',header=None).values
data = data.reshape([3, 41, 12]) #data[0] is for measles, etc.
diseases = ['Measles', 'Mumps', 'ChickenPox']
year = np.arange(1931, 1972)
month = np.arange(1, 13)

#%% Q1 calucate and show average number of cases per year, and 95% CI of the average


measles = data[0]
measlesYSum = data[0].sum(axis = 1) 
measlesYAvg = measlesYSum / 41

mumps = data[1]
mumpsYSum = data[1].sum(axis = 1)
mumpsYAvg = mumpsYSum / 41

chickenPox = data[2]
cpYSum = data[2].sum(axis = 1)
cpYAvg = cpYSum / 41


x = ([1,2,3])

mea = np.mean(measlesYSum,0)
mum = np.mean(mumpsYSum,0)
cp = np.mean(cpYSum,0)

tot = (mea, mum, cp)

SEM1 = np.std(measlesYSum,0)/np.sqrt(measlesYSum.shape[0])
SEM2 = np.std(mumpsYSum,0)/np.sqrt(mumpsYSum.shape[0])
SEM3 = np.std(cpYSum,0)/np.sqrt(cpYSum.shape[0])
SEM = (SEM1, SEM2, SEM3)

figure()
xlabel('NYC diseases')
ylabel('Number of cases')
ylim([0, 25000])
errorbar([1,2,3], tot, SEM, marker='d',linestyle='', capsize=5)
xticks = (['Measles','Mumps', 'ChickenPox'])
title('Fig 1 Average annual disease cases (95% CI)')
show()


#%% Q2 calucate and show fraction of cases occurred in each month

measlesYearly = data[0].sum(axis = 0)
mumpsYearly = data[1].sum(axis = 0)
cpYearly = data[2].sum(axis = 0)

totalMeasles = measles.sum()
totalMumps = mumps.sum()
totalCP = chickenPox.sum()

figure()

measlesFC = measlesYearly/totalMeasles
mumpFC = mumpsYearly / totalMumps
cpFC = cpYearly / totalCP

xlabel('Month')
ylim([0,.25])
ylabel('Fraction of cases')
title('Fig 2. Fraction of cases in each month')
plot(measlesFC)
plot(mumpFC)
plot(cpFC)
show()


#%% Q3.1 scatter plot avg monthly mumps cases vs chicken pox cases
figure()

mumps = data[1]
mumpsSum = data[1].sum(axis = 0)
mumpsAvg = mumpsSum / 12

chickenPox = data[2]
cpSum = data[2].sum(axis = 0)
cpAvg = cpSum / 12


xlabel('Avg monthly cases of ' + diseases[1])
ylabel('Avg monthly cases of ' + diseases[2])
title('Fig 3.1 monthly cases of mumps vs chickpen pox')
scatter(mumpsAvg, cpAvg)
show()


#%% Q3.2 scatter plot total annual mumps cases vs chicken pox cases
figure()

mumpsSumAn = data[1].sum(axis = 1)
cpSumAn = data[2].sum(axis = 1)

xlabel('Total annual cases of ' + diseases[1])
ylabel('Total annual cases of ' + diseases[2])
title('Fig 3.2 annual cases of mumps vs chicken pox')
scatter(mumpsSumAn, cpSumAn)
show()

#%% Q4.1, 4.2 calculate Pearson correlation coefficient


pcorr1 = np.corrcoef(mumpsAvg, cpAvg)
print('Pearson correlation between avg monthly mumps cases and monthly Chicken Pox cases is ', pcorr1)
pcorr2 = np.corrcoef(mumpsSumAn, cpSumAn)
print('Pearson correlation between annual mumps cases and annual Chicken Pox cases is ', pcorr2)

#%% Q4.3, 4.4 calculate the Spearman correlation coefficient 
mumpsRank = np.argsort(np.argsort(mumpsYSum))
cpRank = np.argsort(np.argsort(cpYSum))
spCorr1 = np.corrcoef(mumpsRank, cpRank)[0,1]

print('Spearman correlation between monthly mumps cases and monthly Chicken Pox cases is ', spCorr1)

mumpsRank2 = np.argsort(np.argsort(mumpsSumAn))
cpRank2 = np.argsort(np.argsort(cpSumAn))
spCorr2 = np.corrcoef(mumpsRank2, cpRank2)[0,1]
print('Spearman correlation between annual mumps cases and annual Chicken Pox cases is ', spCorr2)

#%% Q5 calculate and show correlation between number of numps cases in each month
figure()

C = mumps.T
M = np.corrcoef(C)


imshow(M)
title('Fig 4 Correlation between monthly mumps cases')
xlabel('Month')
ylabel('Month')
show()

#%% Q6 calculate and show average fraction of diseases occurring in different months
figure()


xlabel('Month')
ylabel('Fraction of cases')
title('Fig 5 Avg fraction of cases')
ylim([0,.175])
