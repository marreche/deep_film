import sys
from numpy import add

sys.path.append("..")

import streamlit as st
from pages.home import home
from pages.recommender import recommender
from pages.docs import docs
from pages.top_fifty import fifty
from pages.simple_recommender import simple_recommender

st.set_page_config(
    page_title= "deep_film Recommender System",
    initial_sidebar_state= "collapsed"
)

add_selectbox = st.sidebar.radio(
    "Welcome to deep_film",
    ("Home", "Get a simple recommendation", "Get a recommendation","Top Fifty Rated Movies","Docs")
)

if add_selectbox == "Get a simple recommendation":
    simple_recommender()
elif add_selectbox == "Get a recommendation":
    recommender()
elif add_selectbox == "Top Fifty Rated Movies":
    fifty()
elif add_selectbox == "Docs":
    docs()
else:
    home()
