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
        {'adress': 'Красковская ул., д.121А', 'workname': 'Ремонт освещения', 'type': 'base'},
        {'adress': 'Владимирская ул., д.12', 'workname': 'Замена лестницы', 'type': 'smartDb'},
        {'adress': 'Кусковская ул., д.1', 'workname': 'Замена крыльца', 'type': 'smartFile'},
        {'adress': 'Бойцовая ул., д.11', 'workname': 'Сбивание сосулек', 'type': 'smartUrl'}
    ]}

