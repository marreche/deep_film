import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movies = pd.read_csv("/home/marrechea/deep_film/docs/data/movies_metadata.csv")
movies['overview'] = movies['overview'].fillna('')

tfidf = TfidfVectorizer(stop_words= 'english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
tfidf_matrix = tfidf_matrix[:23000]

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(index=movies['title'], data = movies.index).drop_duplicates()

def get_recommendations(title, cosine_sim= cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key= lambda x : x[1], reverse= True) 
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    df = pd.DataFrame(movies['title'][movie_indices]).reset_index().drop(columns=["index"])
    return df