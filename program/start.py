from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Welcome {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/KOT_MUSIC_PLAYER_BOT) **𝗔𝗟𝗟𝗢𝗪𝗦 𝗬𝗢𝗨𝗥 𝗧𝗢 𝗣𝗟𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 𝗔𝗡𝗗 𝗩𝗜𝗗𝗘𝗢 𝗢𝗡 𝗚𝗥𝗢𝗨𝗣𝗦 𝗧𝗛𝗥𝗢𝗨𝗚𝗛 𝗧𝗛𝗘 𝗧𝗚 𝗩𝗜𝗗𝗘𝗢 𝗖𝗛𝗔𝗧!**

💡 **𝗙𝗜𝗡𝗗 𝗢𝗨𝗧 𝗔𝗟𝗟 𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗛𝗢𝗪 𝗧𝗛𝗘𝗬 𝗪𝗢𝗥𝗞 𝗕𝗬 𝗖𝗟𝗜𝗖𝗞𝗜𝗡𝗚 𝗢𝗡 𝗧𝗛𝗘 » 📚 𝗖𝗢𝗠𝗠𝗘𝗡𝗗𝗦 𝗕𝗨𝗧𝗧𝗢𝗡!**

🔖 **𝗧𝗢 𝗞𝗡𝗢𝗪 𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧, 𝗣𝗟𝗘𝗔𝗦𝗘 𝗖𝗟𝗜𝗖𝗞 𝗢𝗡 𝗧𝗛𝗘  » ❓ 𝗕𝗔𝗦𝗜𝗖 𝗚𝗨𝗜𝗗𝗘 𝗕𝗨𝗧𝗧𝗢𝗡! | 𝗕𝗢𝗧 𝗠𝗔𝗧𝗜𝗔𝗡𝗘𝗗/𝗖𝗥𝗘𝗔𝗧𝗘𝗥 𝗕�: @KOT_BOTS**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝗔𝗗𝗗 𝗠𝗘𝗛 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣➕",
                        url=f"https://t.me/KOT_MUSIC_PLAYER_BOT?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ 𝗕𝗔𝗦𝗜𝗖 𝗚𝗨𝗜𝗗𝗘", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 𝗖𝗢𝗠𝗠𝗘𝗡𝗗𝗦", callback_data="cbcmds"),
                    InlineKeyboardButton("❤️ 𝗗𝗢𝗡𝗔𝗧𝗘", url=f"https://t.me/KOT_FREE_DE_LA_HOYA_OFF"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 𝗕𝗢𝗧𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url=f"https://t.me/KOT_BOTS"
                    ),
                    InlineKeyboardButton(
                        "📣 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣", url=f"https://t.me/KOT_REPORS"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘", url="https://t.me/KOT_SOURCE_CODE"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣", url=f"https://t.me/KOT_REPORS"),
                InlineKeyboardButton(
                    "📣 𝗕𝗢𝗧𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url=f"https://t.me/KOT_BOTS"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/KOT_FREE_DE_LA_HOYA_OFF)\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 PyTgCalls version: `{pytover.__version__}`\n✨ Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing video & music on your Group's video chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
