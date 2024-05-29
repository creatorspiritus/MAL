from sqlmodel import SQLModel, Field
from collections import namedtuple
import json

К = namedtuple('КТА', 'широта долгота превышение')

# class Город(SQLModel):
#     """
#     Класс "Город" описывает данные населённых пунктов
#     """
#     id: int | None = Field(default=None, primary_key=True)
#     регион: str | None
#     район: str | None
#     город: str | None
#     жителей: int | None
#     широта: float | None
#     долгота: float | None


class Аэродром(SQLModel):
    """
    Класс "Аэродром" описывает данные аэродрома
    """
    id: int | None = Field(default=None, primary_key=True)
    IATA: str | None = Field(max_length=3)
    ICAO: str | None = Field(max_length=4)
    город: str | None
    название: int | None
    широта: float | None
    долгота: float | None



class Муниципалитет(SQLModel):
    """
    Класс "Муниципалитет" описывает данные населённого пункта
    """
    id: int | None = Field(default=None, primary_key=True)
    регион: str | None
    район: int | None
    название: float | None
    тип: float | None
    широта: float | None
    долгота: float | None
    население: int | None