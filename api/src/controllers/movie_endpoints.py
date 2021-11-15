from src.app import app
from src.utils.mongo_connection import movies_metadata
from flask import request
from src.utils.json_response import serialize


@app.route("/movies")
@serialize
def movies():
    all_movies = list(movies_metadata.find({}))
    return {"all_movies" : all_movies}

@app.route("/movies/search")
@serialize
def search_movies():
    pattern = request.args.get("name")
    pattern = f".*{pattern.lower()}.*"
    res = movies_metadata.find(
        {"original_title": {"$regex": pattern, "$options": "i"}}, 
        {"original_title": 1, "_id": 0, "release_date": 1})
        
    return ({"Results": res})

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