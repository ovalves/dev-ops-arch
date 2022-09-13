from pydantic import BaseModel

class BaseError(BaseModel):
    message: str
    status_code: int