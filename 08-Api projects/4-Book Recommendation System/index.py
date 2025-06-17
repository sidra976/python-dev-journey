import requests
import random
import json
import os

genres = [
    "scifi", "fantasy", "mystery", "thriller", "romance", "horror",
    "historical fiction", "crime", "adventure", "young adult",
    "childrens books", "classics", "non-fiction", "biography",
    "self-help", "memoir", "poetry", "drama", "comedy", "action"
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

def save_book_to_file(book_data, filename="books.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.append(book_data)

    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)

def main():
    print('Available Genres:')
    for i, val in enumerate(genres, start=1):
        print(f"{i} - {val}")

    user_input = input('Pick any genre (1-20): ')
    try:
        user_choice = int(user_input)
        if 1 <= user_choice <= 20:
            val = genres[user_choice - 1]
            try:
                author_name, book_title, published_year = get_books(val)
                print(f"\n📚 Book Recommendation:")
                print(f"- Title: {book_title}\n- Author: {author_name}\n- Year: {published_year}")

                book_info = {
                    "genre": val,
                    "title": book_title,
                    "author": author_name,
                    "year": published_year
                }
                save_book_to_file(book_info)
                print("✅ Book saved to books.json!")
            except Exception as e:
                print("❌ Error:", str(e))
        else:
            print("⚠️ Invalid number. Choose between 1 and 20.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
