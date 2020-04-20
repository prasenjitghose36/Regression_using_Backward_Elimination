# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:18:23 2020

@author: Prasenjit
"""
#Multiple Linear Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(r"C:\Users\Prasenjit\Desktop\Python\Multiple_Linear_Regression\50_Startups.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#Encoding the categorical data
#Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

'''#labelencoding using columntransformer
lt = ColumnTransformer(transformers = [("Label",LabelEncoder(),[3])],remainder = "passthrough")
X = lt.fit_transform(X)'''


ot = ColumnTransformer(transformers = [("OneHot",OneHotEncoder(),[3])],remainder = "passthrough")
X = ot.fit_transform(X)

#Avoiding dummy Variable trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_opt, y, test_size = 0.2, random_state = 0)

'''# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)'''

#fitting the Mutiple linear regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

#Making a optimal model using backward elimination
import statsmodels.api as sm
X = np.append(arr = np.ones((50 , 1)).astype(int), values = X ,axis = 1)
X_opt = np.array(X[:,[0,1,2,3,4,5]], dtype=float) #stackoverflow solve
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #stackoverflow solve
regressor_OLS.summary()
X_opt = np.array(X[:,[0,1,3,4,5]], dtype=float) #stackoverflow solve
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #stackoverflow solve
regressor_OLS.summary()
X_opt = np.array(X[:,[0,3,4,5]], dtype=float) #stackoverflow solve
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #stackoverflow solve
regressor_OLS.summary()                                                                                 
X_opt = np.array(X[:,[0,3,5]], dtype=float) #stackoverflow solve
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #stackoverflow solve
regressor_OLS.summary()
X_opt = np.array(X[:,[0,3,5]], dtype=float) #stackoverflow solve
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #stackoverflow solve
regressor_OLS.summary() 



















