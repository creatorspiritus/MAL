import streamlit as st
from функции import Наименование, Получить_таблицу
from pandas import read_csv, DataFrame

st.title("Маршруты")
st.divider()

m = read_csv('../csv/Маршруты/Маршруты.csv', index_col=['ICAO аэродром вылета', 'ICAO аэродром прибытия'])

st.write(m)