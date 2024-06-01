import streamlit as st
import json
from функции import Наименование, Получить_таблицу, Vт, tр, Рлч, Керосин_сегодня, ЧММ
from pandas import read_csv, DataFrame
from datetime import time

st.title("Маршруты")
st.divider()

m = read_csv('../csv/Маршруты/Маршруты.csv', index_col=['ICAO аэродром вылета', 'ICAO аэродром прибытия'])

st.write(m)

самолёт = st.sidebar.selectbox('Тип ВС',
    ["Ил-114-300", "ТВРС-44 Ладога", "ЛМС-192 Освей", "ЛМС-901 Байкал"])

вылет = st.sidebar.selectbox('Аэропорт вылета',
    st.session_state["аэропорты"], index=99)

прилёт = st.sidebar.selectbox('Аэропорт прибытия',
    st.session_state["аэропорты"], index=100)

try:
    дистанция = m.loc[вылет[:4], прилёт[:4]]['Дистанция, км']
except:
    дистанция = "Маршрут не является расчётным маршурутом проекта МАЛ"
# finally: ...

try:
    st.subheader("Расчёт показателей рейса")
    дистанция = int(дистанция)
    дистанция = st.sidebar.number_input(
        "Расстояние по воздушным трассам, км",
        value=дистанция, min_value=10, max_value=2000)
    техническая_скорость = Vт(тип=самолёт, расстояние=дистанция)
    техническая_скорость = st.sidebar.number_input(
        "Техническая скорость, км/ч", техническая_скорость)
    продолжительность_рейса = tр(тип=самолёт, расстояние=дистанция)
    st.write(продолжительность_рейса)
    st.sidebar.time_input(
        "Продолжительность рейса, Ч:ММ",
        value=time(int(ЧММ(продолжительность_рейса)[0]),int(ЧММ(продолжительность_рейса)[2:])),
        disabled=True)
    расход_керосина = Рлч(тип=самолёт)
    st.write(расход_керосина)
    стоимость_керосина = Керосин_сегодня()
    st.write(стоимость_керосина)
    
except: st.write(f"Расчёты показателей регулярного рейса для самолёта {самолёт} из аэропорта {вылет} в аэропорт {прилёт} не производятся, поскольку маршрут не является расчётным для проекта МАЛ.")
# finally: ...

if 'самолёты' not in st.session_state:
    with open('../json/Самолёты.json', 'r', encoding='utf8') as f:
        st.session_state['самолёты'] = json.load(f)['Самолёты']

col1, col2 = st.columns([5,1])
with col1: st.write("Расчётный тип воздушного судна")
with col2: st.write(самолёт)

try:
    col1, col2 = st.columns([5,1])
    with col1: st.write("Максимальная взлётная масса, т")
    with col2: st.write(str(st.session_state["самолёты"][самолёт]["Максимальная взлётная масса, т"]))
except: ...
finally: ...

try:
    col1, col2 = st.columns([5,1])
    with col1: st.write("Масса снаряжённого, т")
    with col2: st.write(str(st.session_state["самолёты"][самолёт]["Масса снаряжённого, т"]))
except: ...
finally: ...