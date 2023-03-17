import streamlit as st

st.title("Solid Waste Classfication")
st.sidebar.camera_input("Take a Photo of the waste")

st.markdown(title_alignment, unsafe_allow_html=True)

st.sidebar.file_uploader("Upload the photo of the Waste")
st.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True)
