import streamlit as st

st.title("Solid Waste Classfication")
st.sidebar.camera_input("Take a Photo of the waste")
st.sidebar.subheader("Or")
st.sidebar.file_uploader("Upload the photo of the Waste")
