"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User To upgrade to VIP \n Ask for Vip Plan On <a href='t.me/HeavenBotSupport'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/xdecoy")], 
        			[InlineKeyboardButton("Bot Support 🌎",url = "https://t.me/HeavenBotSupport"),
        			InlineKeyboardButton("Bot Update Channel ",url = "https://t.me/RestinHeavenBots")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """<b>Free Plan User \n To upgrade to VIP \n Ask for Vip Plan On <a href='t.me/HeavenBotSupport'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/xdecoy")], 
        			[InlineKeyboardButton("Bot Support 🌎",url = "https://t.me/HeavenBotSupport"),
        			InlineKeyboardButton("Bot Update Channel ",url = "https://t.me/RestinHeavenBots")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
