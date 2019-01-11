# This file will clean up the data by interpolating missing values.
# Make sure to change your working directory to your project folder!

#%%

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from pandas import DataFrame
from datetime import datetime
from sklearn import linear_model

#%%

# Import the raw data files.

gdp = pd.read_csv('(RAW) GDP%2F Capita.csv')
emissions = pd.read_csv('(RAW) Emissions%2F Capita.csv')

#%%

# The countries then would be.
countries = gdp.iloc[:,0].values

# The time values would be.
today = datetime.today().year
time = range(today-56,today,1)
timelist = []
for i in time:
    something = datetime.strptime(str(i),"%Y")
    timelist.append(something)


# Turn them into dataframes.
gdpdf = DataFrame(gdp.iloc[:,1:57]).T
gdpdf.index = timelist
gdpdf.columns = countries
emissionsdf = DataFrame(emissions.iloc[:,1:57]).T
emissionsdf.index = timelist
emissionsdf.columns = countries

#%%

# The data is not linear. Take the log-log.

def mylog(input):
    if math.isnan(input):
        return(input)
    else:
        return(math.log(input))

gdplogdf = gdpdf.applymap(mylog)
emissionslogdf = emissionsdf.applymap(mylog)

#%%

# Perform the regression.
for country in countries[countries!="Czech Republic"]:
    somedf=pd.concat([gdplogdf[[country]],emissionslogdf[[country]]],axis=1)
    otherdf=somedf.dropna()
    regression = linear_model.LinearRegression()
    regression.fit(otherdf[[0]].values,otherdf[[1]].values)
    missing=somedf[np.isnan(somedf[[1]].values)]
    missing[[1]]=regression.intercept_+regression.coef_*missing[[0]].values
    emissionslogdf[[country]]=emissionslogdf[[country]].fillna(missing[[1]])

#%%

newemissionsdf = emissionslogdf.applymap(math.exp)

#%%

    
    
    
    
    
    
    