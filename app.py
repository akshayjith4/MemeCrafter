from flask import Flask, render_template, request
from meme_generator import generate_meme
from gemini_gen import generate_caption
from reddit import get_trending_topic
from caption_generator import extract_captions  # ✅ Only using this
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    meme_url = None
    caption = None
    all_captions = []

    if request.method == "POST":
        try:
            topic = request.form.get("topic") or get_trending_topic()
            print("🔍 Topic received:", topic)

            # Delay to avoid flooding Gemini API
            time.sleep(5)

            captions_raw = generate_caption(topic)
            print("📨 Raw captions from Gemini:", captions_raw)

            all_captions = extract_captions(captions_raw)
            print("✅ Cleaned captions:", all_captions)

            if not all_captions:
                raise Exception("No captions returned from Gemini.")

            selected_caption = request.form.get("selected_caption") or all_captions[0]
            print("🎯 Selected caption:", selected_caption)

            meme_url, caption = generate_meme(all_captions, all_captions.index(selected_caption))
            print("🖼️ Meme URL:", meme_url)

        except Exception as e:
            print("🚨 Error during meme generation:", e)
            if 'quota' in str(e).lower() or '429' in str(e):
                caption = "⚠️ Gemini API quota exceeded. Please try again in a few minutes."
            else:
                caption = "❌ Something went wrong. Please try again later."
            meme_url = None

    return render_template("index.html", meme_url=meme_url, captions=all_captions, used_caption=caption)

if __name__ == "__main__":
    app.run(debug=False)
