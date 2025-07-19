import google.generativeai as genai
import os
import time
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#model = genai.GenerativeModel("gemini-1.5-pro-latest")
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_caption(topic):
    prompt = f"""Generate 5 funny and viral meme captions about "{topic}" in this format:
**Option 1 (Tone):** "Caption" (Image idea)
**Option 2 (Tone):** "Caption" (Image idea)
Keep it engaging and short.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except ResourceExhausted as e:
        print("⚠️ Gemini quota exhausted. Waiting 20 seconds and retrying...")
        time.sleep(20)
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as inner_e:
            print("🔥 Retry failed:", inner_e)
            raise inner_e
    except Exception as e:
        print("🔥 Gemini error:", e)
        raise e
