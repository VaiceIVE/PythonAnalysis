from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=
    [
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/analyze')
def analyze_simple():
    return{'result': [
        {'adress': 'Красковская ул., д.121А', 'workname': ['Ремонт освещения', 'Сбивание сосулек'],"stats": {"Год постройки МКД": 1950, "Район": "Измайлово"}, "priority": "Срочная работа"},
        {'adress': 'Владимирская ул., д.12', 'workname': ['Замена лестницы', 'Замена крыльца'],  "stats": {"Год постройки МКД": 1960, "Район": "Внуково"},"priority": "Плановая работа"},
        {'adress': 'Кусковская ул., д.1', 'workname': ['Замена крыльца', 'Ремонт освещения'],  "stats": {"Год постройки МКД": 1970, "Район": "Сколково"},"priority": "Плановая работа"},
        {'adress': 'Бойцовая ул., д.11', 'workname': ['Сбивание сосулек', 'Замена лестницы'],  "stats": {"Год постройки МКД": 1980, "Район": "Мытищи"},"priority": "Срочная работа"}
    ], 'type': 'base', '_id': "testid"}

