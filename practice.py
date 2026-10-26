import streamlit as st
import datetime

today = datetime.datetime.now()

with st.form(key="my_name_form"):
    user_name = st.text_input("이름")

    st.date_input("생일", min_value=datetime.date(1950, 1, 1), max_value=today)
    
    submitted = st.form_submit_button("제출")

if submitted:
    st.write(f"안녕하세요, {user_name}님!")
    

    