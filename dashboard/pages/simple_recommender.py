import streamlit as st
from support.content_based_recommendation import get_recommendations

def simple_recommender():
    st.title("Simple Recommender")
    st.write("This simple recommender works by recommending movies with similar movie descriptions. Although not the best recommender it shows that only by content similarity we can get some recommendations.")
    st.write("Introduce movie title in the text box below. (Caps sensitive)")
    movie_title = st.text_input("Movie Title")
    if movie_title:
        df = get_recommendations(movie_title)
        df.index += 1
        st.dataframe(df)
    