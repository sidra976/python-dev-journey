import requests
def fetch_random_user_freeapi():
    url = ('https://api.freeapi.app/api/v1/public/randomusers/user/random')
    response = requests.get(url)
    print(response)    

url = ('https://api.freeapi.app/api/v1/public/randomusers/user/random')
response = requests.get(url)
print(response)       