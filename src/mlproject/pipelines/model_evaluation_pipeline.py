from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_evaluation import ModelEvaluation
from src.mlproject import logger


STAGE_NAME="Model Evaluation"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        data_evaluation_config = config.get_model_evaluation_config()
        data_evaluation_config = ModelEvaluation(config=data_evaluation_config)
        data_evaluation_config.log_into_mlflow()
