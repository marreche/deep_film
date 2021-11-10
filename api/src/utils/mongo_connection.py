from pymongo import MongoClient

client = MongoClient()
db = client.get_database("movies")
movie_metadata = db.movie_metadata
credits = db.credits
keywords = db.keywords
links = db.links_small
ratings = db.ratings_small