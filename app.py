import streamlit
from streamlit_extras.switch_page_button import switch_page

want_to_contribute = st.button("About")
if want_to_contribute:
    switch_page("About")
