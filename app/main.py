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
        {'adress': 'Красковская ул., д.121А', 'workname': ['Ремонт освещения', 'Сбивание сосулек'], "priority": "Срочная работа"},
        {'adress': 'Владимирская ул., д.12', 'workname': ['Замена лестницы', 'Замена крыльца'],  "priority": "Плановая работа"},
        {'adress': 'Кусковская ул., д.1', 'workname': ['Замена крыльца', 'Ремонт освещения'],  "priority": "Плановая работа"},
        {'adress': 'Бойцовая ул., д.11', 'workname': ['Сбивание сосулек', 'Замена лестницы'],  "priority": "Срочная работа"}
    ], 'type': 'base'}

