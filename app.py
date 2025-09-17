from flask import Flask, request
import requests
import os
import random

random_word_bank=[]
question_response=["yes","no","idk","maybe","kinda ig", "YES!!!!","NO","yesssssss","nooooooo","yeah","nah","nope","ya","ye","yea","..."]
basic_response=["","ok","fr","cap","lol"]

app = Flask(__name__)
BOT_ID = os.getenv("GROUPME_BOT_ID")

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  sender = data.get('name')
  text = data.get('text').lower()

  # Avoid replying to itself
  if sender != "clank": # Replace with your actual bot name
    if "?" in text:
      message = random.choice(question_response)
      
    elif "hi" in text:
      message = f"hello, {sender}!!!"
    else:
      message = random.choice(basic_response)
    
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
