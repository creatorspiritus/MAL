import streamlit as st
from pandas import read_csv
from функции import Наименование

st.title("Аэропорты")
st.divider()

a = read_csv('../csv/Сводка.csv', index_col='ICAO')
названия = [Наименование(_) for _ in a.index]

# st.write(названия)

with st.sidebar.expander("Выберите действующие аэропорты"):
    st.checkbox(
        "UNWW | NOZ | Новокузнецк",
        value=True)
    st.checkbox(
        "UNNT | OVB | Новосибирск",
        value=True)