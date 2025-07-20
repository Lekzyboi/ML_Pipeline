import os
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.mlproject.entity.config_entity import ModelEvaluationConfig

from src.mlproject.constants import *
from src.mlproject.utils import read_yaml, create_directories, save_json

import os
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/Lakehone/ML_Pipeline.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Lakehone"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "761c242e294f115aac54a7f4acc6b114c878e85a"


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            rmse, mae, r2 = self.eval_metrics(test_y, predicted_qualities)

            # Save metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log params & metrics to MLflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"rmse": rmse, "r2": r2, "mae": mae})

            # Save model manually & log as artifact (works on DagsHub & any MLflow)
            joblib.dump(model, "model.pkl")
            mlflow.log_artifact("model.pkl")