from pydantic import BaseModel


class OperationCreate(BaseModel):
    name: str
    protein: float
    fats: float
    carbohydrates: float
    calories: float
    category: int
