import streamlit as st
import pandas as pd
from support.movie_df_creation import movies_df
from support.api_connection import insert_ratings
from support.mongo_connection import predictions
from support.model_functions_streamlit import SVD_prediction
import numpy as np


def get_movies():
    movies = movies_df
    return movies

movies = get_movies()
movieId = []
rating_array = []
userId = 42


def recommender():
    title = st.title("Recommender")
    st.write("This movie recommendation system uses Singular Value Deomposition (SVD) to predict user ratings.")
    st.write("To calculate your tailored recommendations you must first rate these 20 movies down below.")
    st.write("Use the sliders below each movie poster to rate the movies. Once you're happy with your ratings, press the 'Get Recommendation' button at the bottom of the page. This will train the model with your ratings.")
    st.write("Once the training is complete, a table will be displayed with up to five movie recommendations")
    st.subheader("Enjoy!")
    st.header("Rate these movies:")
    for i in range(len(movies)):
        img = movies.iloc[i]['poster_path']
        movieId.append(movies.iloc[i]['movieId'])
        st.image(img)
        rating_array.append(st.slider("Rate Movie", min_value=0, max_value=5, key= f"rating {i}"))
        
        
    movieIds = movieId[:20]
    ratings = rating_array[-20:]
    if st.button("Get recommendation"):
        for i in range(len(movieIds)):
            insert_ratings(ratings[i], movieIds[i], userId=userId)
        SVD_prediction()
        preds_df = pd.DataFrame(list(predictions.find({'userId': userId}, {'_id': 0, 'movieId': 0, 'userId': 0})))
        preds_df = preds_df[['title', 'rating_prediction']]
        st.dataframe(preds_df)
