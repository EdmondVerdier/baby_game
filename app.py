import streamlit as st

st.image()

baby_name = st.text_input("Who is it ?")

if st.button("Submit"):
    st.write(f"Well played !")
