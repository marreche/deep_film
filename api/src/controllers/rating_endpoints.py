from src.app import app
from support.mongo_connection import ratings, ratings_new
from flask import request
from src.utils.json_response import serialize
import json

@app.route("/ratings")
@serialize
def ratings_data():
    all_ratings = json.dumps(list(ratings.find({}, {'_id': 0})))
    return all_ratings

@app.route("/ratings/new")
@serialize
def ratings_new_data():
    all_ratings = json.dumps(list(ratings_new.find({}, {'_id':0})))
    return all_ratings