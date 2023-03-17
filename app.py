import streamlit as st

st.title("Solid Waste Classfication")
st.sidebar.camera_input("Take a Photo of the waste")

st.sidebar.file_uploader("Upload the photo of the Waste")
st.sidebar.markdown("<h3 style='text-align: center;'>Or </h3>", unsafe_allow_html=True)
