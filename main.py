import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

API_TOKEN ='5354627696:AAFhdHJK8aSPNsBd6rMErBesSFPEgAal0Co'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

import sqlite3
from sqlite import Database
db = Database("main.db")
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    name = message.from_user.username
    try:
        db.create_table_users()
    except:
        pass
    try:
        db.add_user(id=message.from_user.id,
                    name=message.from_user.full_name,
                    email=f"@{name}")
        count_user = db.count_users()[0]
        mes = f"base add @{name} bazada {count_user} bor "
        await bot.send_messsage(chat_id=625700527, text = mes)
    except sqlite3.IntegrityError:
        pass
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)