from fastapi import FastAPI
from .schemas import DataRequest
from src.mediassist.core.crews import MedicalCrew
from src.mediassist.utils.environment import load_env_vars

load_env_vars()

app = FastAPI()


@app.post("/ai")
async def calculate_data(request: DataRequest):
    crew = MedicalCrew(request.language)

    if request.language == "en":
        data = f"Name: {request.name}, Gender: {request.gender}, Age: {request.age}, Weight: {request.weight} kg, Height: {request.height} cm, Occupation: {request.occupation}, Physical Activity: {request.physical_activity}, Diet: Fats: {request.fats}, Sugars: {request.sugars}, Ready Meals: {request.ready_meals}, Vegetarian: {request.vegetarian}, Family Medical History: Diabetes: {request.diabetes}, Chronic Diseases: {request.chronic_diseases}, Symptoms: {request.symptoms}"
    elif request.language == "ar":
        data = f"الاسم: {request.name}, النوع: {request.gender}, السن: {request.age}, الوزن: {request.weight} كيلو, الطول: {request.height} سم, الوظيفة: {request.occupation}, النشاط البدني: {request.physical_activity}, النظام الغذائي: الدهون: {request.fats}, السكريات: {request.sugars}, الأكل الجاهز: {request.ready_meals}, نباتي: {request.vegetarian}, تاريخ العيلة الطبي: السكر: {request.diabetes}, الأمراض المزمنة: {request.chronic_diseases}, الأعراض: {request.symptoms}"
    else:
        return {"message": "Language not supported"}

    result = crew.run_crew(data)
    return {"data": result}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
