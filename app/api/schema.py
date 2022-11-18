from pydantic import BaseModel, validator
from app.exceptions import exceptions


class CheckAPIResponse(BaseModel):
    """Элемент ответа от API"""

    item_id: str
    problem: str

    # @validator('item_id')
    # def name_must_contain_space(cls, v: str):
    #     try:
    #         v = v.split("_")
    #         v = int(v[1])
    #         ...
    #     except:
    #         raise exceptions.BaseDomainException
    #     return v
