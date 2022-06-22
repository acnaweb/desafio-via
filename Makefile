ifneq (,$(wildcard ./.env))
    include .env
    export	
endif

clean:
	chmod +x scripts/* 
	pip uninstall -y -r requirements.txt
	scripts/clean.sh

install: clean 
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
	docker build -t acnaweb/desafiovia:1.0 .

run_api:
	docker run -d --name model -p 80:80 -t acnaweb/desafiovia:1.0 

stop_api:
	docker rm model --force

tag_ecr:
	docker tag acnaweb/desafiovia:1.0 336119796486.dkr.ecr.us-east-2.amazonaws.com/api-desafiovia:latest

push:
	docker push 336119796486.dkr.ecr.us-east-2.amazonaws.com/api-desafiovia:latest
	

run_all: run_data run_train lint test build

