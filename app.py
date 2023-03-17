import streamlit as st
import cv2
import numpy as np


camera_image = st.sidebar.camera_input("Take a Photo of the waste")
st.sidebar.markdown("<h3 style='text-align: center;'>Or </h3>", unsafe_allow_html=True)
upload_file = st.sidebar.file_uploader("Upload the photo of the Waste")

def page1():
    st.title("Solid Waste Classfication")
    button = st.button("Predict")
    
    if button:
        if camera_image is not None:
            image = cv2.imdecode(np.frombuffer(camera_image.read(), np.uint8), 1)
            st.image(image, use_column_width=True)
        else:
            image = cv2.imdecode(np.frombuffer(upload_file.read(), np.uint8), 1)
            st.image(image, use_column_width=True)
            
    if st.button("Next"):
        st.session_state.current_page = "Page 2"

def page2():
    st.title("Page 2")
    # Add content for page 2 here
    st.write("Welcome to Page 2!")
    if st.button("Next"):
        st.session_state.current_page = "Page 1"


# Create a dictionary of page names and their corresponding functions
pages = {
    "Page 1": page1,
    "Page 2": page2
}

# Set initial page to display
if "current_page" not in st.session_state:
    st.session_state.current_page = "Page 1"

# Call the selected page function
pages[st.session_state.current_page]()
