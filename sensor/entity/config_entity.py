import os
from datetime import datetime
import sys

FILE_NAME="sensor.csv"
TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"
TRANSFORMER_OBJECT_FILE_NAME="transform.pkl"
TARGET_ENCODER_OBJECT_FILE_NAME="traget_encoder.pkl"
MODEL_FILE_NAME="model.pkl"

class TrainingPipelineConfig:

    def __init__(self):
        self.artifact_dir=os.path.join(os.getcwd(),"artifacct",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")


class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        self.database_name="airpressuresys"
        self.collection_name="sensor"
        self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
        self.feature_store_file_path=os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
        self.train_file_path= os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
        self.test_file_path=os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
        self.test_size = 0.2


    def to_dict(self,)->dict:

        try:
            return self.__dict__
        except Exception as e:

            raise SensorException(e,sys)



class DataValidationConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        self.data_validation_dir=os.path.join(training_pipeline_config.artifact_dir,"data_validation")
        self.report_file_path=os.path.join(self.data_validation_dir,"report.yaml")
        self.missing_threshold=0.30
        self.base_file_path=os.path.join("/config/workspace/aps_failure_training_set1.csv")
        #to record drift , anomoly 





class DataTransformationConfig:
    
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir =os.path.join(training_pipeline_config.artifact_dir,"data_transformation")
        self.transform_object_path=os.path.join(self.data_transformation_dir,"transformer",TRANSFORMER_OBJECT_FILE_NAME)
        self.transformed_train_path=os.path.join(self.data_transformation_dir,"transformed",TRAIN_FILE_NAME.replace("csv","npz"))
        self.transformed_test_path=os.path.join(self.data_transformation_dir,"transformed",TEST_FILE_NAME.replace("csv","npz"))
        self.target_encoder_path=os.path.join(self.data_transformation_dir,"target_encoder",TARGET_ENCODER_OBJECT_FILE_NAME)
class ModelTrainerConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.model_trainer_dir=os.path.join(training_pipeline_config.artifact_dir,"model_trainer")
        self.model_path=os.path.join(self.model_trainer_dir,"model",MODEL_FILE_NAME)
        self.expected_score=0.70
        self.overfiiting_threshold=0.1
        
    
class ModelEvaluationConfig:
    pass
class ModelPusherConfig:
    pass

