import streamlit as st
from перечни import перечень_самолёты
from функции import ТТХВС

st.title("Самолёты")
st.divider()

st.session_state['самолёты_проекта'] = st.multiselect(
    'Самолёты проекта', 
    st.session_state['самолёты'],
    default=[
        "Ил-114-300",
        "ТВРС-44 Ладога",
        "ЛМС-192 Освей",
        "ЛМС-901 Байкал"
    ])

самолёт = st.sidebar.selectbox(
    "Самолёт",
    options=st.session_state['самолёты'])

st.subheader(f"Технико-экономические характеристики самолёта {самолёт}")

col1, col2 = st.columns([3,1])

with col1:
    st.write("Количество пассажирских кресел")

with col2:
    st.write(ТТХВС(самолёт))