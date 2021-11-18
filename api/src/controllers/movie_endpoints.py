from src.app import app
from src.utils.mongo_connection import movies_metadata
from flask import request
from src.utils.json_response import serialize
import json

@app.route("/movies")
@serialize
def movies():
    movie_data = json.dumps(list(movies_metadata.find({}, {"_id": 0, "homepage": 0, "belongs_to_collection": 0})))
    return movie_data

@app.route("/movies/search")
@serialize
def search_movies():
    pattern = request.args.get("name")
    pattern_format = f".*{pattern.lower()}.*"
    res = movies_metadata.find(
        {"original_title": {"$regex": pattern_format, "$options": "i"}}, 
        {"_id": 0, "homepage": 0, "belongs_to_collection": 0})
        
    return {f"{pattern}" : res}

@app.route("/movies/poster")
@serialize
def movies_poster_link():
    pattern = request.args.get("name")
    res = movies_metadata.find(
        {"original_title": pattern,}, 
        {"poster_path": 1, "_id": 0}
    )
    return ({f"{pattern}": res})

## https://image.tmdb.org/t/p/original{poster_path}