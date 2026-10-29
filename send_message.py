import requests 
import os 
from dotenv import load_dotenv,find_dotenv 


_=load_dotenv(find_dotenv())

TOKEN=os.environ.get("BOT_TOKEN","")
CHAT_ID=os.environ.get("TELEGRAM_CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "Hello slay3r! This message was sent by your bot."
}
requests.post(url,json=payload)
