import requests
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("USER")
password = os.getenv("PASS")
url = f"mongodb+srv://{username}:{password}@datacluster.2umgq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client["movies"]
ratings = db.ratings_small
ratings_new = db.ratings_new
movies_metadata = db.movies_metadata
predictions = db.predictions