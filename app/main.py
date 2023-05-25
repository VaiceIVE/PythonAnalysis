from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from mongoService import Save, Get
from docConvertor import create_xls, create_xlsx
from fastapi.responses import StreamingResponse






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

    mock_result = {'result': [
        {'adress': 'улица Красковская, дом 121А', 'workname': ['Ремонт освещения', 'Сбивание сосулек'],"stats": {"Год постройки МКД": 1950, "Район": "Измайлово"}, "priority": "Срочная работа"},
        {'adress': 'улица Владимирская, дом 12', 'workname': ['Замена лестницы', 'Замена крыльца'],  "stats": {"Год постройки МКД": 1960, "Район": "Внуково"},"priority": "Плановая работа"},
        {'adress': 'улица Кусковская, дом 1', 'workname': ['Замена крыльца', 'Ремонт освещения'],  "stats": {"Год постройки МКД": 1970, "Район": "Сколково"},"priority": "Плановая работа"},
        {'adress': 'улица Бойцовая, дом 11', 'workname': ['Сбивание сосулек', 'Замена лестницы'],  "stats": {"Год постройки МКД": 1980, "Район": "Мытищи"},"priority": "Срочная работа"}
    ], 'type': 'base'}

    
    id = Save(mock_result)
    return {'result': [
        {'adress': 'улица Красковская, дом 121А', 'workname': ['Ремонт освещения', 'Сбивание сосулек'],"stats": {"Год постройки МКД": 1950, "Район": "Измайлово"}, "priority": "Срочная работа"},
        {'adress': 'улица Владимирская, дом 12', 'workname': ['Замена лестницы', 'Замена крыльца'],  "stats": {"Год постройки МКД": 1960, "Район": "Внуково"},"priority": "Плановая работа"},
        {'adress': 'улица Кусковская, дом 1', 'workname': ['Замена крыльца', 'Ремонт освещения'],  "stats": {"Год постройки МКД": 1970, "Район": "Сколково"},"priority": "Плановая работа"},
        {'adress': 'улица Бойцовая, дом 11', 'workname': ['Сбивание сосулек', 'Замена лестницы'],  "stats": {"Год постройки МКД": 1980, "Район": "Мытищи"},"priority": "Срочная работа"}
    ], 'type': 'base', '_id' : id}



@app.get('/worktypes')
def get_worktypes():
    return ['']

@app.get('/objcategories')
def get_object_categories():
    return ['Многоквартирный дом']

@app.get('/xlsbyid/{id}')
def get_xls_report_by_analysis_id(id):
    result = Get(id)

    return StreamingResponse(create_xls(result), media_type="application/vnd.ms-excel")

@app.get('/xlsxbyid/{id}')
def get_xls_report_by_analysis_id(id):
    result = Get(id)

    return StreamingResponse(create_xls(result), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
