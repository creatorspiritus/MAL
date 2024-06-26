from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum



class ТипАэродрома(str, Enum):
    """Тип аэродрома"""
    АЭРОДРОМ = "АЭРОДРОМ"
    ВЕРТОДРОМ = "ВЕРТОДРОМ"
    ГИДРОДРОМ = "ГИДРОДРОМ"
    ПЛОЩАДКА = "ПЛОЩАДКА"



class Покрытие(str, Enum):
    """Класс применяется для определения типа покрытия основной ВПП"""
    БЕТОН = "БЕТОН"
    ГРУНТ = "ГРУНТ"




class Полоса(SQLModel, table=True):
    пк: Optional[int] = Field(default=None, primary_key=True)
    название: str
    длина: int
    ширина: int




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
    иата: str = Field(title='Код ИКАО', unique=True, max_length=3, min_length=3)
    аэродром: Аэродром
    название: Optional[str] = Field(default=None)