import streamlit as st

def docs():
    '''
    Docs streamlit page with useful links
    '''
    
    st.title("Documentation")
    st.header("Github")
    st.markdown(" - [Deep_film](https://github.com/marreche/deep_film)",unsafe_allow_html=True)
    st.header("API")
    st.markdown(" - [API](https://deep-film-api.herokuapp.com/)", unsafe_allow_html=True)
