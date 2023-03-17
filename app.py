import streamlit as st

st.title("Solid Waste Classfication")
st.sidebar.markdown("<h3 style='text-align: center;'>Take a Photo of the waste </h3>", unsafe_allow_html=True)
st.sidebar.camera_input("")
st.sidebar.markdown("<h3 style='text-align: center;'>Or </h3>", unsafe_allow_html=True)
st.sidebar.file_uploader("Upload the photo of the Waste")
