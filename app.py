import streamlit as st
import cv2
import numpy as np


camera_image = st.sidebar.camera_input("Take a Photo of the waste")
st.sidebar.markdown("<h3 style='text-align: center;'>Or </h3>", unsafe_allow_html=True)
upload_file = st.sidebar.file_uploader("Upload the photo of the Waste")

if camera_image is not None:
    image = cv2.imdecode(np.frombuffer(camera_image.read(), np.uint8), 1)
            
if upload_file is not None:
    image = cv2.imdecode(np.frombuffer(upload_file.read(), np.uint8), 1)
        
if camera_image is not None and upload_file is not None:
    st.subheader("Please upload an image")

def page1():
    st.title("Solid Waste Classfication")
    st.image("https://millerrecycling.com/wp-content/uploads/2020/10/organic-waste.jpg", width=None)
            
    if st.button("Next", key="next_page"):
        st.session_state.current_page = "Page 2"

def page2():
    st.image(image, use_column_width=True)
    if st.button("Back", key="prev_page"):
        st.session_state.current_page = "Page 1")


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
