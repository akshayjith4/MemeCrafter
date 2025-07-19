import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# List available models and their supported methods
models = genai.list_models()
for model in models:
    print(model.name, model.supported_generation_methods)
