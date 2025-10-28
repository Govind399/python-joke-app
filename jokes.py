# jokes.py

import requests

API_URL = "https://official-joke-api.appspot.com/jokes/programming/random"

def get_random_joke():
    """
    Fetches a random programming joke from the API.
    
    Returns:
        dict: A dictionary containing the joke's setup and punchline, or None if an error occurs.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()[0]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None