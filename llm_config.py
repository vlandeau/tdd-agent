import os

from openai import OpenAI


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DEEPSEEK_KEY = os.environ.get("DEEPSEEK_API_KEY")
clients = {
    "openai": OpenAI(api_key=OPENAI_API_KEY),
    "deepseek": OpenAI(api_key=DEEPSEEK_KEY, base_url="https://api.deepseek.com/v1")
}
models = {
    "openai": "gpt-3.5-turbo-0125",
    "deepseek": "deepseek-coder",
}
