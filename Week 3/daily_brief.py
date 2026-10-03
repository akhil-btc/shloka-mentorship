import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

load_dotenv()
api_key = os.getenv("NEWSAPI_KEY")

if not api_key:
    print("Missing API key. Add NEWSAPI_KEY to your .env file.")
else:
    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "category": "technology",
        "pageSize": 5,
    }

    headers = {"X-Api-Key": api_key}

    try:
        response = requests.get(
            url, params=params, headers=headers, timeout=10
        )

        if response.status_code == 429:
            print("Rate limit reached. Try again later.")
        else:
            response.raise_for_status()
            articles = response.json()["articles"]

            text = ""

            for article in articles[:5]:
                text += f"Title: {article['title']}\n"
                text += f"Source: {article['source']['name']}\n"
                text += f"URL: {article['url']}\n\n"

            console = Console()
            console.print(
                Panel(text or "No articles found.", title="Today's Tech")
            )

    except requests.RequestException:
        print("Could not get the news. Check your connection or API key.")