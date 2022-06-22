# Desafio Via
    Esse desafio consiste em treinar um modelo de machine learning que classifique as flores em suas respectivas espécies (Iris Dataset) e disponibilizar o modelo treinado em formato de API.
---
## Cloud AWS

#### Dados de acesso
| Item | URL |
|------|-----|
| Url base | http://3.144.218.69 |
| Docs/Test (Swagger) | http://3.144.218.69/docs |
| Predict (endpoint) | http://3.144.218.69/invocations |

- Exemplo de request
`
curl -X 'POST' \
  'http://3.144.218.69/invocations' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length_in_cm": 0,
  "sepal_width_in_cm": 0,
  "petal_length_in_cm": 0,
  "petal_width_in_cm": 0
}'
`    
---

## Dev Setup 

#### Pre req
    - Git
    - Conda
    - Docker
    - Python 3.8

#### Conda environment
    - conda create --name desafiovia python=3.8
    - conda activate desafiovia

#### Install (run in project folder)
    - make install
---
## Data Science
#### Data Ingestion and Data Processing

    - make run_data
*Verificar na pasta **/data** os datasets gerados*
    
#### Training and Validation

    - make run_train
*Verificar na pasta* **/model** *os artefatos de modelo e pipeline transformação*
    
#### Quality 

Unit test (run in project folder)
    
    - make test

Code quality (run in project folder)

    - make lint

### Run (local)

Build Docker Image

    - make build

Run Container

    - make run_api
    
| Item | URL |
|------|-----|
| Url base | http://localhost |
| Docs/Test (Swagger) | http://localhost/docs |
| Predict (endpoint) | http://localhost/invocations |

- Exemplo de request
`
curl -X 'POST' \
  'http://localhost/invocations' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length_in_cm": 3,
  "sepal_width_in_cm": 2,
  "petal_length_in_cm": 1.0,
  "petal_width_in_cm": 3
}'
`    

Stop run 

    - make stop_api


### Continuous Integration

Evento: on push branch main
    
    - make install
    - make lint
    - make test

Project Organization
------------

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── model             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

