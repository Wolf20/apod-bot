import telebot
from googletrans import Translator
import requests
import json
from credentials import *
translator = Translator()
translator.raise_Exception = True

bot = telebot.TeleBot(tg_key)

def main():
    payload = { 'api_key' : nasa_key}
    r = requests.get(BASE_URL, params = payload)
    response = r.content
    json2py = json.loads(response)


    titulo = translator.translate(json2py['title'], dest='es')
    cuerpo = translator.translate(json2py['explanation'], dest='es')

    
    if json2py['media_type'] == "video":
        reply = f"El APOD de hoy es [{titulo.text}]({json2py['url']}).\n\n{cuerpo.text}"
        bot.send_message(chat_id, reply, parse_mode='markdown')
    else:
        if 'copyright' not in json2py:
            reply = f"El APOD de hoy es [{titulo.text}]({json2py['url']}).\n\n{cuerpo.text}\n\Mira la imagen en HD [aqui]({json2py['hdurl']})."
        else:
            reply = f"El APOD de hoy es [{titulo.text}]({json2py['url']}).\n\n{cuerpo.text}\n\nMira la imagen en HD [aqui]({json2py['hdurl']}).\n\nCredito y Copyright de la imagen: {json2py['copyright']}."
        bot.send_message(chat_id, reply, parse_mode='markdown')

if __name__ == '__main__':
    main()
