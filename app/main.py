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
        {'Адрес': 'Красковская ул., д.121А', 'Наименование работы': 'Ремонт освещения'},
        {'Адрес': 'Владимирская ул., д.12', 'Наименование работы': 'Замена лестницы'},
        {'Адрес': 'Кусковская ул., д.1', 'Наименование работы': 'Замена крыльца'},
        {'Адрес': 'Бойцовая ул., д.11', 'Наименование работы': 'Сбивание сосулек'}
    ]}

