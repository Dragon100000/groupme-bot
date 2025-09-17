from flask import Flask, request
import requests
import os

app = Flask(__name__)
BOT_ID = os.getenv("GROUPME_BOT_ID")

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  sender = data.get('name')
  text = data.get('text')

  # Avoid replying to itself
  if sender != "formbot": # Replace with your actual bot name
    message = f"{sender} said: {text}"
    requests.post("https://api.groupme.com/v3/bots/post", json={
    "bot_id": BOT_ID,
    "text": message
    })
  
  return "ok", 200

@app.route('/')
def index():
  return "Bot is running!"
