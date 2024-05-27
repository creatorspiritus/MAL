import streamlit as st
from pandas import read_csv, DataFrame
from функции import Наименование

st.title("Аэропорты")
st.divider()

путь_имя = '../csv/Сводка.csv'
s = read_csv(путь_имя, index_col='ICAO')

st.write(s)