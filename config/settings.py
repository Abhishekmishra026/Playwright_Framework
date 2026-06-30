import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BASE_URL = os.getenv("AMAZON_BASE_URL", "https://www.amazon.com")
    SEARCH_TERM = os.getenv("AMAZON_SEARCH_TERM", "iphone 16 black 256 gb")
    USERNAME = os.getenv("AMAZON_USERNAME")
    PASSWORD = os.getenv("AMAZON_PASSWORD")
