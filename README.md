# 🎬 IMDB CLI

A simple command-line interface that fetches and displays movie data from [The Movie Database (TMDB)](https://www.themoviedb.org/) directly in your terminal.

---

## ✨ Features

- Fetches movie data directly from The Movie Database (TMDB) API
- Supports multiple categories: **Now Playing**, **Popular**, **Top Rated**, and **Upcoming** movies
- Displays results in a clean, human-readable JSON format
- Handles network and API errors gracefully (timeouts, bad responses, missing tokens)
- Allows users to specify movie type via command-line arguments
- Loads secure API credentials from a `.env` file for safety

---

## 📦 Installation

Clone this repository and move into the project directory:

```bash
git clone https://github.com/Simply-Blessing/IMDB_APP.git
cd IMDB_APP
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file in the project root and add your TMDB API token:

```bash
TMDB_ACCESS_TOKEN=your_tmdb_api_token_here
```

---

## 🚀 Usage

```bash
python tmdb_app.py --type <playing|popular|top|upcoming>
```

Example:

```bash
python tmdb_app.py --type top
```

Output:

```bash
Here are the top movies:
{
    "title": "Grave of the Fireflies",
    "release_date": "1988-04-16",
    "rating": 8.447,
    "overview": "In the final months of World War II, 14-year-old Seita and his sister Setsuko are orphaned when their mother is killed during an air raid in Kobe, Japan. After a falling out with their aunt, they move into an abandoned bomb shelter. With no surviving relatives and their emergency rations depleted, Seita and Setsuko struggle to survive."
}
```

---

## Project Inspiration

[TMDB CLI](https://roadmap.sh/projects/tmdb-cli)
