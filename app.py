import streamlit as st
from streamlit.hashing import _CodeHasher
from streamlit_extras import switch_page

st.title("Home Page")

if st.button("Next Page"):
  switch_page("About")
