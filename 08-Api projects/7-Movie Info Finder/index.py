import json
import os
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
FILE_NAME = 'movies.json'

def view_past_movies():
    if not os.path.exists(FILE_NAME):
        print("No movies saved yet.")
        return

    with open(FILE_NAME, 'r') as file:
        try:
            movies = json.load(file)
        except json.JSONDecodeError:
            print("Error reading saved movies.")
            return

    if not movies:
        print("Movie list is empty.")
    else:
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie['title']} ({movie['year']}) - Directed by {movie['director']}, IMDb: {movie['imdb_Rating']}")


def save_movies(movies_data):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.append(movies_data)
    with open(FILE_NAME, 'w') as file:
        json.dump(existing_data, file, indent=4)



def movie_finder(movie_title):
    user_title = movie_title

    URL = f"https://www.omdbapi.com/?t={user_title}&apikey={API_KEY}"
    response = requests.get(URL)
    data = response.json()

    title = data["Title"]
    year = data["Year"]
    director = data["Director"]
    plot = data["Plot"]
    imdb_Rating = data["imdbRating"]
    return title, year, director, plot, imdb_Rating

def search_movie():
        try:
            movie_title = input('Enter movie title: ')
            title, year, director, plot, imdb_Rating  = movie_finder(movie_title)
            print(f'-Title: {title} \n-Year: {year}, \n-Director: {director}, \n-Plot Summary: {plot}, \n-Imdb Rating: {imdb_Rating} ')
            
            movies_data = {
                'title' : title,
                'year' : year,
                'director' : director,
                'plot' : plot,
                'imdb_Rating' : imdb_Rating
            }
            save_movies(movies_data)
            view_past_movies(movies_data)
        except Exception as e:
            print(str(e))

while True:
    print('\n Movie Finder')
    print('1-Search Movie')
    print('2-View save movie list')
    print('3-Close App')
    
    choices = input('Enter you choice: ')

    match choices:
        case '1':
            search_movie()
        case '2':
            view_past_movies()  
        case '3':
            print('Existing..')
            break
        case _:
            print('Invalid Input')   



     


