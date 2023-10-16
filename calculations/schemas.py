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
