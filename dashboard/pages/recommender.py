import streamlit as st
import pandas as pd
from support.movie_df_creation import movies_df
from support.api_connection import insert_ratings
from support.model_functions_streamlit import svd_prediction
import numpy as np


def get_movies():
    '''
    Get sample of 20 movies from movie pool, to display images.
    '''
    movies = movies_df.sample(20)
    return movies


movies = get_movies()
movieId = []
rating_array = []
userId = np.random.randint(700, 10000)


def recommender():
    '''
    Recommender page in streamlit
    '''
    
    title = st.title("Recommender")
    st.write("This movie recommendation system uses Singular Value Deomposition (SVD) to predict user ratings.")
    st.write("To calculate your tailored recommendations you must first rate these 20 movies down below.")
    st.write("Use the sliders below each movie poster to rate the movies. Once you're happy with your ratings, press the 'Get Recommendation' button at the bottom of the page. This will train the model with your ratings.")
    st.write("Once the training is complete, a table will be displayed with your movie recommendations")
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
        st.write("Loading...")
        for i in range(len(movieIds)):
            insert_ratings(ratings[i], movieIds[i], userId=userId)
        st.write("Ratings added to database...")
        st.write("Calculating recommendations...")
        preds_df = svd_prediction()
        preds_df = preds_df[['title', 'rating_prediction']]
        preds_df.sort_values('rating_prediction', ascending=False, inplace=True)
        preds_df = preds_df.reset_index().drop(columns=['index'])
        preds_df.index += 1
        st.dataframe(preds_df)
