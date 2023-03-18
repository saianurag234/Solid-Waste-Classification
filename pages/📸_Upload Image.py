import streamlit as st

st.markdown("Upload the Image")
upload_file = st.file_uploader(" ")
camera_input = st.camera_input("Take a photo")

if upload_file is not None:
  image = cv2.imdecode(np.frombuffer(upload_file.read(), np.uint8), 1)
elif camera_input is not None:
  image = cv2.imdecode(np.frombuffer(camera_input.read(), np.uint8), 1)
else:
  st.write("Please upload the image")
