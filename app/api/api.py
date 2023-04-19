from app.db import user_repository
from app.db.models import Response
from app.exception.data_not_found import DataNotFound


def create_user(payload):
    response = Response(status=True, data=payload)
    user_repository.save(payload)
    return response


def get_user_by_id(user_id: int):
    user = user_repository.get(user_id)
    if user is None:
        raise DataNotFound(message="user id not found")
    else:
        return user