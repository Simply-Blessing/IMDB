import requests, json, os, argparse,sys
from dotenv import load_dotenv


def fetch_movies(movie_type,api_token):
    endpoints = {
        "playing": "https://api.themoviedb.org/3/movie/now_playing",
        "popular": "https://api.themoviedb.org/3/movie/popular",
        "top": "https://api.themoviedb.org/3/movie/top_rated",
        "upcoming": "https://api.themoviedb.org/3/movie/upcoming"
    }
    url = endpoints.get(movie_type)
    if not url:
        raise ValueError(f"Invalid movie type: {movie_type}")
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_token}"
    }
    #handling API request errors
    try:
        response = requests.get(url, headers=headers,timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        sys.exit("Request timed out. Please check your connection.")
    except requests.exceptions.ConnectionError:
        sys.exit("Connection error. Please check your internet connection.")
    except requests.exceptions.HTTPError as http_err:
        sys.exit(f"HTTP error occurred: {http_err}")
    except Exception as err:
        sys.exit(f"An error occurred: {err}")

def movies_result(data,movie_type):
    results = data.get("results",[])
    if not results:
        print("No movies found.")
        return
    print(f"Here are the {movie_type} movies:\n")

    for movie in results:
        movie_info = {
            "title": movie.get("title"),
            "release_date": movie.get("release_date"),
            "rating": movie.get("vote_average"),
            "overview": movie.get("overview")
        }
        print(json.dumps(movie_info, indent=4))
        
def main():
    parser = argparse.ArgumentParser(description="Movie IMDB CLI", add_help=True)
    parser.add_argument('--type',type=str, 
                        help="Type of movie you would like to see",
                        choices=["playing","popular","top","upcoming"],
                        required=True)
    args = parser.parse_args()
    
    #fetch the API token from .env file
    load_dotenv(dotenv_path=".env")
    api_token = os.getenv("TMDB_ACCESS_TOKEN")
    if not api_token:
        sys.exit("API token not found. Please set TMDB_ACCESS_TOKEN in your .env file.")

    data = fetch_movies(args.type, api_token)
    movies_result(data, args.type)

if __name__=="__main__":
    main()