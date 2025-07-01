import streamlit as st
from storage import save_response

st.title("Simple Survey App")

name = st.text_input("Enter your name:")
response = st.radio("Do you like this app?", ("Yes", "No"))

if st.button("Submit"):
    if not name.strip():
        st.warning("Please enter your name.")
    else:
        save_response({"name": name, "answer": response})
        st.success("Response submitted successfully!")
