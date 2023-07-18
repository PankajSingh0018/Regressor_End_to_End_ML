import os
import sys 
# from dataclasses import dataclass

# import numpy as np 
# import pandas as pd 

# from sklearn.compose import ColumnTransformer
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import Pipeline 
# from sklearn.preprocessing import OrdinalEncoder, StandardScaler

# # Add the path to the parent directory of the 'source' package folder
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(module_path)

# from exception import CustomException
# from logger import logging 
# import os 

# from utils import save_object

# @dataclass
# class DataTransformationConfig:
#     preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

# class DataTransformation:
#     def __init__(self):
#         self.data_tranformation_config =DataTransformationConfig()

#     def get_data_transformation_object(self):
#         try:
#             logging.info("Data Transformation Inititated")

#             # Creating categorical and numerical columns 
#             categorical_cols= ['cut','clarity','color']
#             numerical_cols= ['carat','depth','table','x','y','z']

#             # Defining the custom ranking for each ordinal variable 

#             # Define the custom ranking for each ordinal variable
#             cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
#             color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
#             clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

#             logging.info("Data Transformation Pipeline Initiated")

#             ## Numerical pipeline 
#             num_pipeline= Pipeline(
#                 steps=[
#                     ('imputer', SimpleImputer(strategy='median')),
#                     ('scaler', StandardScaler())

#                 ]
#             )

#             #categorical Pipeline 
#             cat_pipeline= Pipeline(
#                 steps = [
#                 ('imputer', SimpleImputer(strategy='most_frequent')),
#                 ('ordinalencoder', OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
#                 ('scaler', StandardScaler())

#                 ]

#             )

#             preprocessor = ColumnTransformer([
#                 ('num_pipeline',num_pipeline,numerical_cols),
#                 ('cat_pipeline',cat_pipeline,categorical_cols)
#             ])

#             return preprocessor

#             logging,info("Data Transformation Completed")

        
#         except Exception as e:
#             logging.info("Error in Data Transformation")
#             raise CustomException(e,sys)


#     def initiate_data_transformation(self, train_path, test_path):
#         try:
#             #Reading the train & test dataset\
#             train_df = pd.read_csv(train_path)
#             test_df = pd.read_csv(test_path)

#             logging.info("Re ad Train and Test Dataset completed ")
#             logging.info(f'Training DataFrame Head :\n{train_df.head().to_string()}')
#             logging.info(f'Test DataFrame Head: \n{test_df.head().to_string()}')
            
#             logging.info("Obtaining the Preprocessing Object")
#             preprocessing_obj= self.get_data_transformation_object()

#             # creating the input and output features 
#             target_column ='price'
#             drop_columns= [target_column, 'id']

#             input_feature_train_df= train_df.drop(columns= drop_columns, axis= 1)
#             target_feature_train_df= train_df[target_column]

#             input_feature_test_df= test_df.drop(columns= drop_columns, axis=1)
#             target_feature_test_df = test_df[target_column]

#             # tranforming using preprocessor object
#             input_feature_train_arr= preprocessing_obj.fit_transform(input_feature_train_df)
#             input_feature_test_arr= preprocessing_obj.transform(input_feature_test_df)

#             logging.info("Applying preprocessing Object on training and testing datasets")

#             # concatenating the datasets and converting it into a numpy array so as to able to load it quickly it is used when the dataset is very very huge
#             train_arr = np.c_[input_feature_train_arr, np.arr(target_feature_train_df)]
#             test_arr = np.c_[input_feature_test_arr, np.arr(target_feature_test_df)]

#             save_object(
#                 file_path= self.data_tranformation_config.preprocessing_obj_file_path, 
#                 obj = preprocessing_obj

#             )

#             logging.info("Preprocessor Pickle file saved ")

#             return (
#                 train_arr, 
#                 test_arr,
#                 self.data_tranformation_config.preprocessing_obj_file_path

#             )

#         except Exception as e:
#             logging.info( " Exception occured in the Data Transformation initiate step")
#             raise CustomException(e,sys)



import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from exception import CustomException
from logger import logging
import os
from utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info('Pipeline Initiated')

            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

            )

            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]

            )

            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            return preprocessor

            logging.info('Pipeline Completed')

        except Exception as e:
            logging.info("Error in Data Trnasformation")
            raise CustomException(e,sys)
        
    def initaite_data_transformation(self,train_path,test_path):
        try:
            # Reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object()

            target_column_name = 'price'
            drop_columns = [target_column_name,'id']

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            ## Trnasformating using preprocessor obj
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets.")
            

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)