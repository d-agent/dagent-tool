import os
from dotenv import load_dotenv
import httpx

# Load .env from the user's project
load_dotenv()

def get_api_key():
    api_key = os.getenv("DAGENT_API_KEY")
    if not api_key:
        raise ValueError("DAGENT_API_KEY is missing. Add it in your .env file.")
    return api_key

def get_cookies():
    cookies = httpx.Cookies()
    # if not cookies:
    #     raise ValueError("COOKIES is missing. Add it in your .env file.")
    return cookies