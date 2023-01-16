import streamlit as st

import time

# @st.cache(suppress_st_warning=True)
def show_preloading():
    with st.spinner("Loading..."):
        # add a delay to simulate loading time
        # st.image("your_logo.png",width=200)
        time.sleep(1)
    # st.success("Your logo is loaded")
