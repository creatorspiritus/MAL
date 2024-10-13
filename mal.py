import streamlit as st

пусто = lambda x: " | " if x else ""

if "icao" not in st.session_state: st.session_state.icao = "UNWW"
if "iata" not in st.session_state: st.session_state.iata = "NOZ"
if "город" not in st.session_state: st.session_state.город = "Новокузнецк"
if "аэродром" not in st.session_state: st.session_state.аэродром = "Спиченково"



МАЛ = st.navigation({
    "Исходные данные": [
        st.Page("files/py/ИД/Аэропорты.py", icon=":material/flight:"),
        st.Page("files/py/ИД/Самолёты.py", icon=":material/flight:")
    ]
})

МАЛ.run()