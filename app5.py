import streamlit as st

st.set_page_config(page_title="Propose Day 💖")

st.title("💖 Happy Propose Day 💖")

st.write("A special message for you ❤️")

# Fixed Name
name = "My Dopamine"

message = st.selectbox(
    "Choose Message",
    [
        "Thank you for choosing me motu💫",
        "I love you forever🌸",
        "Will you be mine forever...??"
    ]
)

if st.button("Send Wish"):
    st.success(f"{name}, {message}")