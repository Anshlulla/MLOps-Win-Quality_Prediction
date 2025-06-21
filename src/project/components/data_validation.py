import pandas as pd
import os
from src.project.entity.config_entity import DataValidationConfig
from src.project import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_data(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_dir)
            cols = list(data.columns)
            schema = self.config.schema.keys()
            validation_status = None
            
            for col in cols:
                if col not in schema:
                    validation_status = False
                else:
                    validation_status = True
            
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation Status: {validation_status}")
            
            return validation_status
        
        except Exception as e:
            raise e 