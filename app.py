import streamlit as st

st.title("Solid Waste Classfication")
st.sidebar.camera_input("Take a Photo of the waste")
title_alignment=
"""
<style>
#the-title {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

st.sidebar.file_uploader("Upload the photo of the Waste")
