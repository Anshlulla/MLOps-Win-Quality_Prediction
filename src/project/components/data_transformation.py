import pandas as pd
import os
from src.project.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from src.project import logger

class DataTransformation:
    def __init__(self, config = DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data, test_size=0.2, random_state=42)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Split the data into train-test sets")
        logger.info(f"Train data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")

        print(train.shape, test.shape)
