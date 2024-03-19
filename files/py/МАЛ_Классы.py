from sqlmodel import SQLModel, Field
from typing import Optional



class Полоса(SQLModel, table=True):
    пк: Optional[int] = Field(default=None, primary_key=True)
    название: str



class Точка(SQLModel, table=True):
    пк: Optional[int] = Field(default=None, primary_key=True)
    широта: float
    долгота: float
    превышение: Optional[int] = Field(default=None)



class Аэродром(SQLModel, table=True):
    пк: Optional[int] = Field(default=None, primary_key=True)
    icao: str = Field(title='Код ICAO', unique=True, max_length=4, min_length=4)
    икао: str = Field(title='Код ИКАО', unique=True, max_length=4, min_length=4)
    название: Optional[str] = Field(default=None)
    кта: Точка



class Аэропорт(SQLModel, table=True):
    пк: Optional[int] = Field(default=None, primary_key=True)
    iata: str = Field(title='Код IATA', unique=True, max_length=3, min_length=3)
    икао: str = Field(title='Код ИКАО', unique=True, max_length=3, min_length=3)
    аэродром: Аэродром