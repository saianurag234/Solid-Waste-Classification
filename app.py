import streamlit as st
from SessionState import get_state

# Define the SessionState function
def set_session_state():
    session = get_state()
    if not hasattr(session, 'page'):
        session.page = 1
    return session

# Initialize the session state
session = set_session_state()

# Create a function to handle the next button click
def next_button():
    session.page += 1

# Define the pages
page1 = """
        ## Page 1
        This is the first page.
        """

page2 = """
        ## Page 2
        This is the second page.
        """

# Create the Streamlit app
if session.page == 1:
    st.markdown(page1)
else:
    st.markdown(page2)

if st.button('Next'):
    next_button()
