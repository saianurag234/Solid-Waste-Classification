import streamlit as st

st.title("Solid Waste Classfication")
st.sidebar.camera_input("Take a Photo of the waste")

st.markdown(title_alignment, unsafe_allow_html=True)

st.sidebar.file_uploader("Upload the photo of the Waste")
st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)
