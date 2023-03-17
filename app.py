import streamlit as st 
st.session_state.page_select = st.sidebar.radio('Pages', ['Page 1', 'Page 2', 'Page 3'])

if st.session_state.page_select == 'Page 1':
    st.title('Page 1')
    next = st.button('Go to page 2')
    if next:
        st.session_state.page_select = 'Page 2'

if st.session_state.page_select == 'Page 2':
    st.title('Page 2')
    next2 = st.button('Go to page 3')
    if next2:
        st.session_state.page_select = 'Page 3'  


if st.session_state.page_select == 'Page 3':
    st.title('Page 3')
