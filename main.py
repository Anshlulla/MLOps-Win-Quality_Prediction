from src.project import logger
from src.project.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.project.pipeline.data_validation_pipeline import DataValidationPipeline
from src.project.pipeline.data_transformation_pipeline import DataTranformationPipeline

## --------- Data Ingestion ------------
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage '{STAGE_NAME}' started <<<<")
    obj = DataIngestionPipeline()
    obj.intiate_data_ingestion()
    logger.info(f">>>> stage '{STAGE_NAME}' completed <<<<\n\n")
except Exception as e:
    raise e

## --------- Data Validation ------------
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>> stage '{STAGE_NAME}' started <<<<")
    obj = DataValidationPipeline()
    obj.intiate_data_validation()
    logger.info(f">>>> stage '{STAGE_NAME}' completed <<<<\n\n")
except Exception as e:
    raise e

## --------- Data Transformation ------------
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>> stage '{STAGE_NAME}' started <<<<")
    obj = DataTranformationPipeline()
    obj.intiate_data_tranformation()
    logger.info(f">>>> stage '{STAGE_NAME}' completed <<<<\n\n")
except Exception as e:
    raise e