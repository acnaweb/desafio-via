import cloudpickle
import model
from fastapi import FastAPI
from pydantic import BaseModel


# load pipeline transformation
with open("./model/pipeline.pkl", 'rb') as pickle_file:
    pipeline = cloudpickle.load(pickle_file)

# load model
with open("./model/model.pkl", 'rb') as pickle_file:
    model = cloudpickle.load(pickle_file)

# load classes do predict
CLASSES = model.classes_.tolist()

# initiate API
app = FastAPI()


# define model for post request.
class ModelParams(BaseModel):
    sepal_length_in_cm: float
    sepal_width_in_cm: float
    petal_length_in_cm: float
    petal_width_in_cm: float


def get_prediction(params: ModelParams):
    """get_prediction"""

    x = [[params.sepal_length_in_cm, params.sepal_width_in_cm,
        params.petal_length_in_cm, params.sepal_width_in_cm]]
    x_trans = pipeline.transform(x)
    y = model.predict(x_trans)[0]
    prob = model.predict_proba(x_trans).tolist()
    d = {'category': CLASSES, 'probability': prob}
    return {'prediction': y, 'probability': d}


@app.post("/invocations")
def invocation(params: ModelParams):
    prediction = get_prediction(params)
    return prediction
