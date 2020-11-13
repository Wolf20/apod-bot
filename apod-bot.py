import telebot
import requests
import json
import time as tiempo
from googletrans import Translator
from credentials import *


#Init some variables and functions
bot = telebot.TeleBot(tg_key)
telepost = bot.send_message
translate = Translator().translate
lang = 'es'

def main():
    try:
        payload = { 'api_key' : nasa_key}
        r = requests.get(BASE_URL, params = payload)
        response = r.content
        json2py = json.loads(response)
        if lang == "en":
            intro = f"Today's APOD is"
        elif lang == "es":
            intro = f"El APOD de hoy es"
        else:
            intro = translate(f"Today's APOD is", dest=lang).text
        title = translate(f"{json2py['title']})", dest=lang).text
        url = f"{json2py['url']}"
        explanation = translate(f"{json2py['explanation']}", dest=lang).text
        if lang == "en":
            outro = f"Check out HD picture [here]"
        elif lang == "es":
            outro = f"Mira la imagen en HD [aqui]"
        else:
            outro = translate(f"Check out HD picture [here]", dest=lang).text
        if lang == "en":
            coutro = f"Image Credit & Copyright"
        elif lang == "es":
            coutro = f"Creditos y Copyright de la Imagen"
        else:
            coutro = translate(f"Image Credit & Copyright", dest=lang).text
        if json2py['media_type'] == "video":
            teleapod = intro + " [" + title + "](" + url + ")" + ".\n\n" + explanation
        else:
            hdurl = f"{json2py['hdurl']}"
            if 'copyright' not in json2py:
                teleapod = intro + " [" + title + "](" + url + ").\n\n" + explanation + "\n\n" + outro + "(" + hdurl + ")."
            else:
                imgrights = f"{json2py['copyright']}"
                teleapod = intro + " [" + title + "](" + url + ").\n\n" + explanation + "\n\n" + outro + "(" + hdurl + ").\n\n" + coutro + ": " + imgrights + "."
        telepost(chat_id, teleapod, parse_mode='markdown')
    except AttributeError:
        tiempo.sleep(10)
        print( " No se ha podido contactar con los servidores de google, reintentando...")
        main()

if __name__ == '__main__':
        main()
    
