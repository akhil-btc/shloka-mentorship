
import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq, APIError


load_dotenv(Path(__file__).with_name(".env"))
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("Missing GROQ_API_KEY. Add it to your .env file.")
else:
    client = Groq(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": "In 3 sentences, explain to me what a Large Language Model is, like I'm a 10th grader.",
                }
            ],
        )
        print(response.choices[0].message.content)
    except APIError as error:
        print("Groq error:", error)