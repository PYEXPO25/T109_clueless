import pandas as pd

def get_recommendations(user_id):
    # Mock data for simplicity
    movies = [
        {'id': 1, 'title': 'Inception', 'rating': 8.8},
        {'id': 2, 'title': 'The Dark Knight', 'rating': 9.0},
        {'id': 3, 'title': 'Interstellar', 'rating': 8.6},
    ]
    # Add logic to recommend based on user preferences or collaborative filtering
    return movies[:2]
