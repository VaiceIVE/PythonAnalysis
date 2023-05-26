from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from mongoService import Save, Get, Getall, Delete
from docConvertor import create_xls, create_csv
from fastapi.responses import StreamingResponse
from IResult import IResult
from ICriteria import ICriteria







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
    ], 'type': 'base', 'criterias': ['МКД', 'Капитальный ремонт'], 'date': '03.08.2003'}

    
    id = Save(mock_result)
    return {'result': [
        {'adress': 'улица Красковская, дом 121А', 'workname': ['Ремонт освещения', 'Сбивание сосулек'],"stats": {"Год постройки МКД": 1950, "Район": "Измайлово"}, "priority": "Срочная работа"},
        {'adress': 'улица Владимирская, дом 12', 'workname': ['Замена лестницы', 'Замена крыльца'],  "stats": {"Год постройки МКД": 1960, "Район": "Внуково"},"priority": "Плановая работа"},
        {'adress': 'улица Кусковская, дом 1', 'workname': ['Замена крыльца', 'Ремонт освещения'],  "stats": {"Год постройки МКД": 1970, "Район": "Сколково"},"priority": "Плановая работа"},
        {'adress': 'улица Бойцовая, дом 11', 'workname': ['Сбивание сосулек', 'Замена лестницы'],  "stats": {"Год постройки МКД": 1980, "Район": "Мытищи"},"priority": "Срочная работа"}
    ], 'type': 'base', '_id' : id}



@app.get('/worktypes')
def get_worktypes():
    return ['Капитальный ремонт']

@app.get('/objcategories')
def get_object_categories():
    return ['Многоквартирный дом']

@app.get('/xlsbyid/{id}/{name}')
def get_xls_report_by_analysis_id(id, name):
    result = Get(id)

    return StreamingResponse(create_xls(result), headers={'Content-Disposition': f'attachment; filename="{name}.xls"'.encode('utf-8').decode('unicode-escape')}, media_type="application/vnd.ms-excel")

@app.get('/xlsxbyid/{id}/{name}')
def get_xlsx_report_by_analysis_id(id, name):
    result = Get(id)

    return StreamingResponse(create_xls(result), headers={'Content-Disposition': f'attachment; filename="{name}.xlsx"'.encode('utf-8').decode('unicode-escape')}, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@app.get('/csvbyid/{id}/{name}')
def get_xlsx_report_by_analysis_id(id, name):
    result = Get(id)

    return StreamingResponse(create_csv(result), headers={'Content-Disposition': f'attachment; filename="{name}.csv"'.encode('utf-8').decode('unicode-escape')}, media_type="application/vnd.ms-excel")

@app.get('/history')
def get_history():
    results = Getall()

    print(results)
    response = list()

    for result in results:
        response.append({"type": result['type'], "date": result['date'], "criterias": result['criterias'], 'id': str(result['_id']) })

    return response

@app.get('/analyze/{id}')
def get_analyze_by_id(id):
    
    result = Get(id)

    return result

@app.post('/analyze/update')
def update_analysis_data(result: IResult):
    Delete(result.id)
    id = Save(result.ToDict())
    return id

@app.post('/analyze/criterized')
def update_analysis_data(criterias: ICriteria):
    objtype = criterias.obj
    worktype = criterias.work
    dates = criterias.date


    mock_result = {'result': [
        {'adress': 'улица Красковская, дом 121А', 'workname': ['Ремонт освещения', 'Сбивание сосулек'],"stats": {"Год постройки МКД": 1950, "Район": "Измайлово"}, "priority": "Срочная работа"},
        {'adress': 'улица Владимирская, дом 12', 'workname': ['Замена лестницы', 'Замена крыльца'],  "stats": {"Год постройки МКД": 1960, "Район": "Внуково"},"priority": "Плановая работа"},
        {'adress': 'улица Кусковская, дом 1', 'workname': ['Замена крыльца', 'Ремонт освещения'],  "stats": {"Год постройки МКД": 1970, "Район": "Сколково"},"priority": "Плановая работа"},
        {'adress': 'улица Бойцовая, дом 11', 'workname': ['Сбивание сосулек', 'Замена лестницы'],  "stats": {"Год постройки МКД": 1980, "Район": "Мытищи"},"priority": "Срочная работа"}
    ], 'type': 'base', 'criterias': [objtype, worktype, dates], 'date': '03.08.2003'}

    
    id = Save(mock_result)
    return {'result': [
        {'adress': 'улица Красковская, дом 121А', 'workname': ['Ремонт освещения', 'Сбивание сосулек'],"stats": {"Год постройки МКД": 1950, "Район": "Измайлово"}, "priority": "Срочная работа"},
        {'adress': 'улица Владимирская, дом 12', 'workname': ['Замена лестницы', 'Замена крыльца'],  "stats": {"Год постройки МКД": 1960, "Район": "Внуково"},"priority": "Плановая работа"},
        {'adress': 'улица Кусковская, дом 1', 'workname': ['Замена крыльца', 'Ремонт освещения'],  "stats": {"Год постройки МКД": 1970, "Район": "Сколково"},"priority": "Плановая работа"},
        {'adress': 'улица Бойцовая, дом 11', 'workname': ['Сбивание сосулек', 'Замена лестницы'],  "stats": {"Год постройки МКД": 1980, "Район": "Мытищи"},"priority": "Срочная работа"}
    ], 'type': 'base', 'criterias': [objtype, worktype, dates], 'date': '03.08.2003', "_id": id}
    