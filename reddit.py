import requests

def get_trending_topic():
    try:
        response = requests.get("https://www.reddit.com/r/all/top.json?limit=10&t=day", headers={"User-agent": "meme-gen"})
        posts = response.json()["data"]["children"]
        titles = [post["data"]["title"] for post in posts]
        return titles[0]
    except Exception:
        return "current events"
