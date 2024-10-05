import streamlit as st

МАЛ = st.navigation({
    "Исходные данные": [
        st.Page("files/py/ИД/Аэропорты.py")
    ]
})

МАЛ.run()