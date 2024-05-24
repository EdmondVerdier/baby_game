import streamlit as st

from src.constants import MATCH_PHOTOS
from src.utils.pop_sicariot import pop_sicariot

if "score" not in st.session_state:
    st.session_state.score = 0

if "sicariot" not in st.session_state:
    st.session_state.sicariot = pop_sicariot()

st.sidebar.title("Noms possibles")
for item in MATCH_PHOTOS:
    st.sidebar.write(item["name"])

container = st.empty()

def update_image() -> None:
    with container:
        st.image(st.session_state.sicariot["photo"], width=400)

update_image()

baby_name = st.text_input("Who is it ?")

if st.button("Submit"):
    if baby_name == st.session_state.sicariot["name"]:
        st.write(f"Good job ! 🎉")
        st.session_state.score += 1
        st.session_state.sicariot = pop_sicariot()
        update_image()
    else:
        st.write(f"Try again ! ❌")
        st.session_state.score = 0

st.write(f"Score actuel : {st.session_state.score}")
