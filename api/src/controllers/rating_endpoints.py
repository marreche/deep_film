from src.app import app
from src.utils.mongo_connection import ratings, ratings_new
from flask import request
from src.utils.json_response import serialize
import json

@app.route("/ratings")
@serialize
def ratings_data():
    '''
    Returns all ratings stored in ratings collection.
    '''
    
    all_ratings = json.dumps(list(ratings.find({}, {'_id': 0})))
    return all_ratings

@app.route("/ratings/new")
@serialize
def ratings_new_data():
    '''
    Returns all new ratings introduced by the user's streamlit input
    '''
    
    all_ratings = json.dumps(list(ratings_new.find({}, {'_id':0})))
    return all_ratings