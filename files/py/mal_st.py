import streamlit as st
from функции import *
from классы import *
from перечни import *


if "радиус_зоны_ответственности" not in st.session_state:
    st.session_state["радиус_зоны_ответственности"] = 1000

if "радиус_зоны_агломерации" not in st.session_state:
    st.session_state["радиус_зоны_агломерации"] = 100

if "аэродром" not in st.session_state:
    st.session_state["аэродром"] = "UNWW | NOZ | Новокузнецк | Спиченково"

if "аэропорты" not in st.session_state:
    st.session_state["аэропорты"] = перечень_МАЛ

if "самолёты" not in st.session_state:
    st.session_state["самолёты"] = [_['тип'] for _ in перечень_самолёты]

if 'самолёты_проекта' not in st.session_state:
    st.session_state['самолёты_проекта'] = [
        "Ил-114-300",
        "ТВРС-44 Ладога",
        "ЛМС-192 Освей",
        "ЛМС-901 Байкал"
    ]

if 'опорные_аэродромы_ЮВК' not in st.session_state:
    st.session_state['самолёты_проекта'] = [
        "Ил-114-300",
        "ТВРС-44 Ладога",
        "ЛМС-192 Освей",
        "ЛМС-901 Байкал"
    ]


# st.session_state["аэродром"] = st.sidebar.selectbox("Аэродром",options=перечень_МАЛ)
# аэродром = st.session_state["аэродром"]


    
st.title("Общая информация о проекте МАЛ")
st.divider()

with st.sidebar.expander('Исходные данные'):
    st.session_state["Опорные аэродромы ЮВК"] = st.number_input(
        "Радиус агломерации, км",
        min_value=100, max_value=100,
        value=st.session_state["радиус_зоны_агломерации"],
        help="Значение определяет радиус круга с центром в контрольной точке аэродрома, который ограничивает количество населённых пунктов, население которых учитывается при подсчёте количества жителей, проживающих в районе аэропорта")
    
    st.session_state["радиус_зоны_ответственности"] = st.number_input(
        "Радиус доступности, км",
        min_value=1000, max_value=1000,
        value=int(st.session_state["радиус_зоны_ответственности"]))
    
    АвиаГСМ = st.number_input(
        "Стоимость ТС-1, руб. без НДС",
        Керосин_сегодня(аэропорт=st.session_state["аэродром"][:4]),
        help="Указывается расчётное значение стоимости авиационного керосина ТС-1 в рублях без НДС на пистолете топливозаправщика"
        )