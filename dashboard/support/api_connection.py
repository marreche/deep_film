import requests

url_main = "https://deep-film-api.herokuapp.com"

def get_movies():
    '''
    Returns all movie data
    '''
    
    url = f"{url_main}/movies"
    movies = requests.get(url).json()
    return movies

def insert_ratings(ratings, movieIds, userId):
    '''
    Adds ratings to database
    '''
    
    url = f"{url_main}/add?rating={ratings}&movieId={movieIds}&userId={userId}"
    requests.post(url).json()

def get_predictions():
    '''
    Returns all user predictions
    '''
    
    url = f"{url_main}/predictions"
    predictions = requests.get(url).json()
    return predictions

def get_ratings():
    '''
    Returns all ratings data
    '''
    
    url = f"{url_main}/ratings"
    ratings = requests.get(url).json()
    return ratings

def get_new_ratings():
    '''
    Returns all new user ratings data
    '''
    
    url = f"{url_main}/ratings/new"
    new_ratings = requests.get(url).json()
    return new_ratings

