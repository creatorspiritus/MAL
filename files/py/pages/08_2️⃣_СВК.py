import streamlit as st
from перечни import перечень_СВК

st.title("II Этап | Северный воздушный коридор")
st.divider()

if "СВКВ" not in st.session_state:
    st.session_state["СВКВ"] = st.session_state["СВК"]

st.session_state["СВКВ"] = st.multiselect(
    "Аэропорты северного воздушного коридора",
    default=st.session_state['СВК'],
    options=перечень_СВК)