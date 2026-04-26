#
# CREATE BOT IN TELEGRAM:
#         open telegram app
#         in search icon type BotFather , in the result type the one with blue checkmark
#         type start then /newbot   then send /empty
#         BotFather will then give you your Bot Token : SAVE IT !
#         then to get your chat id , open bot, send to it any message: type hello
#         then open this url in your browser :
#         https://api.telegram.org/bot"YOUR_TOKEN_HERE"/getUpdates  # without the strings
#         inside the response in browser note the id of the chat
#         now you have your token and your chat id
#
# USAGE:
#         import telegram
#         device_id = "ESP_Kitchen" 
#         telegram.send_telegram(device_id,"Hello From ESP")
#
# USAGE WITH MINIMUM MEMORY USAGE:
#
#         from telegram import send_telegram
#         send_telegram("ESP32_Kitchen", "Hello!")

import urequests
import ujson
import gc

TELEGRAM_TOKEN = "8774110596:AAEylbWoLA5bWnasp2oaqPXAlU1MYaMudME"
TELEGRAM_CHAT_ID = "8368702577"


def send_telegram(device_id, message):
    try:
        url = "https://api.telegram.org/bot{}/sendMessage".format(TELEGRAM_TOKEN)
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": "{}: {}".format(device_id, message)
        }
        headers = {"Content-Type": "application/json"}
        response = urequests.post(url, data=ujson.dumps(payload), headers=headers)
        print("Telegram status:", response.status_code)
        response.close()
    except Exception as e:
        print("Telegram error:", e)
    finally:
        gc.collect()