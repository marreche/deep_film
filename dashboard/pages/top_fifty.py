import streamlit as st
from model.top_fifty_rated_movies import get_top_50_movies


def fifty():
    st.header("Top 50 rated movies")
    st.write("This leaderboard was created using the weighted rating formula used by IMDB. The formula is as follows:")
    st.latex(r''' W = \frac{R * v + C * m}{v + m}''')
    st.write("Where:")
    st.write("- W = weighted rating")
    st.write("- R = average rating for the movie from 1 to 10 (mean)")
    st.write(" - v = number of votes for the movie")
    st.write(" - m = minimum number of votes required to be listed in the top 250")
    st.write(" - C = the mean vote across the whole vote")
    st.subheader("Leaderboard")
    
    df = get_top_50_movies()
    st.dataframe(df)