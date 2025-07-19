import requests
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("IMGFLIP_USERNAME")
PASSWORD = os.getenv("IMGFLIP_PASSWORD")

params = {
    "template_id": "181913649",  # "Drakeposting"
    "username": USERNAME,
    "password": PASSWORD,
    "text0": "Top Text",
    "text1": "Bottom Text"
}

response = requests.post("https://api.imgflip.com/caption_image", params=params)

print("Success:", response.json()["success"])
print("Response:", response.json())
