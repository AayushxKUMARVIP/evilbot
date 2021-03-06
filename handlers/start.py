from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""๐ Hi {message.from_user.first_name}!

โจ I am รชvilแบรธโ  Music Player. 

๐ฅณ I can play music in your Telegram Group's Voice Chat๐

โ๏ธ Use these buttons below to know more. ๐""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Source Code ๐", url="https://github.com/jattpawan/evilbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ฌ Group ๐ฌ", url="https://t.me/BLAC_USERBOT_GROUP"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Channel ๐ฃ", url="https://t.me/BLAC_USERBOT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ Close โ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**รชvilแบรธโ :** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ถ Search ๐ถ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "โ Close โ", callback_data="close"
                    )
                ]
            ]
        )
    )
