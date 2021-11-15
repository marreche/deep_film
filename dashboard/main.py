import streamlit as st
from pages.home import home
from pages.recommender import recommender
from pages.docs import docs

st.set_page_config(
    page_title= "deep_film Recommender System",
    initial_sidebar_state= "collapsed"
)

add_selectbox = st.sidebar.radio(
    "Welcome to deep_film",
    ("Home", "Get a recommendation", "Docs")
)

if add_selectbox == "Get a recommendation":
    recommender()
elif add_selectbox == "Docs":
    docs()
else:
    home()
