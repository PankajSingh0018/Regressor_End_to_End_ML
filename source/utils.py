import os 
import sys
import pandas as pd 
import numpy as np 
import pickle
import os

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Add the path to the parent directory of the 'source' package folder
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(module_path)

from logger import logging 
from  exception import CustomException


def save_object( file_path, obj):
    try:
        dir_path= os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok= True)

        with open(file_path,'wb') as f:
            pickle.dump(obj, f)
    
    except Exception as e:
        raise CustomException(e, sys)