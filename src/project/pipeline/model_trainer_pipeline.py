from src.project.config.configuration import ConfigurationManager
from src.project.components.model_trainer import ModelTrainer
from src.project import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def intiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
    
if __name__ == "__main__":
    try:
        logger.info(f">>>> stage '{STAGE_NAME}' started <<<<")
        obj = ModelTrainerPipeline()
        obj.intiate_model_trainer()
        logger.info(f">>>> stage '{STAGE_NAME}' completed <<<<")
    except Exception as e:
        raise e