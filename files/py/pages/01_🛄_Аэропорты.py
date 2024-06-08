import streamlit as st
from pandas import read_csv, DataFrame
from функции import Наименование, Агломерация, УА, АПН, АН

РЗА = st.session_state["радиус_зоны_агломерации"]
РЗО = st.session_state["радиус_зоны_ответственности"]

st.title("Аэропорты")
st.divider()

путь_имя = '../csv/Сводка.csv'
s = read_csv(путь_имя, index_col='ICAO')

st.write(s)

аэропорт = аэропорт = st.sidebar.selectbox(
    "Выберите аэропорт для получения подробной информации",
    st.session_state['аэропорты'])

st.subheader(
    'Информация по аэропорту ' + аэропорт)

агломерация = Агломерация(
    аэродром=аэропорт[:4], 
    радиус=st.session_state["радиус_зоны_агломерации"])


st.write(f"Агломерация населения в радиусе {РЗА} км от контрольной точки аэродрома составляет {агломерация} жителей.")

try:
    st.write("Города и населённые пункты в районе аэропорта, а также геодезические расстояния и количество жителей представлены в таблице 1")

    города = read_csv('../csv/Города/' + аэропорт[:4] + '_' + str(РЗА) + '_перечень_городов.csv')

    st.caption(f"Таблица 1 - Города в районе аэропорта {аэропорт}")
    st.write(города)
except:
    ...
finally:
    ...

подвижность = АПН(аэродром=аэропорт[:4])
st.write(f"Расчётный показатель авиационной подвижности населения для аэродрома {аэропорт} имеет значение {подвижность}.")

расчётный_пассажиропоток = int(агломерация * подвижность)
st.write(f"Расчётный годовой пассажиропоток для аэропорта {аэропорт} составляет {расчётный_пассажиропоток} пассажиров. Значение расчётного ежедневного пассажиропотока (для значения коэффициента авиационной подвижности населения данного аэропорта, равным {подвижность}) составляет {int(расчётный_пассажиропоток/365)} пассажиров в сутки.")

if АН(аэропорт[:4]):
    st.write(f"Аэропорт {аэропорт} в терминологии проекта МАЛ является аэропортом назначения.")
elif УА(аэропорт[:4]):
    st.write(f"Аэропорт {аэропорт[:4]} в терминологии проекта МАЛ является узловым аэропортом.")
else: st.write("Тип аэропорта не определён")

аэропорты = read_csv('../csv/Аэродромы/' + аэропорт[:4] + '_' + str(РЗО) + '_перечень_аэродромов.csv', index_col='ICAO')

st.write(f"Перечень аэропортов, расположенных в зоне полётной доступности из аэропорта {аэропорт} представлен в таблице 2")

st.caption(f"Таблица 2 - Аэропорты в зоне {аэропорт}")
st.write(аэропорты)

if АН(аэропорт[:4]):
    st.write(f"Для аэропорта {аэропорт}, поскольку он является аэропортом назначения, основным расчётным направлением ежедневных регулярных рейсов определяется ближайший узловой аэропорт. Расчёты других маршрутов регулярных рейсов производятся индивидуально для каждого направления с учётом рекомендаций руководителей муниципальных образований.")
elif УА(аэропорт[:4]):
    st.write(f"Пассажиропоток аэропорта {аэропорт} распределяется между соседними узловными аэропортами, себестоимость выполнения не менее двух ежедневных парных рейсов которых ниже расчётных поступлений денежных средств каждого направления.")
else: ...

