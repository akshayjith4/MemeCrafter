import random
import os
import uuid
import requests
from dotenv import load_dotenv
from meme_templates import get_random_template

# Load credentials from .env
load_dotenv()
IMGFLIP_USERNAME = os.getenv("IMGFLIP_USERNAME")
IMGFLIP_PASSWORD = os.getenv("IMGFLIP_PASSWORD")

def create_meme_imgflip(caption, template_id):
    if not IMGFLIP_USERNAME or not IMGFLIP_PASSWORD:
        raise Exception("Imgflip credentials not set in .env")

    if not caption or not caption.strip():
        raise Exception("Caption is empty")

    response = requests.post("https://api.imgflip.com/caption_image", data={
        'template_id': template_id,
        'username': IMGFLIP_USERNAME,
        'password': IMGFLIP_PASSWORD,
        'text0': caption,
        'text1': ''  # optional second line
    }).json()

    if not response["success"]:
        raise Exception("Failed to generate meme: " + response["error_message"])

    return response["data"]["url"]

def generate_meme(captions, selected_index=None):
    if not captions:
        raise Exception("No captions provided.")

    selected_caption = captions[selected_index] if selected_index is not None else random.choice(captions)
    # ✅ Add random string to ensure unique URL
    caption_with_uuid = f"{selected_caption} ({str(uuid.uuid4())[:5]})"

    template = get_random_template()
    meme_url = create_meme_imgflip(caption_with_uuid, template["id"])
    return meme_url, selected_caption  # 👈 Return original caption for display
