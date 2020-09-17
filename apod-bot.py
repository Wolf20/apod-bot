import telebot
import requests
import json
from googletrans import Translator as trans
from credentials import *

bot = telebot.TeleBot(tg_key)
def t(text, dest, src):
    text= str(text)
    dest = str(dest)
    src= str(src)  
    text = translator.translate(text, dest=(dest),src=src)
    return text.text

def main():
    payload = { 'api_key' : nasa_key}
    r = requests.get(BASE_URL, params = payload)
    response = r.content
    json2py = json.loads(response)
    if json2py['media_type'] == "video":
        reply = t(f"Today's APOD is [{json2py['title']}]({json2py['url']}).\n\n{json2py['explanation']}","es","en")
        bot.send_message(chat_id, reply, parse_mode='markdown')
    else:
        if 'copyright' not in json2py:
            reply = t("Today's APOD is [{json2py['title']}]({json2py['url']}).\n\n{json2py['explanation']}\n\nCheck out HD picture [here]({json2py['hdurl']}).","es","en")
        else:
            reply = t(f"Today's APOD is [{json2py['title']}]({json2py['url']}).\n\n{json2py['explanation']}\n\nCheck out HD picture [here]({json2py['hdurl']}).\n\nImage Credit & Copyright: {json2py['copyright']}.","es","en")
        bot.send_message(chat_id, reply, parse_mode='markdown')

if __name__ == '__main__':
    translator = trans()
    main()
    
