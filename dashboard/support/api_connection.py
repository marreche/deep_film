import requests

url_main = "http://127.0.0.1:5000/"

def get_movies(movie_name):
    url = f"{url_main}/movies/search?name=" +  movie_name
    movies = requests.get(url).json()
    return movies

def insert_ratings(ratings, movieIds, userId):
    url = f"{url_main}/add?rating={ratings}&movieId={movieIds}&userId={userId}"
    requests.post(url).json()

def get_predictions():
    url = f"{url_main}/predictions"
    predictions = requests.get(url).json()
    return predictions
