import os 
import sys
import pandas as pd 
import numpy as np 
import pickle

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Add the path to the parent directory of the 'source' package folder
# module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(module_path)

from source.logger import logging 
from  source.exception import CustomException


def save_object( file_path, obj):
    try:
        dir_path= os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok= True)

        with open(file_path,'wb') as f:
            pickle.dump(obj, f)
    
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for i in range(len(models)):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]

            # Training the model 
            model.fit(X_train, y_train)

            # Predicting Testing Data
            y_test_pred = model.predict(X_test)

            # Get the R2score for the  test data 
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        logging.info("Exception Occured during model training")
        raise CustomException(e, sys)

    # Loading the pickle file    
def load_object(file_path):
    try:
        with open(file_path,'rb')as f:
            return pickle.load(f)
    
    except Exception as e:
        logging.info("Exception Occured in load_object function utils")
