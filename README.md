
Look at other libraries for formatting examples

data #a pandas dataframe
#Data is treated as categorical or nlp
#Categorical is converted to n-1 one-hot
#nlp is converted to ngrams unless otherwise specified

#uses statsmodels bc we get error

propensity_model = LinearRegression(predict='treatment', hyperparams=, interaction=None)
#see https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression?
#to see what goes in it
#But we do want to use statsmodels 

#interaction could take a list of categories

Does the init or the fit contain each variable

propensity_model.fit(data, treatment='t', outcome='out', nlp='textcol', interaction=None) 
#speicfy treatment and outcome columns, default to first and last. Can also specify with indices. Specify columns

