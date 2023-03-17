import streamlit as st
# page1.py
import foo
foo.hello = 123

# page2.py
import foo
st.write(foo.hello)  # If page1 already executed, this should write 123

# page1.py

if "shared" not in st.session_state:
   st.session_state["shared"] = True

# page2.py
import streamlit as st
st.write(st.session_state["shared"])
# If page1 already executed, this should write True
