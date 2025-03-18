from typing import Optional
from sqlmodel import Field, SQLModel


class Performance(SQLModel, table=True):

    id : Optional[int] = Field(default=None, primary_key=True)
    athlete_id: int | None = Field(default=None, foreign_key="athlete.id")
    power_max: int
    hr_max: int
    vo2_max: int
    rf_max: int
    cadence_max: int