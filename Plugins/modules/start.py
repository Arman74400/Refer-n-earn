from pyrogram import filters, Client
import asyncio
from .. import JN
from pyrogram.enums import ParseMode
from pyrogram.errors import UserNotParticipant, ChatWriteForbidden, ChatAdminRequired
from config import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ..database import collection, add_refer_balance, add_default_balance, is_new_user


# Force join handler

@JN.on_message(filters.command("start") & filters.private)
async def must_join_channel(bot: Client, msg):
    
    if not UPDATE_CHNL and not SUPPORT_GRP:
        return
    try:
        try:
            await bot.get_chat_member(UPDATE_CHNL, msg.from_user.id)
            await bot.get_chat_member(SUPPORT_GRP, msg.from_user.id)
            
            caption = f"Hello {msg.from_user.mention}, \nI'm {JN.mention}\n\n🏡 Welcome To UPI Giveaway Bot!\n\nʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ  ᴇᴀʀɴ ʙʏ ʀᴇꜰᴇʀ ʏᴏᴜʀ ꜰʀɪᴇɴᴅꜱ ᴀɴᴅ ᴀʟꜱᴏ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ʙʏ ʙᴇᴛꜱ .\n\nMaintained by:<a href='https://t.me/Ak74400/'>AK</a>"
            caption2 = f"Hello {msg.from_user.mention},\n\n ʜᴇʏ ʟᴏᴏᴋ ʟɪᴋᴇ ʏᴏᴜ ᴀʀᴇ ɴᴇᴡ ʜᴇʀᴇ ᴏɴᴇ ʟɪᴛᴛʟᴇ ɢɪꜰᴛ ꜰʀᴏᴍ ᴍᴇ ʏᴏᴜ ᴊᴜꜱᴛ ɢᴏᴛ +2 ₹ ᴀꜱ ʙᴏɴᴜꜱ.\n Maintained by:<a href='https://t.me/Ak74400/'>AK</a>"

            if is_new_user(msg.from_user.id):
                add_default_balance(msg.from_user.id)

                j = await msg.reply_sticker("CAACAgUAAxkDAAIIImYMPfDBC9C0hwEdm34oVxFYbAYLAAJrDgACIHkgVAjUFXHyK3urHgQ")
                await asyncio.sleep(1)
                await j.delete()
                await JN.send_photo(msg.chat.id, photo=start_img2, caption=caption, reply_markup=main_button)
                await JN.send_message(msg.chat.id, text="Hey you just got +2₹ in your account as a new user bonus")
                await JN.send_message(log_channel, text=f"🦋 #newuser 🦋,\n\n**ID** : `{msg.from_user.id}`\n**Name**: {msg.from_user.first_name}\n **refer by:** No one")
            else:
                j = await msg.reply_sticker("CAACAgUAAxkBAAECPc9mA9nqb8a0d0ziqad0mrNlleIXXAAC0w4AAudpIVTD64tNd-x1Xx4E")
                await asyncio.sleep(1)
                await j.delete()
                j = await msg.reply_sticker("CAACAgUAAxkBAAECPcpmA9bYkPLWQz9DGg0KL5tShE3QRwACrQ8AAutgIVRELBWrQpHOux4E")
                await asyncio.sleep(1)
                await j.delete()
                await JN.send_photo(msg.chat.id, photo=start_img2, caption=caption, reply_markup=main_button)
                
        except UserNotParticipant:
            # Generate dynamic buttons for channels
            links = [
                "https://t.me/Crypto_Loot_AK",  # Add actual links here
                "https://t.me/Looters_Money_Trick",
                "https://t.me/myank_Real_Earn",
                "https://t.me/Earning_Loots08",
                # Add more channel links as needed
            ]
            buttons = []
            
            # Adding rows of two buttons
            for i in range(0, len(links), 2):
                row = []
                for j in range(2):
                    if i + j < len(links):
                        row.append(InlineKeyboardButton(f"Channel {i+j+1}", url=links[i + j]))
                buttons.append(row)

            # Adding the 'Joined' button dynamically with bot's start link
            bot_username = (await bot.get_me()).username
            start_link = f"https://t.me/{bot_username}?start"
            buttons.append([InlineKeyboardButton("🔒 Claim", url=start_link)])

            try:
                await msg.reply_photo(
                    photo=START_IMG,
                    caption='»<b>👋 Hey There User Welcome To Bot !\n\n🛑 Must Join Total Channel To Use Our Bot\n\n💣 After Joining Click Claim </b>',
                    parse_mode=ParseMode.HTML,   
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                await msg.stop_propagation()
                  
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the UPDATE CHANNEL: {UPDATE_CHNL}!")
        print(f"Promote me as an admin in the SUPPORT_GRP: {SUPPORT_GRP}!")

@JN.on_message(filters.regex('〄 ᴍᴀɪɴ ᴍᴇɴᴜ 〄') & filters.private)
async def main_menu_handler(bot, message):
    
    caption = f"Hello {message.from_user.first_name},\n\n🏡 Welcome To UPI Giveaway Bot!\n\nʜᴇʀᴇ ʏᴏᴜ cᴀɴ  ᴇᴀʀɴ ʙʏ ʀᴇꜰᴇʀ ʏᴏᴜʀ ꜰʀɪᴇɴᴅꜱ ᴀɴᴅ ᴀʟꜱᴏ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ʙʏ ʙᴇᴛꜱ .\n\nMaintained by: <a href='https://t.me/Ak74400/'>AK</a>"
    
    await JN.send_photo(message.chat.id, photo=start_img2, caption=caption, reply_markup=main_button)
    await message.delete()
