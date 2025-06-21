from src.project.config.configuration import ConfigurationManager
from src.project.components.data_transformation import DataTransformation
from src.project import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTranformationPipeline:
    def __init__(self):
        pass

    def intiate_data_tranformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
            if status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_tranformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data scheme is not valid")
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>> stage '{STAGE_NAME}' started <<<<")
        obj = DataTranformationPipeline()
        obj.intiate_data_tranformation()
        logger.info(f">>>> stage '{STAGE_NAME}' completed <<<<")
    except Exception as e:
        raise e