from flask import Flask, request
import requests
import os
import random
import re

simple_responses={
  ":(":[":("],
  "sad":[":("],
  "mb":["dw ur good"],
  "nvm":["ok"],
  "clank":["layl","yes?","yes","wut you need?","yes i here"],
  "double text":["1^2"],
  "?":["yes","no","idk","maybe","kinda ig", "YES!!!!","NO","yesssssss","nooooooo","yeah","nah","nope","ya","ye","yea","..."]
}
basic_response=["","ok","fr","lol", "what?","hmmmm...^ok"]
greetings=["hi","hello","hey","wsp","!-wud"]
bruh_response=["bruh","bro","...","wth","tf"]
reversePronouns={
  "me":"you",
  "my":"your",
  "i":"you"
}

app = Flask(__name__)
BOT_ID = os.getenv("GROUPME_BOT_ID")

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  sender = data.get('name')
  text = data.get('text').lower()

  
  if sender != "clank": 
    
    #choose from or
    if " or " in text:
      jsor=text.split(":")[1]
      options=jsor.split(" or ")
      message=random.choice(options)
      
    #greet
    elif any(word in text for word in greetings):
      message = f"{random.choice(greetings)}, {sender}!!!"
      
    #bruh
    elif any(word in text for word in bruh_response):
      message="null"
      
    #simple responses
    elif any(word in text for word in simple_responses):
      message=simple_response[word][random.choice(simple_response[word])
      
    #other
    else:
      if random.randint(1, 10)>1:
        message = random.choice(basic_response)
      else:
        message = "no response"

    #if "!-" in message:
      #message="wud"
    
    for old, new in reversePronouns.items():
      pattern = r"\b" + re.escape(old) + r"\b"  # match whole words only
      message = re.sub(pattern, new, message, flags=re.IGNORECASE)
    
    
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
