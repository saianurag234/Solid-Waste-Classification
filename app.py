import streamlit as st

# Define a list of pages
pages = ["Page 1", "Page 2", "Page 3"]
current_page_index = 0

# Define a function to handle the "Next" button click
def next_page():
    global current_page_index
    current_page_index = (current_page_index + 1) % len(pages)

# Create the Streamlit app
def main():
    st.title("Next Button Navigation")

    # Display the current page
    st.write(f"You are on {pages[current_page_index]}")

    # Add a "Next" button to navigate to the next page
    if st.button("Next"):
        next_page()

if __name__ == "__main__":
    main()
