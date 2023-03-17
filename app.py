import streamlit as st

def main():
    # Set page title
    st.set_page_config(page_title="Image Predictor")

    # Set page heading
    st.header("Image Predictor")

    # Show image
    image = st.file_uploader("Upload an image")
    if image is not None:
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # Add "Predict" button
    if st.button("Predict"):
        # Navigate to new page
        st.experimental_rerun()

if __name__ == '__main__':
    main()
