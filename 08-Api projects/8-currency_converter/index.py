import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_result():
    convert_from = 'USD'
    convert_to = 'PKR'
    amount = 10

    URL = f'https://api.exchangerate.host/convert?from={convert_from}&to={convert_to}&amount={amount}&access_key={API_KEY}'
    # URL = f'https://api.exchangerate.host/convert?from=USD&to=PKR&amount=10&access_key={API_KEY}'
    response = requests.get(URL)
    data = response.json()

    result = data["result"]
    return result

def main():
    try:
        result = get_result()
        print(f"Amount: {result}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
   main()



