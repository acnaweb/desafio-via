# ml-framework
ML Framework

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### Setup

* Pre requisitos
- Git
- Conda
- Docker
- Python 3.8

* Conda: create environment
- conda create --name desafiovia python=3.8
- conda activate desafiovia

* Install
- make install

### Data Science

* Data Ingestion and Data Processing
- make run_data

* Training and Validation
- make run_train

### Quality

* Unit test
- make test

* Code quality
- make lint

### Continuous Integration

- on push branch main

### Cloud AWS

- url base: http://3.144.218.69/
- docs (Swagger): http://3.144.218.69/docs 
- predict (endpoint): http://3.144.218.69/invocations

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

### Run (local)

* Build Docker Image
- make build

* Run Container
- make run_api

* API

- url base: http://localhost
- docs (Swagger): http://localhost/docs
- predict (endpoint): http://localhost/invocations

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

* Stop run 
- make stop_api









#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 3.8+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

desafio-via
==============================

Desafio Via

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
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

