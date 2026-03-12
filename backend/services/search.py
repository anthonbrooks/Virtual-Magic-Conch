import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")

def search_web(query):
    url = "https://api.search.brave.com/res/v1/web/search"

    headers = {
        "X-Subscription-Token": BRAVE_API_KEY
    }

    params = {
        "q": query,
        "count": 5
    }

    res = requests.get(url, headers=headers, params=params)
    data = res.json()

    return [r["url"] for r in data["web"]["results"]]