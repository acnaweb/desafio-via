import pandas as pd
import logging
from data_serialize import save_interim_dataset, save_raw_dataset


# define column names
COLUMNS: list = ["sepal length in cm",
        "sepal width in cm",
        "petal length in cm",
        "petal width in cm",
        "class"]

# define column and row size
NUM_COLUMNS: int = 5
NUM_ROWS: int = 149
URL: str = "https://archive.ics.uci.edu/ml/" + \
    "machine-learning-databases/iris/iris.data"


def load_dataset() -> pd.DataFrame:
    """load_dataset"""
    dataset: pd.DataFrame = pd.read_csv(URL)
    return dataset


class InvalidDataError(Exception):
    pass


class DataIngestion:
    """Processo de ETL"""

    def run_task(self):
        """run_task"""

        logging.info("running DataIngestion")

        dataset = self.load()

        try:
            self.validate(dataset)

            dataset.columns = COLUMNS

        except InvalidDataError as e:
            logging.error("Dataset invalido {}".format(e))

        else:
            self.save(dataset)

    def load(self) -> pd.DataFrame:
        """load"""

        dataset: pd.DataFrame = load_dataset()

        save_raw_dataset(dataset)

        return dataset

    def validate(self, dataset: pd.DataFrame):
        """validate"""

        # validate shape
        if dataset.shape[0] != NUM_ROWS:
            raise InvalidDataError("rows: expected {} load {}"
                .format(dataset.shape[0], NUM_ROWS))

        if dataset.shape[1] != NUM_COLUMNS:
            raise InvalidDataError("columns: expected {} load {}"
                .format(dataset.shape[1], NUM_COLUMNS))

    def save(self, dataset: pd.DataFrame):
        """save"""

        save_interim_dataset(dataset)
