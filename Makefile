ifneq (,$(wildcard ./.env))
    include .env
    export	
endif

clean:
	chmod +x scripts/* 
	pip uninstall -y -r requirements.txt
	scripts/clean.sh

setup: clean 
	pip install -r requirements.txt	
	scripts/create_folder.sh	

lint:
	flake8 

test:
	python -m pytest

run_data:
	python src/app/data/make_dataset.py  

run_train:
	python src/app/models/train_model.py  

build:
	docker build -t via/model:1.0 .

run_api:
	docker run -d --name model -p 80:80 -t via/model:1.0 

run_all: run_data run_train lint test build

