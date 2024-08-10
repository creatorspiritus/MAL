import streamlit as st

st.logo("files/ico/МАЛ_2.ico", link="https://мал.орг/ru", icon_image="files/ico/МАЛ.ico")

st.set_page_config(
    page_title="МАЛ",
    page_icon="files/ico/МАЛ_2.ico",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://мал.орг/ru',
        'Report a bug': "https://мал.орг/ru",
        'About': "###### МУНИЦИПАЛЬНЫЕ АВИАЛИНИИ"
    }
)