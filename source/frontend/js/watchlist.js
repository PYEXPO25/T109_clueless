// Sample Movies Data (same as in main.js and movie.js)
const movies = [
    {
        id: 1,
        title: "Inception",
        poster: "https://image.tmdb.org/t/p/w500/euCnMxNRlPrvYBU6bFmK8F2OhuV.jpg",
        rating: 8.8,
    },
    {
        id: 2,
        title: "The Dark Knight",
        poster: "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        rating: 9.0,
    },
    {
        id: 3,
        title: "Interstellar",
        poster: "https://image.tmdb.org/t/p/w500/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
        rating: 8.6,
    },
];

// Fetch Watchlist from LocalStorage
const watchlistContainer = document.getElementById("watchlist");
const watchlist = JSON.parse(localStorage.getItem("watchlist")) || [];

// Load Watchlist Movies
function loadWatchlist() {
    watchlistContainer.innerHTML = ""; // Clear existing content

    if (watchlist.length === 0) {
        watchlistContainer.innerHTML = "<p>Your watchlist is empty!</p>";
        return;
    }

    watchlist.forEach((movieId) => {
        const movie = movies.find((m) => m.id === movieId);
        if (movie) {
            const watchlistCard = document.createElement("div");
            watchlistCard.className = "watchlist-card";
            watchlistCard.innerHTML = `
                <img src="${movie.poster}" alt="${movie.title}">
                <h3>${movie.title}</h3>
                <p>Rating: ${movie.rating}</p>
                <button onclick="removeFromWatchlist(${movie.id})">Remove</button>
            `;
            watchlistContainer.appendChild(watchlistCard);
        }
    });
}

// Remove Movie from Watchlist
function removeFromWatchlist(movieId) {
    const updatedWatchlist = watchlist.filter((id) => id !== movieId);
    localStorage.setItem("watchlist", JSON.stringify(updatedWatchlist));
    alert("Movie removed from watchlist!");
    loadWatchlist(); // Reload watchlist
}

// Initial Load
loadWatchlist();
