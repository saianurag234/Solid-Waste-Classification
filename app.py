import streamlit as st
import cv2
import numpy as np

st.title("Solid Waste Classfication")
camera_image = st.sidebar.camera_input("Take a Photo of the waste")
st.sidebar.markdown("<h3 style='text-align: center;'>Or </h3>", unsafe_allow_html=True)
upload_file = st.sidebar.file_uploader("Upload the photo of the Waste")

button = st.button("Predict")
next = st.button("Next")

if button:
  if camera_image is not None:
    image = cv2.imdecode(np.frombuffer(camera_image.read(), np.uint8), 1)
    st.image(image, use_column_width=True)
  else:
    image = cv2.imdecode(np.frombuffer(upload_file.read(), np.uint8), 1)
    st.image(image, use_column_width=True)

st.session_state.page_select = st.button('Next')

if st.session_state.page_select == True:
    st.title('Page 1')

