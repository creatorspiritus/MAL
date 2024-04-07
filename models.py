from sqlmodel import SQLModel, Field

информация = """\
Данные поступают из нескольких источников нформации:
    - aopa-points-export.csv (Аэродромы и вертодромы Европы и Азии)
    - data.csv (Населённые пункты России с количеством жителей) 
"""


class Аэродром(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    icao: str = Field(max_length=4)
    название: str | None = Field(default=None)
    город:  str | None = Field(default=None)



class Вертодром(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    icao: str = Field(max_length=4)
    название: str | None = Field(default=None)
    город:  str | None = Field(default=None)


