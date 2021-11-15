import streamlit as st
from support.api_connection import get_movies

def recommender():
    st.title("Recommender")
    movies = st.text_input("Movie title")
    st.json(get_movies(movies))