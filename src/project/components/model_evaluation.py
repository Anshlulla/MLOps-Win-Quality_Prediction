import pandas as pd
import os
from src.project.entity.config_entity import ModelEvaluationConfig
from src.project import logger
from src.project.utils.common import save_json
from pathlib import Path
import mlflow
import joblib
import mlflow.sklearn
from urllib.parse import urlparse
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import pandas as pd

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, y_test, y_pred):
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        return mse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            y_pred = model.predict(X_test)
            mse, mae, r2 = self.eval_metrics(y_test, y_pred)
            scores = {"mae": mae, "mse": mse, "r2": r2}
            save_json(path=Path(self.config.metrics_file_name), data=scores)

            mlflow.log_params(self.config.params)
            mlflow.log_metric("mse", mse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")