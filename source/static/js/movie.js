// Sample Movies Data
const movies = [
    {
        id: 1,
        title: "Inception",
        poster: "https://image.tmdb.org/t/p/w500/euCnMxNRlPrvYBU6bFmK8F2OhuV.jpg",
        rating: 8.8,
        description: "A skilled thief is offered a chance to erase his criminal history if he can successfully perform inception.",
    },
    {
        id: 2,
        title: "The Dark Knight",
        poster: "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        rating: 9.0,
        description: "Batman sets out to dismantle the remaining criminal organizations in Gotham with the help of Lieutenant Jim Gordon and Harvey Dent.",
    },
    {
        id: 3,
        title: "Interstellar",
        poster: "https://image.tmdb.org/t/p/w500/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
        rating: 8.6,
        description: "A group of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    },
];

// Fetch Movie ID from URL
const urlParams = new URLSearchParams(window.location.search);
const movieId = parseInt(urlParams.get("id"));
const movie = movies.find((m) => m.id === movieId);

// Load Movie Details
const movieDetails = document.getElementById("movie-details");

if (movie) {
    movieDetails.innerHTML = `
        <img src="${movie.poster}" alt="${movie.title}">
        <div class="details">
            <h2>${movie.title}</h2>
            <p>Rating: ${movie.rating}</p>
            <p>${movie.description}</p>
            <button onclick="addToWatchlist(${movie.id})">Add to Watchlist</button>
        </div>
    `;
} else {
    movieDetails.innerHTML = "<p>Movie not found.</p>";
}

// Add Movie to Watchlist
function addToWatchlist(movieId) {
    const watchlist = JSON.parse(localStorage.getItem("watchlist")) || [];
    if (!watchlist.includes(movieId)) {
        watchlist.push(movieId);
        localStorage.setItem("watchlist", JSON.stringify(watchlist));
        alert(`${movie.title} has been added to your watchlist!`);
    } else {
        alert(`${movie.title} is already in your watchlist.`);
    }
}

// Render Sentiment Analysis Chart
const ctx = document.getElementById("review-chart").getContext("2d");
const sentimentChart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: ["Positive", "Neutral", "Negative"],
        datasets: [
            {
                label: "Sentiment Analysis",
                data: [70, 20, 10], // Placeholder data
                backgroundColor: ["#4caf50", "#ffeb3b", "#f44336"],
            },
        ],
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
        },
    },
});
