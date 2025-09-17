from flask import Flask, request
import requests
import os

random_word_bank=[]
question_response=["yes","no","idk"]

app = Flask(__name__)
BOT_ID = os.getenv("GROUPME_BOT_ID")

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  sender = data.get('name')
  text = data.get('text')

  # Avoid replying to itself
  if sender != "friend bot": # Replace with your actual bot name
    if "?" in text:
      message=question_response[random(0,2)]
    
    message = f"{sender} said: {text}"
    
    requests.post("https://api.groupme.com/v3/bots/post", json={
    "bot_id": BOT_ID,
    "text": message
    })
  
  return "ok", 200

@app.route('/')
def index():
  return "Bot is running!"
  
if __name__ == '__main__':
  import os
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
