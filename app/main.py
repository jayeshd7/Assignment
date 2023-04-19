

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from app.api import api
from app.db.models import UserDetails, Response, Error
from app.exception.data_not_found import DataNotFound
import logging

app = FastAPI()

def response():
    return "It's working ✨"

@app.exception_handler(DataNotFound)
async def data_not_found_exception(request: Request, exc: DataNotFound):
    response = Response(status=False, data = None, error = Error(code = 404, message = exc.message))
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(response),
    )

@app.get("/")
async def root():
    return {"message": "Fast API in Python"}


@app.post("/user", status_code=201)
async def create_user(payload: UserDetails):
    return create_new_user(payload)


def create_new_user(payload: UserDetails):
    return api.create_user(payload)

@app.get("/user/{user_id}")
async def read_alternatives(user_id: int):
    response = Response(status=True, data=api.get_user_by_id(user_id))
    return response
