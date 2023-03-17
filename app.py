import streamlit as st

def page1():
    st.title("Page 1")
    # Add content for page 1 here
    st.write("Welcome to Page 1!")
    if st.button("Next"):
        st.session_state.current_page = "Page 2"

def page2():
    st.title("Page 2")
    # Add content for page 2 here
    st.write("Welcome to Page 2!")
    if st.button("Next"):
        st.session_state.current_page = "Page 3"

def page3():
    st.title("Page 3")
    # Add content for page 3 here
    st.write("Welcome to Page 3!")
    if st.button("Next"):
        st.session_state.current_page = "Page 1"

# Create a dictionary of page names and their corresponding functions
pages = {
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3
}

# Set initial page to display
if "current_page" not in st.session_state:
    st.session_state.current_page = "Page 1"

# Call the selected page function
pages[st.session_state.current_page]()
