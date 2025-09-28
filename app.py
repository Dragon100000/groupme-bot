from flask import Flask, request
import requests
import os
import random

random_word_bank=[]
question_response=["yes","no","idk","maybe","kinda ig", "YES!!!!","NO","yesssssss","nooooooo","yeah","nah","nope","ya","ye","yea","..."]
basic_response=["","ok","fr","lol", "what?","hmmmm...^ok"]
greetings=["hi","hello","hey","wsp","!-wud"]
bruh_response=["bruh","bro","...","wth","tf"]

app = Flask(__name__)
BOT_ID = os.getenv("GROUPME_BOT_ID")

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  sender = data.get('name')
  text = data.get('text').lower()

  
  if sender != "clank": 
    
    if "?" in text:
      message = random.choice(question_response)
      
    elif any(word in text for word in greetings):
      message = f"{random.choice(greetings)}, {sender}!!!"
    elif any(word in text for word in bruh_response):
      message="null"
    elif text == "double send":
      message="1^2"
    else:
      if random.randomint(1,10)>50:
        message = random.choice(basic_response)
      else:
        message = "no response"

    #if "!-" in message:
      #message="wud"
    mess_arr=message.split("^")
    for i in mess_arr:
      requests.post("https://api.groupme.com/v3/bots/post", json={
      "bot_id": BOT_ID,
      "text": i
      })
  
  return "ok", 200

@app.route('/')
def index():
  return "Bot is running!"
  
if __name__ == '__main__':
  import os
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
