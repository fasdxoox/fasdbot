import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/72b1f87ac7a3dffcd07a4.png",
        caption = f"""<b>  <b>\n<a href="https://t.me/EF_19"> ➮ 𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐬𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐬𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥🧚‍♀", url=f"https://t.me/K55DD"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتك او قناتك", url=f"http://t.me/LL0_BOT?startgroup"),         
                ],

            ]

        ),

    )
