# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
import random
import traceback
from sys import version as pyver
from datetime import datetime
import os
import shlex
import textwrap
from typing import Tuple
import asyncio
import speedtest

from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from zika.helpers.basic import edit_or_reply
from zika.helpers.constants import WWW
from zika import app
from zika.helpers.PyroHelpers import SpeedConvert
from zika.modules.bot.inline import get_readable_time
from zika.helpers.adminHelpers import DEVS
from zika.helpers.PyroHelpers import ReplyCheck
from config import BOT_VER, CMD_HANDLER as cmd
from config import GROUP, BRANCH as branch
from zika import CMD_HELP, StartTime, app
from .help import add_command_help

modules = CMD_HELP

kopi = [
    "**Hadir bang** 😁",
    "**Hadir sayang** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]


@Client.on_message(filters.command("absen", ["."]) & filters.user(DEVS) & ~filters.me)
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))


@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(
    filters.command("aping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("zping", cmd) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    zika = await edit_or_reply(message, "**Mengecek Sinyal...**")
    await zika.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await zika.edit("**40% ████▒▒▒▒▒▒**")
    await zika.edit("**60% ██████▒▒▒▒**")
    await zika.edit("**80% ████████▒▒**")
    await zika.edit("**100% ██████████**")
    await zika.edit("**Completed!!**")
    await zika.edit("✨")
    await asyncio.sleep(2.5)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await zika.edit(
        f"**sɪᴀʀᴀʙ-ᴜsᴇʀʙᴏᴛ**\n"
        f"** ➠  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ➠  Aᴋᴛɪꜰ  :** "
        f"`{uptime}` \n"
        f"** ➠  Mᴀꜱᴛᴇʀ   :** {client.me.mention}" % (duration)
    )

@Client.on_message(filters.command("arab", cmd) & filters.me)
async def module_ping(client: Client, message: Message):
    cdm = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cdm) > 1:
        help_arg = " ".join(cdm[1:])
    elif not message.reply_to_message and len(cdm) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="ling")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id),
            )
        except BaseException:
            pass


@Client.on_message(
    filters.command("aping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("ping", cmd) & filters.me)
async def kping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"**sɪᴀʀᴀʙ-ᴜsᴇʀʙᴏᴛ** 🏓\n"
        f"**Pᴏɴɢ »** "
        f" `%sms` \n "
        f"**Aᴋᴛɪꜰ »** "
        f" `{uptime}` \n " % (duration)
    )
        
add_command_help(
    "speedtest",
    [
        ["dc", "Untuk melihat DC Telegram anda."],
        [
            f"speedtest `atau` {cmd}speed",
            "Untuk megetes Kecepatan Server anda.",
        ],
    ],
)


add_command_help(
    "ping",
    [
        ["ping", "Untuk Menunjukkan Ping Bot Anda."],
        ["aping", "Untuk Menunjukkan Ping Bot Anda ( Beda animasi doang )."],
    ],
)
