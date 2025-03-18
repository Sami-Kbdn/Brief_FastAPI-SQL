from typing import Optional
from sqlmodel import Field, SQLModel


class Athlete(SQLModel, table=True):

    id : Optional[int] = Field(default=None, primary_key=True)
    first_name : str = Field(max_length=255,unique=True)
    last_name : str = Field(max_length=255,unique=True)
    weight: int
    age: int
    height: int