from flask import Flask, request
import requests
import os
import random

random_word_bank=[]
question_response=["yes","no","idk","maybe","kinda ig", "YES!!!!","NO","yesssssss","nooooooo","yeah","nah","nope","ya","ye","yea","..."]
basic_response=["","ok","fr","lol", "what?","hmmmm...^ok"]
greetings=["hi","hello","heyyyyy","wsp","wud"]

app = Flask(__name__)
BOT_ID = os.getenv("GROUPME_BOT_ID")

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  sender = data.get('name')
  text = data.get('text').lower()

  
  if sender != "clank": 
    for i in greetings:
      if greetings[i] in text:
        message = f"hello, {sender}!!!"
    if "?" in text:
      message = random.choice(question_response)
      
    elif "bruh" in text || text=="..." || "bro" in text:
      #dont say anything
    elif text == "double send":
      message="1^2"
    else:
      if random.randomint(1,10)>5:
        message = random.choice(basic_response)
      else:
        message = "no response"
    mess_arr=message.split("^")
    for i in mess_arr:
      requests.post("https://api.groupme.com/v3/bots/post", json={
      "bot_id": BOT_ID,
      "text": mess_arr
      })
  
  return "ok", 200

@app.route('/')
def index():
  return "Bot is running!"
  
if __name__ == '__main__':
  import os
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
