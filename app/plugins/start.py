from pyrogram import Client, filters
from utils import logger
from utils import cache

@Client.on_message(filters.command('start'))
async def say_hello(bot, msg):
    await bot.send_message(msg.from_user.id , f'hi user')