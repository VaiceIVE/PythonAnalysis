from pydantic import BaseModel

class ICriteria(BaseModel):
    obj: string,
    work: string,
    date: list