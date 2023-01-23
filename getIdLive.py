import requests
import os
from threading import Timer
from dotenv import load_dotenv
import youtubeChat

load_dotenv()

url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={os.environ.get('CHANNEL_ID')}&eventType=live&type=video&key={os.environ.get('API_KEY')}"
res = requests.get(url).json()
print(res)
if not (res["items"]):
    print("There no stream in this channel right now...")
else:
    videoId = res["items"][0]["id"]["videoId"]
    Timer(2.0, youtubeChat.getChat(videoId))
    print("running")