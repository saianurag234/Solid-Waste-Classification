import streamlit as st
from PIL import Image

# Define function to display uploaded image
def display_image(image):
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Define function to handle image upload and navigation to new page
def handle_image_upload():
    # Display instructions for uploading image
    st.write('Please upload an image:')
    
    # Allow user to upload image
    uploaded_image = st.file_uploader('', type=['png', 'jpg', 'jpeg'])
    
    # If user has uploaded an image
    if uploaded_image is not None:
        # Display the uploaded image on the current page
        display_image(uploaded_image)
        
        # Navigate to new page to display the uploaded image
        st.write('Navigating to new page...')
        st.experimental_rerun()
        st.write('Uploaded image:')
        display_image(uploaded_image)
    
# Define main function to run the app
def main():
    # Set page title and icon
    st.set_page_config(page_title='Image Upload', page_icon=':camera:')
    
    # Define page layout
    st.title('Image Upload')
    st.write('Upload an image and click the "Predict" button to navigate to a new page and display the uploaded image.')
    
    # Display image upload form
    handle_image_upload()

# Run the app
if __name__ == '__main__':
    main()
