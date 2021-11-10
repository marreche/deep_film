from src.app import app

@app.route("/")
def home():
    return {
        "Welcome": "Movies API"
    }