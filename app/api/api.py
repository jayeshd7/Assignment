from app.db import user_repository
from app.db.models import Response
from app.exception.data_not_found import DataNotFound
from app.kafka.kafka import produce_message
import json


def create_user(payload):
    response = Response(status=True, data=payload)
    user_repository.save(payload)
    produce_message(str(json.loads(payload.json())), 'com.persistance.test')
    return response


def get_user_by_id(user_id: int):
    user = user_repository.get(user_id)
    if user is None:
        raise DataNotFound(message="user id not found")
    else:
        return user