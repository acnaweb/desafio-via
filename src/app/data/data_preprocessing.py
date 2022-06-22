import logging
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from data_serialize import (load_interim_dataset,
    save_processed_dataset,
    save_artifact)


# define features
COLUMN_FEATURES: list = ["sepal length in cm",
    "sepal width in cm",
    "petal length in cm",
    "petal width in cm"]

# define target/class column
COLUMN_TARGET: list = ["class"]


class DataPreprocessing:
    """DataPreprocessing"""

    def run_task(self):
        """run_task"""

        logging.info("running DataPreprocessing")

        # load dataset
        dataset: pd.DataFrame = load_interim_dataset()

        # get features and target
        X, y = self.get_feature_and_target(dataset)

        # fit pipeline transformation
        pipeline: Pipeline = self.get_transform_pipeline()
        pipeline.fit(X)

        # serialize pipeline
        save_artifact(pipeline, "pipeline.pkl")

        # split dataset
        X_train, X_test, y_train, y_test = self.train_test_split(X, y)

        # save datasets
        self.save(X_train, X_test, y_train, y_test)

    def get_feature_and_target(self, dataset: pd.DataFrame):
        """get_feature_and_target"""

        X: pd.DataFrame = dataset[COLUMN_FEATURES]
        y: pd.DataFrame = dataset[COLUMN_TARGET]

        return (X, y)

    def train_test_split(self, X: pd.DataFrame, y: pd.DataFrame):
        """train_test_split"""

        X_train, X_test, y_train, y_test = train_test_split(X, y)

        return (X_train, X_test, y_train, y_test)

    def save(self, X_train: pd.DataFrame, X_test: pd.DataFrame,
            y_train: pd.DataFrame, y_test: pd.DataFrame):
        """save_processed_dataset"""

        save_processed_dataset(X_train, X_test, y_train, y_test)

    def get_transform_pipeline(self) -> Pipeline:
        """get_transform_pipeline"""

        pipeline: Pipeline = Pipeline([('scaler', StandardScaler())])

        return pipeline
