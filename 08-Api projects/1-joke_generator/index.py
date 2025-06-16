import requests

def get_jokes():
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    data = response.json()

    # Directly access setup and punchline since the API doesn't use 'success' or 'data'
    joke_setup = data["setup"]
    joke_punchline = data["punchline"]
    return joke_setup, joke_punchline

def main():
    try:
        joke_setup, joke_punchline = get_jokes()
        print(f"Joke Setup: {joke_setup}\nJoke Punchline: {joke_punchline}")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
