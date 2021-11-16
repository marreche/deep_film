import streamlit as st
from model.content_based_recommendation import get_recommendations

def simple_recommender():
    st.title("Simple Recommender")
    movie_title = st.text_input("Movie Title")
    if movie_title:
        df = get_recommendations(movie_title)
        df.index += 1
        st.dataframe(df)
    