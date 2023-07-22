# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:00:09 2021

@author: pujit
"""

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import os


dataset=pd.read_csv(os.path.join(os.path.dirname(__file__),"dataset.csv"),skipinitialspace=True)

Y=dataset['Disease']
del dataset['Disease']
X=dataset.iloc[:,:4]
xtrain,xtest,ytrain,ytest=train_test_split(X,Y,train_size=0.99)

OE=OneHotEncoder()
xtrain=OE.fit_transform(xtrain)

# file_name='django_fit_transform.sav'
# joblib.dump(OE,file_name)


xtest=OE.transform([['constipation','pain_during_bowel_movements','bloody_stool','irritation_in_anus']])

from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb = mnb.fit(xtrain, ytrain)
YP=mnb.predict(xtest)
print(YP)
# file_name='django_patient_registration.sav'
# joblib.dump(mnb,file_name)

# fit_transform=joblib.load('django_fit_transform.sav')

# test=fit_transform.transform([['muscle_wasting','shivering','extra_marital_contacts','spotting_ urination']])


# model=joblib.load('django_patient_registration.sav')
# YP=model.predict(test)

# print(YP)


