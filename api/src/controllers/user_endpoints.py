from src.app import app
from flask import request
from src.utils.mongo_connection import ratings_new
from src.utils.json_response import serialize

@app.route("/add",  methods = ["GET", 'POST'])
@serialize
def add():
    rating = request.args.get('rating')
    userId = ratings_new.find().distinct('userId')[-1] + 1
    ##movieId = 
    ratings_new.insert_one(
        {   "userId" : userId,
            ##"movieId" : movieId
            "rating": float(rating)
    })
    return {"state": "Rating successfully added!"}