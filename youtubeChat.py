from chat_downloader import ChatDownloader
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def getChat(url):

  now = datetime.now()

  url =f"{url}"

  date_time = now.strftime("%Y-%m-%d")

  chat = ChatDownloader().get_chat(url) 

  for message in chat:
    data = f"{chat.format(message)}\n"
    with open(f"{date_time}.txt", 'a',encoding="raw_unicode_escape") as the_file:
      the_file.write(data)
   