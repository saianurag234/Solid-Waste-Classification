import streamlit as st

st.subheader("Upload the Image")
upload_file = st.file_uploader(" ")

st.markdown("<h2 style='text-align: center;;'>Or</h2>", unsafe_allow_html=True)

st.subheader("Take a photo")
camera_input = st.camera_input(" ")

if upload_file is not None:
  image = cv2.imdecode(np.frombuffer(upload_file.read(), np.uint8), 1)
elif camera_input is not None:
  image = cv2.imdecode(np.frombuffer(camera_input.read(), np.uint8), 1)
else:
  st.write("Please upload the image")
