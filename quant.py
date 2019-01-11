# Make sure to run dataclean.py first!

import scipy.stats as stats
import pylab
import numpy as np
import math

#%%

series = newemissionsdf.iloc[0].values
series = series[~np.isnan(series)]
somedata = stats.probplot(series,dist="norm",plot=pylab)

#%%

newseries = emissionslogdf.iloc[0].values
newseries = newseries[~np.isnan(newseries)]
somedata = stats.probplot(newseries,dist="norm",plot=pylab)

#%%

series = gdplogdf.iloc[0].values
series = series[~np.isnan(series)]
somedata = stats.probplot(series,dist="norm",plot=pylab)

#%%

series = gdpdf.iloc[0].values
series = series[~np.isnan(series)]
somedata = stats.probplot(series,dist="norm",plot=pylab)

#%%
for i in range(20):
    plt.plot(gdplogdf[[i]]/emissionsdf[[i]])