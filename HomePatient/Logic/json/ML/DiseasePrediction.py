import joblib
import os


class Symptoms:
    def __init__(self,s1,s2,s3,s4):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        # self.s5=s5
    
    def predictDisease(self):
        try:
            test_data=[[self.s1,self.s2,self.s3,self.s4]]
            print("test data is",test_data)
            transform_model=joblib.load(os.path.join(os.path.dirname(__file__),"django_fit_transform.sav"))
            test=transform_model.transform(test_data)
            print(test)
            model=joblib.load(os.path.join(os.path.dirname(__file__),"django_patient_registration.sav"))
            prediction=model.predict(test)
            if(prediction=='null' or prediction==None or prediction[0].upper()=='null'.upper() or prediction[0]==None):
                raise Exception()
        except:
            return "No Prediction"
        return prediction[0]
