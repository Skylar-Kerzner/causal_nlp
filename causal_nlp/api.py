import numpy as np
import pandas as pd
import sklearn

#Takes pandas dataframes.
#Write UX in readme


#make a baseclass as an interface just to require fit and predict (more for contributors to easily see whats required to add a new ML model)
#standardize hyperparameter fitting across models? Calibration too. see scikit learn's solutions for that.


#classes can have a standard interface with model attribute that is the library model
#Then can get attributes of that library model as expected
class LinearRegression:
    def __init__(self, fit_intercept=True, copy_X=True, n_jobs=None, positive=False):
        self.model = sklearn.linear_model.LinearRegression(fit_intercept=fit_intercept, copy_X=copy_X, n_jobs=n_jobs, positive=positive)

    #change these defaults to None. no default for predict. Can default treatment and outcome cols to 0 and -1
    def fit(self, data, 
    predict='outcome', treatment='col1', outcome='coln', nlp_cols=['textcol',], nlp_methods= , interactions='all', pick_interations='L1', regularization='elastic_net'):
        validate_inputs(data, predict, treatment, outcome, nlp_cols, nlp_methods, interactions, pick_interations, regularization)

    #output some text details of the input before and after the transformations
    #What columns are being applied as treatment, covariate and prediction
    #outcome model predict... or treatment (propensity) model predicting treatment from the covariates

        # do the transformations
        self.model.fit() #give it the X and y based on give parameters

    #use self.model.predict() for any model
    #CATE will call this
    def predict(self, ):
        pass
    

    
def validate_inputs(data, predict, treatment, outcome, nlp_cols, nlp_methods, interactions, pick_interations, regularization):

    if not isinstance(data, pd.DataFrame):
        raise TypeError(f'Data object is of type {type(data)} but should be of type: pandas.DataFrame')

    if not isinstance(predict, str):
        raise TypeError(f'Predict option {predict} of type {type(predict)} should be of type str')
    if predict not in ['outcome', 'treatment']:
        raise ValueError(f'Predict option {predict} must be "outcome" or "treatment"')

    if not (isinstance(treatment, str) or  isinstance(treatment, int)  ):
        raise TypeError(f'Treatment column {treatment} must be of type: str or int')
    if isinstance(treatment, str):
        if treatment not in data.columns:
            raise ValueError(f'Treatment column {treatment} not found in data')
    if isinstance(treatment, int):



#ATE wrapper on CATE with no conditions, just calls CATE()