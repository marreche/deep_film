from src.app import app
from flask import request
from src.utils.mongo_connection import ratings_new
from src.utils.json_response import serialize

@app.route("/add",  methods = ["GET", 'POST'])
@serialize
def add():
    rating = request.form.get('rating')
    ratings_new.insert_one(
        {   "userId" : 1,
            "rating": rating
    })
    return {"state": "Rating successfully added!"}