from pydantic import BaseModel


class UserDetails(BaseModel):
    user_id: int
    user_name: str
    address: str
    email: str


class Error(BaseModel):
    code: str
    message: str

class Response(BaseModel):
    status: bool
    data: object
    error: Error = None



