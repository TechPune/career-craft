from flask import Flask
from routes.user_routes import user_bp

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome to Career Craft API!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

app.register_blueprint(user_bp, url_prefix="/api")
