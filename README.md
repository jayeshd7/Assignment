# fastapi-example 

A simple example of using Fast API in Python.

## Preconditions:

- Python3

## Clone the project

```
https://github.com/jayeshd7/Assignment
```

## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

### Run test

```
pytest app/test.py
```

## Run with docker

### Run server

```
docker-compose up -d 
```

### Run test

```
docker-compose exec app pytest test/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

### Run server

```
docker-compose exec db psql --username=fastapi --dbname=fastapi_dev
```

### Run Unit Test cases
```
pytest -v
```

### safe to put : kafka & kafdrop up & down locally

```
docker-compose --file kafka-compose.yml up -d
docker-compose --file kafka-compose.yml down


```