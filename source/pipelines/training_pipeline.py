import os 
import sys 
import pandas as pd 

# Add the path to the parent directory of the 'source' package folder
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(module_path)

from source.logger import logging
from source.exception import CustomException
from source.components.data_ingestion import DataIngestion
from source.components.data_transformation import DataTransformation
from source.components.model_trainer import ModelTrainer



if __name__ == "__main__":
    
    obj= DataIngestion()
    train_data_path, test_data_path= obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr,_= data_transformation.initaite_data_transformation(train_data_path,test_data_path)
    model_trainer =ModelTrainer()
    model_trainer.initiate_model_trainer( train_arr,test_arr)
