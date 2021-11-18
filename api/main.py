from os import getenv
from src.controllers.general_endpoints import app
from src.controllers.movie_endpoints import app
from src.controllers.user_endpoints import app
from src.controllers.rating_endpoints import app
import os

app.run("0.0.0.0", os.getenv("PORT"), debug=True)