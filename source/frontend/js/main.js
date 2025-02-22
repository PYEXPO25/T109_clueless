// Sample Movie Data
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

// Load Movies into the Home Page
const movieList = document.getElementById("movie-list");

movies.forEach((movie) => {
    const movieCard = document.createElement("div");
    movieCard.className = "movie-card";
    movieCard.innerHTML = `
        <img src="${movie.poster}" alt="${movie.title}">
        <h3>${movie.title}</h3>
        <p>Rating: ${movie.rating}</p>
        <button onclick="viewMovie(${movie.id})">View Details</button>
    `;
    movieList.appendChild(movieCard);
});

// Redirect to Movie Details Page
function viewMovie(movieId) {
    window.location.href = `movie.html?id=${movieId}`;
}


