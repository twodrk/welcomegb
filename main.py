import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "BotNameHere",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

@bughunter0.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Hoşgeldin {message.from_user.mention} to {message.chat.username} ,  Burada olmandan mutlu oldum",chat_id=chatid)
	
@bughunter0.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Görüşürüz ,  {message.from_user.mention} , iyi günler dileğiyle",chat_id=chatid)
	
bughunter0.run()
