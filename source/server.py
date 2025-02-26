import os
import requests
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

# Initialize Flask App
app = Flask(__name__)
CORS(app)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/movie')
def movie_page():
    return render_template("movie.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/watchlist')
def watchlist():
    return render_template("watchlist.html")

# Fetch Movies from TMDb API
def fetch_from_tmdb(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    response = requests.get(url)
    data = response.json()

    if data["results"]:
        movie = data["results"][0]
        return {
            "title": movie["title"],
            "year": movie.get("release_date", "N/A").split("-")[0],
            "rating": movie.get("vote_average", "N/A"),
            "poster": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if "poster_path" in movie else None
        }
    return None

# Fetch Ratings from OMDb API (Includes IMDb & Rotten Tomatoes)
def fetch_from_omdb(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "Ratings" in data:
        ratings = {rating["Source"]: rating["Value"] for rating in data["Ratings"]}
        return {
            "title": data["Title"],
            "year": data["Year"],
            "imdb_rating": ratings.get("Internet Movie Database", "N/A"),
            "rotten_tomatoes": ratings.get("Rotten Tomatoes", "N/A"),
            "metacritic": ratings.get("Metacritic", "N/A")
        }
    return None

# Fetch Movie Data from APIs & Return Merged Response
@app.route('/movies/<title>', methods=['GET'])
def get_movie_data(title):
    tmdb_data = fetch_from_tmdb(title)
    omdb_data = fetch_from_omdb(title)

    if tmdb_data and omdb_data:
        return jsonify({
            "title": tmdb_data["title"],
            "year": tmdb_data["year"],
            "rating": tmdb_data["rating"],
            "poster_url": tmdb_data["poster"],
            "imdb_rating": omdb_data["imdb_rating"],
            "rotten_tomatoes": omdb_data["rotten_tomatoes"],
            "metacritic": omdb_data["metacritic"]
        }), 200

    return jsonify({"error": "Movie not found"}), 404

# Fetch a List of Movies (Static Example)
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = [
        {"id": 1, "title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
        {"id": 2, "title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    ]
    return jsonify(movies)

# Sentiment Analysis for Movie Reviews
@app.route('/review', methods=['POST'])
def add_review():
    data = request.json  
    review_text = data.get('review_text', '')  

    if not review_text:
        return jsonify({"error": "Review text is missing"}), 400  

    sentiment = "Positive" if "good" in review_text.lower() else "Negative"

    return jsonify({
        "message": "Review added",
        "sentiment": sentiment
    })

# Fetch Movie Recommendations (Example Data)
@app.route('/recommendations/<int:user_id>', methods=['GET'])
def recommendations(user_id):
    recommended_movies = [
        {"id": 3, "title": "Interstellar", "rating": 8.6},
        {"id": 4, "title": "The Prestige", "rating": 8.5},
    ]
    return jsonify(recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
