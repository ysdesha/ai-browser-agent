import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def parse_intent(user_command):

    try:

        with open(
            "prompts/system_prompt.txt",
            "r",
            encoding="utf-8"
        ) as f:

            system_prompt = f.read()

        prompt = f"""
{system_prompt}

User Command:
{user_command}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {e}"