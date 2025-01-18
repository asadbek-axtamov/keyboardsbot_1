import requests
import os
TOKEN = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    button_1 = {
        'text': 'contact',
        'request_contact':True
    }
    button2={
        'text':'location',
        'request_location':True
    }
    ReplyKeyboardMarkup = {
        'keyboard': [
            [button_1],
            [button2]
        ]
    }
    params = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': ReplyKeyboardMarkup
    }

    response = requests.post(url, json = params)
    return response.json()


text = "abs"
r = send_message(chat_id, text)

