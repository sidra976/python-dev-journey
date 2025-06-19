import json
import os
import requests

API_KEY = 'e8ec7085'

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

def main():
    try:
        movie_title = input('Enter movie title: ')
        title, year, director, plot, imdb_Rating  = movie_finder(movie_title)
        print(f'-Title: {title} \n-Year: {year}, \n-Director: {director}, \n-Plot Summary: {plot}, \n-Imdb Rating: {imdb_Rating} ')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
   main()        


