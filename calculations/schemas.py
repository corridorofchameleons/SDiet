from pydantic import BaseModel


class RecordCreate(BaseModel):

    user_id: int
    date: str
    name: str
    weight: float
    protein: float
    fats: float
    carbohydrates: float
    calories: float


class UpdateLimits(BaseModel):

    user_id: int | None = None
    protein: float | None = None
    fats: float | None = None
    carbohydrates: float | None = None
    calories: float | None = None

