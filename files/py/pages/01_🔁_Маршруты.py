import streamlit as st
from pandas import read_csv, DataFrame
from функции import Наименование, наименования

st.title("Маршруты")
st.divider()
st.session_state.keys()
a = []
# for _ in st.session_state.keys():
#     if (len(_) == 4) and st.session_state[_]:
#         a.append(Наименование(_))    

# a = наименования()
# 
вылет = st.sidebar.selectbox("Вылет", a)
# 
# файл = '../csv/Аэродромы/' + вылет[:4] + '_1000_перечень_аэродромов.csv'
# d = read_csv(файл, index_col='ICAO')
# b = [Наименование(_) for _ in d.index]
# 
# 
# прилёт = st.sidebar.selectbox("Прилёт", b.remove(вылет))