FROM python:3.8-slim-buster

EXPOSE 80

COPY ./requirements_image.txt /webapp/requirements.txt

WORKDIR /webapp

COPY ./src/app/models/* /webapp/
COPY ./model/* /webapp/model/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
