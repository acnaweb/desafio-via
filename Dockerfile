FROM python:3.8-slim-buster

EXPOSE 80

WORKDIR /

COPY ./requirements_image.txt ./requirements.txt
COPY ./src/app/models/* /app/
COPY ./model/* /app/model/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
