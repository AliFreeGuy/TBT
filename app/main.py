import asyncio
import uvloop
from pyrogram import Client, idle
from utils import logger
import config 



async def main():
    bot_client = Client(
        config.BOT_SESSION,
        config.API_ID,
        config.API_HASH,
        bot_token=config.BOT_TOKEN,
        workdir=config.WORK_DIR,
        plugins=dict(root="plugins")
    )
    
    if config.DEBUG =='True':
        bot_client.proxy = config.PROXY

    await bot_client.start()
    await idle()

if __name__ == '__main__':
    uvloop.install()
    asyncio.run(main())