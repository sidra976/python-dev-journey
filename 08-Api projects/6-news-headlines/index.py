import requests
import json
import os

FILE_NAME = 'news.json'
def fetch_news(category, country):
    user_category = category
    user_country = country
    url = f'https://saurav.tech/NewsAPI/top-headlines/category/{user_category}/{user_country}.json'
    response = requests.get(url)
    data = response.json()
    
    if "articles" in data and len(data["articles"]) > 0:
        author = data["articles"][0]["author"]
        title = data["articles"][0]["title"]
        description = data["articles"][0]["description"]
        content= data["articles"][0]["content"]
        newUrl = data["articles"][0]["url"]
        return author, title, description, content, newUrl
    else:
       raise Exception('No News headlines found at the moment!')
    

def save_news(news_data):
    if os.path.exists(FILE_NAME):
      with open(FILE_NAME, 'r') as file:
         existing_data = json.load(file)
    else:
     existing_data = []     

     existing_data.append(news_data)
     with open(FILE_NAME, "w") as file:
        json.dump(existing_data, file, indent=4)
    
         

def main():
    category = input('Enter category || (e.g., health, sports, technology): ')
    country = input('Enter category: || (e.g., us, gb, au, ca, de, fr, jp, cn, ru): ')

    category = category.lower()
    country = country.lower()
    try:
      author, title, description, content, newUrl = fetch_news(category, country)
      print(f"-author: {author} \n-Title: {title} \n-description: {description} \n-Headline: {content} \n \n-Read full article: {newUrl}")
      news_data = {
         'author' : author,
         'title' : title,
         'description' : description,
         'content' : content,
         'newUrl' : newUrl
      }
      save_news(news_data)
    except Exception as e:
     print(str(e))


if __name__ == "__main__":
   main()

