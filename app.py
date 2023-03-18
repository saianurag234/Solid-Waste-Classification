import streamlit as st

# Define a dictionary of page names and their contents
pages = {
    "Page 1": "This is page 1",
    "Page 2": "This is page 2",
    "Page 3": "This is page 3"
}

# Create the Streamlit app
def main():
    st.title("Single Click Button Navigation")

    # Create a list of page names
    page_names = list(pages.keys())

    # Display a dropdown to select the current page
    current_page = st.selectbox("Select a page", page_names)

    # Display the contents of the current page
    st.write(pages[current_page])

    # Create buttons to navigate to the previous and next pages
    current_page_index = page_names.index(current_page)
    if current_page_index > 0:
        if st.button("Previous"):
            current_page = page_names[current_page_index - 1]
    if current_page_index < len(page_names) - 1:
        if st.button("Next"):
            current_page = page_names[current_page_index + 1]

if __name__ == "__main__":
    main()
