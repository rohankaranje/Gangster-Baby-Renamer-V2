import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6087816605:AAFsPV-uIOs8OhTSF9PN2lOE2GbdAzMTep8")

API_ID = int(os.environ.get("API_ID", "d89d7c5ac61ea8f467a6a75aa54a51ca"))

API_HASH = os.environ.get("API_HASH", "26184984")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
