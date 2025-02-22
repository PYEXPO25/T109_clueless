// Fetch Watchlist from LocalStorage
const watchlist = JSON.parse(localStorage.getItem("watchlist")) || [];

// Update Watchlist Stats
const watchlistCount = document.getElementById("watchlist-count");
watchlistCount.textContent = `Movies in Watchlist: ${watchlist.length}`;
