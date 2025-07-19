import requests
import os
from dotenv import load_dotenv
import random


load_dotenv()

IMGFLIP_API = "https://api.imgflip.com/caption_image"


def get_random_template():
    templates_url = "https://api.imgflip.com/get_memes"
    res = requests.get(templates_url)
    memes = res.json()["data"]["memes"]
    return random.choice(memes)  

def create_meme_imgflip(caption, template_id):
    params = {
        "template_id": template_id,
        "username": os.getenv("IMGFLIP_USERNAME"),
        "password": os.getenv("IMGFLIP_PASSWORD"),
        "text0": caption,
        "text1": "",
    }
    res = requests.post(IMGFLIP_API, params=params)
    data = res.json()
    if data["success"]:
        return data["data"]["url"]
    else:
        raise Exception("Failed to generate meme: " + data["error_message"])
