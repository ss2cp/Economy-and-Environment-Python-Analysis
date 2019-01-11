### TIME SERIES ###
newemissionsdf # CO2/Capita
gdplogdf # GDP/Capita
cogdpdf = newemissionsdf/gdplogdf # CO2/GDP

emmeans = newemissionsdf.mean(axis=1) # Emissions means of all NATO nations
gdpmeans = gdplogdf.mean(axis=1) # GDP means of all NATO nations
cogdpmeans = cogdpdf.mean(axis=1) # Emissions/GDP of all NATO nations

usem = newemissionsdf['United States'] # US emissions/capita
usgdp = gdplogdf['United States'] # US GDP/capita
uscogdp = cogdpdf['United States'] # US emissions/GDP


# TS plot of US emissions/capita
usem.plot()


# TS plot of all NATO countries emissions/capita
emmeans.plot()


# TS plot of US gdp/capita
usgdp.plot()


# TS plot of all NATO countries gdp/capita
gdpmeans.plot()


# TS plot of US emissions/gdp
uscogdp.plot()


# TS plot of all NATO countries emissions/gdp
cogdpmeans.plot()

#%%

import statsmodels.api as sm

dta = usem
acf = sm.graphics.tsa.plot_acf(dta.values, lags=40)
acf.show()
pacf = sm.graphics.tsa.plot_pacf(dta.values, lags=40)
pacf.show()

#%%

# Let's try some models.
for i in range(0,4):
    for j in range(0,4):
        try:
            print("The model is ARMA with coefficients ",i,"and",j)
            somemodel = sm.tsa.ARMA(dta,(i,j)).fit()
            print("The AIC estimate is.")
            print(somemodel.aic)
        except:
            print("None")
            pass

#%%

# We can see that the best estimate is an ARMA(1,3) or ARMA(2,2).
# Try bic now.

for i in range(0,4):
    for j in range(0,4):
        try:
            print("The model is ARMA with coefficients ",i,"and",j)
            somemodel = sm.tsa.ARMA(dta,(i,j)).fit()
            print("The AIC estimate is.")
            print(somemodel.bic)
        except:
            print("None")
            pass

#%%

# ARMA(2,2) is the best model by a small margin. Now make the next few
# prediction values using this model.
model = sm.tsa.ARMA(dta, (2,2)).fit()
pred = model.predict("2016","2046",dynamic=False)
predict = pd.concat([dta,pred]).plot()




