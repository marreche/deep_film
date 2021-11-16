import streamlit as st
from support.movie_df_creation import movies_df
from support.api_connection import insert_ratings
import numpy as np


def get_five_random_movies():
    five = movies_df.sample(5)
    return five

movies = get_five_random_movies()
movieId = []
rating_array = []
userId = np.random.randint(1, 1000)


def recommender():
    title = st.title("Recommender")
    for i in range(len(movies)):
        img = movies.iloc[i]['poster_path']
        movieId.append(movies.iloc[i]['movieId'])
        st.image(img)
        rating_array.append(st.slider("Rate Movie", min_value=0, max_value=5, key= f"rating {i}"))
        
        
    movieIds = movieId[:5]
    ratings = rating_array[-5:]
    if st.button("Get recommendation"):
        for i in range(len(movieIds)):
            insert_ratings(ratings[i], movieIds[i], userId=userId)
    