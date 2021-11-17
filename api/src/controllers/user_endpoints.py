from src.app import app
from flask import request
from src.utils.mongo_connection import ratings_new, predictions
from src.utils.json_response import serialize
import numpy as np

@app.route("/add",  methods = ["GET", 'POST'])
@serialize
def add():
    rating = request.args.get('rating')
    userId = request.args.get('userId')
    if not userId:
        userId = np.random.randint(1, 100000)
    movieId = request.args.get('movieId')
    ratings_new.insert_one(
        {   "userId" : int(userId),
            "movieId" : int(movieId),
            "rating": float(rating)
    })
    return {"state": "Rating successfully added!"}

@app.route("/predictions",  methods = ["GET"])
@serialize
def get_predictions():
    res = list(predictions.find())
    return {"Predictions" : res}

