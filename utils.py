import pandas as pd
import numpy as np
import pickle
import json
import config

class Titanic:
    def __init__(self):
        print("init functin")
    
    def load_data(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model=pickle.load(f)
        with open(config.JSON_FILE_PATH,'r') as f:
            self.project_data=json.load(f)
            self.gender=self.project_data['Gender']
            self.embarked=self.project_data['Columns'][-3:]
    
    def get_emabrked(self):
        self.load_data()
        
        emabrk = self.embarked
        emb=[]
        for i in emabrk:
            l1=i.split("_")
            emb.append(l1[1])
        print("locations :",emb)

        return emb
    def get_gender(self):
        gen=["Male","Female"]

        return gen

    def get_prediction(self,Pclass,Gender,Age,SibSp,Parch,Fare,Embarked):
        self.load_data()
        embarked="Embarked_"+Embarked
        index = self.project_data['Columns'].index(embarked)
        Gender_no=self.project_data['Gender'][Gender]
        columns = len(self.project_data['Columns'])
        test_array = np.zeros(columns)
        test_array[0] = Pclass
        test_array[1] = Gender_no
        test_array[2] = Age
        test_array[3] = SibSp 
        test_array[4] = Parch
        test_array[5] = np.sqrt(Fare)
        test_array[index] = 1
        print("Prajakta")
        predict_value = self.model.predict([test_array])[0]
        print("praaaaaj")
        return predict_value




if __name__ == "__main__":
    tt = Titanic()
    tt.get_emabrked()
    tt.get_gender()