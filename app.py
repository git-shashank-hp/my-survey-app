import streamlit as st
from storage import save_response

st.title("Simple Survey App")

# Input fields
name = st.text_input("Enter your name:")
response = st.radio("Do you agree?", ("Yes", "No"))

# Submit button
if st.button("Submit"):
    if name.strip() == "":
        st.warning("Please enter your name.")
    else:
        save_response(name, response)
        st.success("Response submitted successfully!")
