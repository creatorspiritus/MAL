import streamlit as st
from перечни import перечень_ЮВК

st.title("I Этап | Южный воздушный коридор")
st.divider()

if "ЮВКВ" not in st.session_state:
    st.session_state["ЮВКВ"] = st.session_state["ЮВК"]

st.session_state["ЮВКВ"] = st.multiselect(
    "Аэропорты южного воздушного коридора",
    default=st.session_state['ЮВК'],
    options=перечень_ЮВК)