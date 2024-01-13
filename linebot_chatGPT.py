from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

import openai
openai.api_key = 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
model_use = "text-davinci-003"

channel_secret = 229899f41da92b96d4d16bd03b32338e
channel_access_token = Nmsi4hCXXmI8M3CLVYryyAgy8zqYWrcaigqfHt9T34S9XH+SwpZiezoUPtd//Qs+aghjM3jO66FtTyLlUEMtjj3MAZifUQMG9Gre+IuXi6BGCnGd4UekcJCwYAgVtRWas8iUJGaOdGzLhRPLeHGTogdB04t89/1O/w1cDnyilFU=

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    try:
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        handler.handle(body, signature)
    except:
        pass
    
    return "Hello Line Chatbot"

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text)

    prompt_text = text

    response = openai.Completion.create(
        model=model_use,
        prompt=prompt_text,  
        max_tokens=1024) # max 4096

    text_out = response.choices[0].text 
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

if __name__ == "__main__":          
    app.run()

