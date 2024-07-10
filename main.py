from textSummarizer.pipeline.text_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.text_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.text_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.text_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.text_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e
