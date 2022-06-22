import logging
from data_ingestion import DataIngestion
from data_preprocessing import DataPreprocessing


def workflow():
    """workflow"""
    dataIngestion = DataIngestion()
    dataIngestion.run_task()

    dataPreprocessing = DataPreprocessing()
    dataPreprocessing.run_task()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    workflow()
