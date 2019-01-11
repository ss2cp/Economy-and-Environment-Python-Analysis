#%%

import pandas as pd
import numpy as np
from scipy.stats import t

newemissionsdf # CO2/Capita
gdplogdf # GDP/Capita

newemissionsdf.__delitem__('Czech Republic') # remove Czech Republic
gdplogdf.__delitem__('Czech Republic') # remove Czech Republic



# Emission/Capita for NATO countries

newemissionsdf['Sum']=newemissionsdf.sum(axis=1,skipna=True) # get the sum of countries for each year
newemissionsdf['Avg']=newemissionsdf.Sum/28 # divide the sum by 28 since there are 28 countries to get the average value for each year
xbar = np.mean(newemissionsdf.Avg) # mean emission/capita of the mean values for each year
s = np.std(newemissionsdf.Avg,ddof=1) # standard deviation emission/capita of the mean values for each year
n = len(newemissionsdf.Avg) # number of years
tstar = t.ppf(.975, n-1) # tstar
lcl = xbar - tstar*s/np.sqrt(n) #lower bound
ucl = xbar + tstar*s/np.sqrt(n) #upper bound
print("95% confidence interval for Emissions/Capita for NATO: ")
print([lcl,ucl])

# GDP/Capita for NATO countries

gdplogdf['Sum']=gdplogdf.sum(axis=1,skipna=True) # get the sum of countries for each year
gdplogdf['Avg']=gdplogdf.Sum/28 # divide the sum by 28 since there are 28 countries to get the average value for each year
newxbar = np.mean(gdplogdf.Avg) # mean GDP/capita of the mean values for each year
s = np.std(gdplogdf.Avg,ddof=1) # standard deviation GDP/capita of the mean values for each year
n = len(gdplogdf.Avg) # number of years
tstar = t.ppf(.975, n-1) # tstar
newlcl = xbar - tstar*s/np.sqrt(n) #lower bound
newucl = xbar + tstar*s/np.sqrt(n) #upper bound
print("95% confidence interval for GDP/Capita for NATO: ")
print([newlcl,newucl])

# Efficiency of productivity for NATO countries
[lcl/newlcl, ucl/newucl]

# Emission/Capita for the United States

xbar = np.mean(newemissionsdf['United States']) # mean emission/capita of US
s = np.std(newemissionsdf['United States'],ddof=1) # standard deviation emission/capita of US
n = len(newemissionsdf['United States']) # number of years
tstar = t.ppf(.975, n-1) # tstar
lcl = xbar - tstar*s/np.sqrt(n) #lower bound
ucl = xbar + tstar*s/np.sqrt(n) #upper bound
print("95% confidence interval for Emissions/Capita for the United States: ")
print([lcl,ucl])

# GDP/Capita for the United States

newxbar = np.mean(gdplogdf['United States']) # mean GDP/capita of US
s = np.std(gdplogdf['United States'],ddof=1) # standard deviation GDP/capita of US
n = len(gdplogdf['United States']) # number of years
tstar = t.ppf(.975, n-1) # tstar
newlcl = xbar - tstar*s/np.sqrt(n) #lower bound
newucl = xbar + tstar*s/np.sqrt(n) #upper bound
print("95% confidence interval for GDP/Capita for the United States: ")
print([newlcl,newucl])

# Efficiency of productivity for the United States
[lcl/newlcl, ucl/newucl]
