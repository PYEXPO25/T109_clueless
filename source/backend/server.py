from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend-backend communication
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Initialize the database


@app.route('/')
def home():
    return "Welcome to Moview Backend!"


@app.route('/movies', methods=['GET'])
def get_movies():
    # Example static data; replace with database queries later
    movies = [
        {"id": 1, "title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
        {"id": 2, "title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    ]
    return jsonify(movies)

@app.route('/review', methods=['POST'])
def add_review():
    # Parse JSON data from the incoming request
    data = request.json  # Ensure request contains JSON data
    review_text = data.get('review_text', '')  # Extract review_text

    # Example sentiment analysis
    if not review_text:
        return jsonify({"error": "Review text is missing"}), 400  # Return error if review_text is empty

    sentiment = "Positive" if "good" in review_text.lower() else "Negative"

    return jsonify({
        "message": "Review added",
        "sentiment": sentiment
    })

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def recommendations(user_id):
    # Example recommendations; replace with real logic later
    recommended_movies = [
        {"id": 3, "title": "Interstellar", "rating": 8.6},
        {"id": 4, "title": "The Prestige", "rating": 8.5},
    ]
    return jsonify(recommended_movies)


if __name__ == '__main__':
    app.run(debug=True)


