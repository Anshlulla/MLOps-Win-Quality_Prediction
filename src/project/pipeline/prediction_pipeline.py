import joblib
import pandas as pd
from pathlib import Path
import numpy as np

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
    
    def predict(self, data):
        y_pred = self.model.predict(data)

        return y_pred
    
    