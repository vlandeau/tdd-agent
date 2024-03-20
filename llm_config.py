import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DEEPSEEK_KEY = os.environ.get("DEEPSEEK_API_KEY")
clients = {
    "openai": OpenAI(api_key=OPENAI_API_KEY),
    "deepseek": OpenAI(api_key=DEEPSEEK_KEY, base_url="https://api.deepseek.com/v1")
}
models = {
    "openai": "gpt-4-0125-preview",
    "deepseek": "deepseek-coder",
}
