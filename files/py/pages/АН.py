import streamlit as st
from pandas import read_csv
from перечни import перечень_АН
from функции import Агломерация, РПП, Керосин_сегодня, Парных, Пвс, Рлч, Vкр, Vт, tр, tрасп, ЧММ, Рлч, Таблица_аэродромов, Наименование, Базовый_УА, Базовый_УА_км, Расчётный_тип_ВС, Категория

аэропорт_назначения = st.sidebar.selectbox("Аэропорт назначения", перечень_АН, placeholder="Выберите аэропорт", )
радиус_население = 100
радиус_зоны_ответственности = 1000
st.header(f"Аэропорт назначения {аэропорт_назначения}", divider=True)
средняя_стоимость_керосина=Керосин_сегодня()
средняя_расчётная_загрузка_пасс=0.7 # 70% пассажирского салона
средняя_стоимость_авиабилета=3000 # в рублях

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

таблица_аэродромов = Таблица_аэродромов(аэродром=аэропорт_назначения[:4], радиус=радиус_зоны_ответственности)

таблица_наименований = []

for _ in таблица_аэродромов.index:
    таблица_наименований.append(Наименование(_))

with st.sidebar.expander("Маршрут"):
    ICAO_прилёт = st.selectbox("Расчётный аэропорт прибытия", таблица_наименований)
    # крейсерская_скорость = st.number_input("Крейсерская скорость, км/ч", value=Vкр(тип=str(тип_ВС)))
    # расход = st.number_input("Расход ТС-1, кг/лч", value=Рлч(тип=str(тип_ВС)))

col1, col2 = st.columns([2,1])

with col1:
    st.write('Базовый узловой аэропорт')
    st.write('Расстояние до узлового аэропорта, км')
    st.write('Расчётный годовой пассажиропоток, пасс')
    st.write('Расчётный суточный пассажиропоток, пасс')
    st.write('Расчётный тип воздушного судна')
    st.write('Крейсерская скорость, км/ч')
    st.write('Техническая скорость, км/ч')
    st.write('Расчётная продолжительность рейса, Ч:ММ')
    st.write('Продолжительность рейса в расписании, Ч:ММ')
    st.write('Часовой расход ТС-1, кг/лч')
    st.write('Потребное количество ТС-1 на полёт, кг')
    st.write('Стоимость ТС-1, руб/кг')
    st.write('Стоимость ТС-1 на полёт, руб')
    st.write('Расчётная cебестоимость рейса, руб')
    st.write('Расчётное количество пассажиров на рейс')
    st.write('Средняя стоимость авиабилета, руб')
    st.write('Средний валовый доход с рейса, руб')
    st.write('Баланс рейса, руб')
    st.write('Парных рейсов в сутки, не менее')
    st.write('Расчётная авиационная подвижность')


with col2:
    БУА = Базовый_УА(аэропорт_назначения[:4]) # Полное наименование
    БУАКМ = Базовый_УА_км(аэропорт_назначения[:4]) # Расстояние в км
    РГПП = РПП(аэропорт_назначения[:4]) # Расчётный годовой пассажиропоток
    РСПП = int(round(РГПП/365, 0)) # Расчётный суточный пассажиропоток
    РТВС = Расчётный_тип_ВС(рпп=РСПП, категория=Категория(аэропорт_назначения[:4]))
    техническая_скорость = Vт(тип=тип_ВС, расстояние=БУАКМ)
    продолжительность_рейса_расчётная = tр(тип=РТВС, расстояние=БУАКМ)
    РЛЧ = Рлч(РТВС)
    потребное_количество_керосина = int(round(РЛЧ*продолжительность_рейса_расчётная,0))
    стоимость_керосина_на_полёт = int(round(средняя_стоимость_керосина/1000*потребное_количество_керосина, 0))
    расчётная_себестоимость_рейса = int(round(стоимость_керосина_на_полёт*4))
    расчётное_количество_пассажиров_на_рейс = int(round(Пвс(РТВС)*средняя_расчётная_загрузка_пасс, 0))
    средний_валовый_доход=int(round(средняя_стоимость_авиабилета*расчётное_количество_пассажиров_на_рейс,0))
    баланс_рейса=int(round(средний_валовый_доход-расчётная_себестоимость_рейса,0))
    парных_рейсов=Парных(РСПП, расчётное_количество_пассажиров_на_рейс)
    расчётная_авиационная_подвижность = round((парных_рейсов*расчётное_количество_пассажиров_на_рейс*365)/агломерация_населения,2)
    st.write(БУА)
    st.write(str(БУАКМ))
    st.write(str(РГПП))
    st.write(str(РСПП))
    st.write(str(РТВС))
    st.write(str(крейсерская_скорость))
    st.write(str(техническая_скорость))
    st.write(ЧММ(продолжительность_рейса_расчётная))
    st.write(tрасп(ЧММ(продолжительность_рейса_расчётная)))
    st.write(str(РЛЧ))
    st.write(str(потребное_количество_керосина))
    st.write(str(int(round(средняя_стоимость_керосина/1000, 0))))
    st.write(str(стоимость_керосина_на_полёт))
    st.write(str(расчётная_себестоимость_рейса))
    st.write(str(расчётное_количество_пассажиров_на_рейс))
    st.write(str(средняя_стоимость_авиабилета))
    st.write(str(средний_валовый_доход))
    st.write(str(баланс_рейса))
    st.write(str(парных_рейсов))
    st.write(str(расчётная_авиационная_подвижность))




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

st.caption(f'Таблица 1 - Маршруты полётов из АН в зоне, радиусом {радиус_зоны_ответственности} км')

# anua = read_csv('../csv/АНУА.csv', index_col='АН')
st.write(таблица_аэродромов)

st.markdown("""Критерием выбора узлового аэропорта для аэропорта
            назначения является минимальное расстояние между КТА
            (контрольными точками аэродромов).
""")

