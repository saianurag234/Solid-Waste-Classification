import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Home Page")

if st.button("Next Page"):
  switch_page("About")
