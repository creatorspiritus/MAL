import streamlit as st
from перечни import перечень_самолёты
from функции import ТТХВС

st.title("Самолёты")
st.divider()



самолёт = st.sidebar.selectbox(
    "Самолёт",
    options=st.session_state['самолёты'])

ттх = ТТХВС(самолёт)


st.subheader(f"Технико-экономические характеристики самолёта {самолёт}")

col1, col2 = st.columns([5,1])
with col1: st.write("Количество пассажирских кресел")
with col2: st.write(str(ттх['Пассажиров, чел']))

col1, col2 = st.columns([5,1])
with col1: st.write("Крейсерская скорость, км/ч")
with col2: st.write(str(ттх['Крейсерская скорость, км/ч']))

col1, col2 = st.columns([5,1])
with col1: st.write("Расход авиакеросина, кг/лч")
with col2: st.write(str(ттх['Расход ТС-1, кг/лётный час']))

st.write(ттх)

#st.sidebar.write(st.session_state['самолёты_проекта'])
st.sidebar.write(самолёты_проекта)