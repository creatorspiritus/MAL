import streamlit as st

st.logo("files/ico/МАЛ_2.ico", link="https://мал.орг/ru", icon_image="files/ico/МАЛ.ico")
st.set_page_config(page_title="МАЛ", page_icon="files/ico/МАЛ_2.ico", layout="wide", initial_sidebar_state="auto", menu_items={'Get Help': 'https://мал.орг/ru', 'Report a bug': "https://мал.орг/ru", 'About': "###### МУНИЦИПАЛЬНЫЕ АВИАЛИНИИ"})

#аэродромы = st.Page("files/py/ИД/Аэродромы.py", title="Аэродромы проекта")

меню = st.navigation({
    "Аэродромы": [
        st.Page("files/py/Аэродромы/Узловые.py", title="Узловые аэропорты", icon=":material/connecting_airports:"),
        st.Page("files/py/Аэродромы/Назначения.py", title="Аэропорты назначения", icon=":material/flight_takeoff:"),
        st.Page("files/py/Аэродромы/Аэродромы ЮВК.py", title="Южный воздушный коридор", icon=":material/counter_1:"),
        st.Page("files/py/Аэродромы/Аэродромы СВК.py", title="Северный воздушный коридор", icon=":material/counter_2:"),
        st.Page("files/py/Аэродромы/Аэродромы ЦВК.py", title="Центральный воздушный коридор", icon=":material/counter_3:"), 
        st.Page("files/py/Аэродромы/Аэродромы Все.py", title="Полный перечень аэропортов", icon=":material/flights_and_hotels:"),
    ],
    "Маршруты": [
        st.Page("files/py/Маршруты/Маршруты ЮВК.py"),
        st.Page("files/py/Маршруты/Маршруты СВК.py"),
        st.Page("files/py/Маршруты/Маршруты ЦВК.py"),
        st.Page("files/py/Маршруты/Обязательные.py"),
        st.Page("files/py/Маршруты/Коммерческие.py"),
        st.Page("files/py/Маршруты/Транспортные.py"),
        st.Page("files/py/Маршруты/Маршруты Все.py"),
    ],
    "Самолёты": [
        st.Page("files/py/Самолёты/Ил-114-300.py"),
        st.Page("files/py/Самолёты/ТВРС-44 Ладога.py"),
        st.Page("files/py/Самолёты/ЛМС-192 Освей.py"),
        st.Page("files/py/Самолёты/ЛМС-901 Байкал.py"),
        st.Page("files/py/Самолёты/Самолёты Все.py"),
    ],
    "Настройки": [
        st.Page("files/py/Настройки/Валюты.py"),
        st.Page("files/py/Настройки/АвиаГСМ.py"),
        st.Page("files/py/Настройки/Агломерации.py"),
        st.Page("files/py/Настройки/Настройки Все.py"),
    ],
})

меню.run()