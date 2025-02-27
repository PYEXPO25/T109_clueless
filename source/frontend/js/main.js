// Fetch Movies from Flask API and Display on Home Page
document.addEventListener("DOMContentLoaded", function () {
    fetch("http://127.0.0.1:5000/movies") // Calls Flask API
        .then(response => response.json()) // Convert response to JSON
        .then(movies => {
            const movieList = document.getElementById("movie-list");
            movieList.innerHTML = ""; // Clear any existing data

            movies.forEach((movie) => {
                const movieCard = document.createElement("div");
                movieCard.className = "movie-card";
                movieCard.innerHTML = `
                    <img src="${movie.poster_url}" alt="${movie.title}">
                    <h3>${movie.title}</h3>
                    <p>IMDb Rating: ${movie.imdb_rating}</p>
                    <p>Rotten Tomatoes: ${movie.rotten_tomatoes}</p>
                    <p>Metacritic: ${movie.metacritic}</p>
                    <button onclick="viewMovie(${movie.id})">View Details</button>
                `;
                movieList.appendChild(movieCard);
            });
        })
        .catch(error => console.error("Error fetching movies:", error));
});

// Redirect to Movie Details Page
function viewMovie(movieId) {
    window.location.href = `movie.html?id=${movieId}`;
}

