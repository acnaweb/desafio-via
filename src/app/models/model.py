import logging
from sklearn.linear_model import LogisticRegression
from data_serialize import load_artifact
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score)
from validation import custom_validate_performance


class Model(LogisticRegression):

    def train(self, data):
        """Train and test the model instance, from the given dataset."""
        logging.info("start training")

        # split data
        self.X_train, self.X_test, self.y_train, self.y_test = data

        # remove header
        self.X_train = self.X_train.iloc[1:, :]
        self.X_test = self.X_test.iloc[1:, :]
        self.y_train = self.y_train.iloc[1:, :].values.ravel()
        self.y_test = self.y_test.iloc[1:, :].values.ravel()

        # load pipeline transformation
        pipeline = load_artifact("pipeline.pkl")

        # run transformation
        self.X_train_trans = pipeline.transform(self.X_train)
        self.X_test_trans = pipeline.transform(self.X_test)

        # fit
        self.fit(self.X_train_trans, self.y_train)
        logging.info("end training")

        # validate
        self.validate_training()

    def validate_training(self):
        """Validate that the training was successful."""

        logging.info("start validation")

        # predictions
        logging.info("start predictions")
        self.y_train_pred = self.predict(self.X_train_trans)
        self.y_test_pred = self.predict(self.X_test_trans)
        logging.info("end predictions")

        # evaluate train
        performance_train = self.evaluate_performance(
            self.y_train,
            self.y_train_pred)

        custom_validate_performance(performance_train)

        # evaluate test
        performance_test = self.evaluate_performance(
            self.y_test,
            self.y_test_pred)

        custom_validate_performance(performance_test)

        logging.info("end validation")

    def evaluate_performance(self, y_test, y_pred) -> dict:
        """evaluate_performance"""

        data = {
            "accuracy": accuracy_score(y_test, y_pred),
            "f1_macro": f1_score(y_test, y_pred, average='macro'),
            "f1_micro": f1_score(y_test, y_pred, average='micro'),
            "precision": precision_score(y_test, y_pred, average='micro'),
            "recall": recall_score(y_test, y_pred, average='micro')
        }
        return data
