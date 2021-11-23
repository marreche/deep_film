from src.app import app

@app.route("/")
def home():
    '''
    Main API page
    '''
    
    return {
        "Welcome": "Movies API"
    }