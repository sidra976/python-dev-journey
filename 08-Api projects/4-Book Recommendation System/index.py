import requests
import json 
import os
import random

# FILE_NAME = 'book_recommendation.py'

# def load_data():
#     if os.path.exists(FILE_NAME):
#         with open(FILE_NAME, 'r') as file:
#             return json.load(file)
#     else:
#         return []

genres = [
    "scifi",
    "fantasy",
    "mystery",
    "thriller",
    "romance",
    "horror",
    "historical fiction",
    "crime",
    "adventure",
    "young adult",
    "childrens books",
    "classics",
    "non-fiction",
    "biography",
    "self-help",
    "memoir",
    "poetry",
    "drama",
    "comedy",
    "action"
]

def get_books(genre):
    url = f'https://openlibrary.org/search.json?subject={genre}'
    response = requests.get(url)
    data = response.json()

    if "docs" in data and len(data["docs"]) > 0:
        book = random.choice(data["docs"])
        author_name = book.get("author_name", ["Unknown"])[0]
        book_title = book.get("title", "Unknown Title")
        published_year = book.get("first_publish_year", "Unknown")
        return author_name, book_title, published_year
    else:
        raise Exception("No books found for this genre.")


def main():
    print('Avaiable Genres: ')
    for i, val in enumerate(genres, start=1):
        print(f"{i} - {val}")

    user_input = input('Pick any genre(1-20): ')  
    for i, val in enumerate(genres, start=1):
        if int(user_input) == i:
            try:
                author_name, book_title, published_year = get_books(val)
                print(f"- Title: {book_title}\n- Author: {author_name}\n- Year: {published_year}")
            except Exception as e:
                print("Error:", str(e))
            break  # ✅ Don't forget this!
    else:
        print('Invalid number')


if __name__ == "__main__":
    main()
        



