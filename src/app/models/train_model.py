import logging
from model import Model
from data_serialize import load_processed_dataset, save_artifact


def run_train():
    model = Model()
    model.train(load_processed_dataset())
    logging.info("serialize model")
    save_artifact(model, "model.pkl")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    run_train()
