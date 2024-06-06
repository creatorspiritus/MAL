import streamlit as st
from перечни import перечень_ЦВК

st.title("III Этап | Центральный воздушный коридор")
st.divider()

if "ЦВКВ" not in st.session_state:
    st.session_state["ЦВКВ"] = st.session_state["ЦВК"]

st.session_state["ЦВКВ"] = st.multiselect(
    "Аэропорты центрального воздушного коридора",
    default=st.session_state['ЦВК'],
    options=перечень_ЦВК)