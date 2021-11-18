import pandas as pd
import numpy as np
from support_model.mongo_connection import ratings, ratings_new, movies_metadata
from ast import literal_eval


def extract_genres(x):
    x = literal_eval(x)
    if isinstance(x, list):
        genre_names = [i['name'] for i in x]
        if len(genre_names) > 3:
            genre_names= genre_names[:3]
        return genre_names
    return []


ratings_df = pd.DataFrame(list(ratings.find()))
ratings_df = ratings_df.drop(columns=['_id', 'timestamp'])

new_ratings_df = pd.DataFrame(list(ratings_new.find()))
new_ratings_df = new_ratings_df.drop(columns=['_id'])

df_user = ratings_df.append(new_ratings_df)
df_user = df_user.reset_index().drop(columns=['index'])

df_movies = pd.DataFrame(list(movies_metadata.find()))
literal_eval(df_movies['genres'].loc[0])
df_movies['genres']= df_movies['genres'].apply(extract_genres)
df_movies = df_movies.drop(columns=['adult', 'belongs_to_collection', 'budget', 'homepage',
       'imdb_id', 'original_language', 'original_title', 'overview',
       'popularity', 'poster_path', 'production_companies',
       'production_countries', 'release_date', 'revenue', 'runtime',
       'spoken_languages', 'status', 'tagline', 'video',
       'vote_average', 'vote_count'])
df_movies = df_movies.rename(columns={'id':'movieId'})
df_movies = df_movies[["movieId", "title", "genres"]]
df_movies['genres'] = ["".join(string) for string in df_movies['genres']]
df_movies.drop(df_movies.index[19730],inplace=True)
df_movies.drop(df_movies.index[29502],inplace=True)
df_movies.drop(df_movies.index[35585],inplace=True)
df_movies.movieId = df_movies.movieId.astype(np.int64)
