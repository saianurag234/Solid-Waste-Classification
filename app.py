import streamlit as st

# Define a list of pages
pages = ["Page 1", "Page 2", "Page 3"]
page_index = 0

# Define a function to handle the "Next" button click
def next_page():
    global page_index
    page_index += 1
    if page_index >= len(pages):
        page_index = 0
    return pages[page_index]

# Create a Streamlit app
def main():
    st.title("Next Button Navigation")
    page = next_page()
    st.write(f"You are on {page}")
    st.button("Next", on_click=next_page)

if __name__ == "__main__":
    main()
