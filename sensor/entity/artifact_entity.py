from dataclasses import dataclass
@dataclass

class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str
    
class DataTransformationArtifact:
    pass
class ModelTrainerArtifact:
    pass
class ModelEvaluationArtifact:
    pass
class ModelPusherArtifact:
    pass