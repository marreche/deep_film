from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("USER")
password = os.getenv("PASS")
url = f"mongodb+srv://{username}:{password}@datacluster.2umgq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.get_database("movies")
movies_metadata = db.movies_metadata
credits = db.credits
keywords = db.keywords
links = db.links_small
ratings = db.ratings_small