import requests

def cat_fact_fetcher():
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    data = response.json()

    cat_fact = data["fact"]
    return cat_fact

def main():
    try:
        cat_fact = cat_fact_fetcher()
        print(f"Did you know?: {cat_fact}")
    except Exception as e:
        print('Error', str(e))

if __name__ == "__main__":
    main()

