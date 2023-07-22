import pandas as pd
import os
import joblib


def searialize():
    data=pd.read_csv(os.path.join(os.path.dirname(__file__),'dataset.csv'),skipinitialspace=True)
    obj={"s1":list(set(data['Symptom_1'])),"s2":list(set(data['Symptom_2'])),"s3":list(set(data['Symptom_3'])),"s4":list(set(data['Symptom_4']))}
    joblib.dump(obj,os.path.join(os.path.dirname(__file__),'symptoms.joblib'))

def getSymptoms():
    obj=joblib.load(os.path.join(os.path.dirname(__file__),'symptoms.joblib'))
    return obj