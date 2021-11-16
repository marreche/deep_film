import pandas as pd
import numpy as np

def get_top_50_movies():
    metadata = pd.read_csv("../data/movies_metadata.csv")
    C = metadata['vote_average'].mean()
    m = metadata['vote_count'].quantile(0.90)
    q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
    print(m, C)
    q_movies['weighted score'] = q_movies.apply(lambda x: weighted_rating(x, m, C), axis= 1)
    q_movies.sort_values(by= 'weighted score', ascending= False, inplace= True)
    top_score_movies = q_movies[['title', 'vote_count', 'vote_average', 'weighted score']].head(50).reset_index().drop(columns=["index"])
    top_score_movies.index += 1
    return top_score_movies

def weighted_rating(x, m, C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)