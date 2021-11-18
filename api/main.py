from src.controllers.general_endpoints import app
from src.controllers.movie_endpoints import app
from src.controllers.user_endpoints import app
from src.controllers.rating_endpoints import app

app.run(debug=True)