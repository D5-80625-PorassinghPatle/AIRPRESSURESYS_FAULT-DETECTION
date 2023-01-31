import os

FILE_NAME="sensor.csv"
TRAIN_FILE_NAME="train.csv"
TEST_FIEL_NAME="test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        self.artifact_dir=os.path.join(os.getcwd(),"artifacct",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")


class DataIngestionConfig:

    def __init__(self,trainingpipelineconfig:TrainingPipelineConfig):

        self.database_name="airpressuresys"
        self.collection_name="sensor"
        self.data_ingestion_dir=os.path.join(trainingpipelineconfig.artifact_dir,"data_ingestion")
        self.feature_store_dir=os.path.join(self.data_ingestion_dir,"feature_store")

    def to_dict(self,)->dict:

        try:
            return self.__dict__
        except Exception as e:

            raise SensorException(e,sys)



class DataValidationConfig:
    pass
class DataTransformationConfig:
    pass
class ModelTrainerConfig:
    pass
class ModelEvaluationConfig:
    pass
class ModelPusherConfig:
    pass

