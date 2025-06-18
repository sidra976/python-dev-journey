import requests

def fetch_news(category, country):
    url = f'https://saurav.tech/NewsAPI/top-headlines/category/{category}/{country}.json'
    response = requests.get(url)
    data = response.json()
    
    if "articles" in data and len(data["articles"]) > 0:
        article = data["articles"][0]
        author = article.get("author", "Unknown")
        title = article.get("title", "No Title")
        description = article.get("description", "No Description")
        content = article.get("content", "No Content")
        new_url = article.get("url", "No URL")
        return author, title, description, content, new_url
    else:
        raise Exception('No News headlines found at the moment!')

def main():
    category = input('Enter category (e.g., health, sports, technology): ').lower()
    country = input('Enter country code (e.g., us, gb, au): ').lower()

    try:
        author, title, description, content, new_url = fetch_news(category, country)
        print(f"\n- Author: {author}\n- Title: {title}\n- Description: {description}\n- Content: {content}\n- Read full article: {new_url}")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
