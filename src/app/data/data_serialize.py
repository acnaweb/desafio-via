import pandas as pd
import logging
import cloudpickle

# dataset defaults (no change)
RAW_DATASET: str = "./data/raw/dataset.csv"
INTERIM_DATASET: str = "./data/interim/dataset.csv"
PROCESSED_X_TRAIN: str = "./data/processed/x_train.csv"
PROCESSED_X_TEST: str = "./data/processed/x_test.csv"
PROCESSED_Y_TRAIN: str = "./data/processed/y_train.csv"
PROCESSED_Y_TEST: str = "./data/processed/y_test.csv"
MODEL_PATH: str = "./model/"


def load_interim_dataset() -> pd.DataFrame:
    """get_interim_dataset"""

    return pd.read_csv(INTERIM_DATASET)


def save_dataset(dataset: pd.DataFrame, filename: str):
    """save_dataset"""

    try:
        dataset.to_csv(filename, index=False)
    except Exception as e:
        logging.error("Erro ao salvar datasets {}:{}".format(filename, e))


def save_raw_dataset(dataset: pd.DataFrame):
    """save_raw_dataset"""

    save_dataset(dataset, RAW_DATASET)


def save_interim_dataset(dataset: pd.DataFrame):
    """save_interim_dataset"""

    save_dataset(dataset, INTERIM_DATASET)


def save_processed_dataset(X_train: pd.DataFrame, X_test: pd.DataFrame,
        y_train: pd.DataFrame, y_test: pd.DataFrame):
    """save_processed_dataset"""

    save_dataset(X_train, PROCESSED_X_TRAIN)
    save_dataset(X_test, PROCESSED_X_TEST)
    save_dataset(y_train, PROCESSED_Y_TRAIN)
    save_dataset(y_test, PROCESSED_Y_TEST)


def load_processed_dataset():
    """load_processed_dataset"""

    X_train = pd.read_csv(PROCESSED_X_TRAIN)
    X_test = pd.read_csv(PROCESSED_X_TEST)
    y_train = pd.read_csv(PROCESSED_Y_TRAIN)
    y_test = pd.read_csv(PROCESSED_Y_TEST)

    return (X_train, X_test, y_train, y_test)


def save_artifact(object, filename: str):
    """save_artifact"""

    with open("{}{}".format(MODEL_PATH, filename), 'wb') as pickle_file:
        logging.info(pickle_file)
        cloudpickle.dump(object, pickle_file)


def load_artifact(filename: str):
    """load_artifact"""

    with open("{}{}".format(MODEL_PATH, filename), 'rb') as pickle_file:
        logging.info(pickle_file)

        return cloudpickle.load(pickle_file)
