import streamlit as st

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')
st.header(':blue[Cool] :sunglasses:')

agree = st.checkbox("Who's ur daddy?")

if agree:
    st.write("Jerry!!")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
    st.write("Laugh out loud.")
elif genre == "***Drama***":
    st.write("Get the popcorn.")
elif genre == "Documentary :movie_camera:":
    st.write("Never stop learning.")

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")