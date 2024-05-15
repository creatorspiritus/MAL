import streamlit as st
from pandas import read_csv
from перечни import перечень_АН
from функции import Агломерация, РПП, Vкр, Рлч

аэропорт_назначения = st.sidebar.selectbox("Аэропорт назначения", перечень_АН, placeholder="Выберите аэропорт", )
радиус_население = 100
st.header(f"Аэропорт назначения {аэропорт_назначения}", divider=True)

with st.sidebar.expander("Пассажиропоток"):
    агломерация_населения = st.number_input("Агломерация населения", value=Агломерация(аэропорт_назначения[:4]))
    РПП_годовой = st.number_input("Расчётный годовой пассажиропоток", value=int(РПП(аэропорт_назначения[:4])))
    РПП_ежедневный = st.number_input("Расчётный ежедневный пассажиропоток", value=int(РПП_годовой/365))
    
    if РПП_ежедневный > 130: индекс = 0
    else: индекс = 2
    
with st.sidebar.expander("Самолёт"):
    тип_ВС = st.selectbox("Расчётный тип ВС", 
        ["Ил-114-300", "ТВРС-44", "ЛМС-901"], index=индекс)
    крейсерская_скорость = st.number_input("Крейсерская скорость, км/ч", value=Vкр(тип=str(тип_ВС)))
    расход = st.number_input("Расход ТС-1, кг/лч", value=Рлч(тип=str(тип_ВС)))

with st.sidebar.expander("Маршрут"):
    ICAO_прилёт = st.selectbox("Расчётный аэропорт прибытия", ["UNWW", "UNNT"])
    # крейсерская_скорость = st.number_input("Крейсерская скорость, км/ч", value=Vкр(тип=str(тип_ВС)))
    # расход = st.number_input("Расход ТС-1, кг/лч", value=Рлч(тип=str(тип_ВС)))

st.markdown("""\
Аэропортами назначения (далее АН) в терминологии проекта развития региональных
воздушных перевозок с применением самолётов российского производства
называются 107 аэродромов (аэропортов), представленные в Транспортной
стратегии Российской Федерации (Распоряжение Правительства Российской
Федерации № 3363-р от 27 ноября 2021 года приложение № 7) которые 
необходимы для обеспечения транспортной доступности и расположены
в удалённых и труднодоступных районах Российской Федерации.

Для АН выбраны ближайшие по расстоянию между контрольными 
точками аэродромов узловые аэропорты (далее УА) с целью определения основного 
социального (субсидируемого) маршрута для каждого АН.
            
По формуле:""")

st.latex("П_{расч} = А_{" + str(радиус_население) + "} \cdot Р_{АПН}")

st.markdown("""\
, где

- $П_{расч}$ - расчётный годовой пассажиропоток, чел.
- $А_{100}$ - агломерация населения в радиусе 100 км от аэропорта, чел.
- $Р_{АПН}$ - расчётная авиационная подвижность населения.
            
Сведения о расчётных пассажиропотоках из аэропортов назначения
в направлении главного расчётного узлового аэропорта представлены
в таблице 1. """)

st.caption('Таблица 1 - Маршруты полётов из АН в гланвый расчётный УА')

anua = read_csv('../csv/АНУА.csv', index_col='АН')
st.write(anua)

st.markdown("""\
Критерием выбора узлового аэропорта для аэропорта назначения является
""")

