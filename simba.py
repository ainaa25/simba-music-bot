from pyrogram import Client
import os

simba = Client(
    "simba",
    api_id = int(os.environ["API_ID"]
    ),
    
    api_hash =os.environ["API_HASH"]
    ,
    
    bot_token =os.environ["BOT_TOKEN
    "]
)
