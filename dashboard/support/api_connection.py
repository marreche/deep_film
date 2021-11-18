import requests

url_main = "http://127.0.0.1:5000/"

def get_movies():
    url = f"{url_main}/movies"
    movies = requests.get(url).json()
    return movies

def insert_ratings(ratings, movieIds, userId):
    url = f"{url_main}/add?rating={ratings}&movieId={movieIds}&userId={userId}"
    requests.post(url).json()

def get_predictions():
    url = f"{url_main}/predictions"
    predictions = requests.get(url).json()
    return predictions

def get_ratings():
    url = f"{url_main}/ratings"
    ratings = requests.get(url).json()
    return ratings

def get_new_ratings():
    url = f"{url_main}/ratings/new"
    new_ratings = requests.get(url).json()
    return new_ratings

