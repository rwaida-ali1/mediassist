from pydantic import BaseModel


class DataRequest(BaseModel):
    name: str
    gender: str
    age: int
    weight: int
    height: int
    occupation: str
    physical_activity: str
    fats: str
    sugars: str
    ready_meals: str
    vegetarian: str
    diabetes: str
    chronic_diseases: str
    symptoms: str
    language: str
