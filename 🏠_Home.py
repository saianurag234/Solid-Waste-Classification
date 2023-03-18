import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.sidebar.image("data:image/jpeg;base64,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", width=None)

st.title("Solid Waste Classification")
want_to_contribute = st.button("Click Here to upload the Image")
if want_to_contribute:
    switch_page("Upload Image")
