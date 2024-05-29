import random

import streamlit as st

from src.constants import MATCH_PHOTOS

if "score" not in st.session_state:
    st.session_state.score = 0

if "shown_sicariots" not in st.session_state:
    st.session_state.shown_sicariots = []

def pop_sicariot() -> dict[str, str]:
    """Pop a sicariot from the list of photos."""
    remaining_photos = [sicariot for sicariot in MATCH_PHOTOS if sicariot not in st.session_state.shown_sicariots]
    if not remaining_photos:
        st.write("Fin de la partie ! Tu as tout trouvé ! 🎉")
    sicariot = random.choice(remaining_photos)
    st.session_state.shown_sicariots.append(sicariot)
    return sicariot

if "sicariot" not in st.session_state:
    st.session_state.sicariot = pop_sicariot()

st.title("Qui est ce bébé ? 👶🍼")


st.sidebar.image("data/logo/Arrakiff.png")
st.sidebar.title("Noms possibles")
for item in MATCH_PHOTOS:
    st.sidebar.write(item["name"])

container = st.empty()

def update_image() -> None:
    with container:
        st.image(st.session_state.sicariot["photo"], width=400)

def qualify_score() -> str:
    if st.session_state.score < 5:
        return "Haha c'est pas encore ça ! 😂"
    elif st.session_state.score <10 :
        return "Hey pas mal, ça commence à prendre forme ! 😏"
    elif st.session_state.score <20 :
        return "Ouuuh ! Tu es on fire ! 🔥"
    elif st.session_state.score <30 :
        return "Comment tu fais pour tout trouver ?? 😳"
    elif st.session_state.score <40 :
        return "Appelez tout le monde, on a un génie ici ! 🤯"
    elif st.session_state.score <50 :
        return "Tu mériterais un titre pour cette performance ! 🏆"
    elif st.session_state.score >=50 :
        return "On m'indique tu viens de recevoir un titre pour cette performance. \n Tu es officiellement The Baby God ! 🤩👶"
    else :
        return ""

def end_game() -> None:
    with container:
        st.markdown(
            f"""
            Ton score : {st.session_state.score}\n

            **{qualify_score()}**

            *Actualise la page pour relancer une partie 😉*
"""
        )

update_image()

baby_name = st.text_input("Who is it ?")

if baby_name:
    if baby_name == st.session_state.sicariot["name"]:
        st.write(f"Good job ! 🎉")
        st.session_state.score += 1
        st.write(f"Score actuel : {st.session_state.score}")
        st.session_state.sicariot = pop_sicariot()
        update_image()
    else:
        end_game()
        st.session_state.shown_sicariots = []
        st.session_state.score = 0


