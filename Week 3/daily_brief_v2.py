import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from groq import Groq, APIError
from rich.console import Console
from rich.panel import Panel


load_dotenv(Path(__file__).with_name(".env"))
news_key = os.getenv("NEWSAPI_KEY")
groq_key = os.getenv("GROQ_API_KEY")
console = Console()

if not news_key:
    console.print(Panel("(unable to fetch news)", title="Today's Tech"))
else:
    url = "https://newsapi.org/v2/top-headlines"
    params = {"country": "us", "category": "technology", "pageSize": 5}
    headers = {"X-Api-Key": news_key}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        articles = response.json()["articles"]
    except (requests.RequestException, ValueError, KeyError):
        console.print(Panel("(unable to fetch news)", title="Today's Tech"))
    else:
        client = Groq(api_key=groq_key) if groq_key else None
        text = ""

        for article in articles[:5]:
            title = article.get("title") or "Untitled"
            text += f"Original: {title}\n"

            if client:
                try:
                    answer = client.chat.completions.create(
                        model="openai/gpt-oss-20b",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a friendly summarizer. Rewrite this news headline in one sentence for a 10th grader who isn't into tech.",
                            },
                            {"role": "user", "content": title},
                        ],
                    )
                    text += f"Rewritten: {answer.choices[0].message.content}\n"
                except APIError:
                    pass  # Keep the original headline if Groq fails.

            text += f"Source: {(article.get('source') or {}).get('name') or 'Unknown'}\n"
            text += f"URL: {article.get('url') or 'Not provided'}\n\n"

        console.print(Panel(text or "No articles found.", title="Today's Tech"))
