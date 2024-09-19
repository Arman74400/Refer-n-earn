from .. import JN
from pyrogram import Client, enums, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from ..database import update_balance, collection
import asyncio
from config import all_platform

def increase_balance(user_id, amount):
    collection.update_one({'user_id': user_id}, {'$inc': {'balance': amount}})

def decrease_balance(user_id, amount):
    collection.update_one({'user_id': user_id}, {'$inc': {'balance': -amount}})

@JN.on_message((filters.regex("ᴅɪᴄᴇ ɢᴀᴍᴇ 🥳") | filters.command("dice")) & filters.private)
async def dice(bot, message):
    document = collection.find_one({"user_id": message.from_user.id})
    balance = document.get("balance")
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("1 "), KeyboardButton("3 ")],
        [KeyboardButton("5 "), KeyboardButton("10 ")],
        [KeyboardButton("15 "), KeyboardButton("20 ")],
        [KeyboardButton("📍ᴄᴀɴᴄᴇʟ ʙᴇᴛ📍")]
    ], resize_keyboard=True)
    keyboard2 = ReplyKeyboardMarkup([
        [KeyboardButton("1 "), KeyboardButton("2 ")],
        [KeyboardButton("3 "), KeyboardButton("4 ")],
        [KeyboardButton("5 "), KeyboardButton("6 ")],
        [KeyboardButton("📍ᴄᴀɴᴄᴇʟ ʙᴇᴛ📍")]
    ], resize_keyboard=True)

    msg1 = await JN.ask(message.from_user.id, "How much money you want to bet in INR format.", reply_markup=keyboard)
    if msg1.text == "📍ᴄᴀɴᴄᴇʟ ʙᴇᴛ📍":
        await message.reply_text("Bet canceled.", reply_markup=all_platform)
        return

    try:
        amount = float(msg1.text)
    except ValueError:
        await message.reply_text("Invalid amount. Please enter a valid number.", reply_markup=all_platform)
        return

    if balance < amount:
        await message.reply_text("Insufficient balance. Share With Your Friend's & Family And Earn Refer Bonus Easily ✨🤑.", reply_markup=all_platform)
        return

    msg2 = await JN.ask(message.from_user.id, "Choose number to bet", reply_markup=keyboard2)
    if msg2.text == "📍ᴄᴀɴᴄᴇʟ ʙᴇᴛ📍":
        await message.reply_text("Bet canceled.", reply_markup=all_platform)
        return

    try:
        bet_number = float(msg2.text)
    except ValueError:
        await message.reply_text("Invalid number. Please choose a valid number.", reply_markup=all_platform)
        return

    x = await bot.send_dice(message.chat.id)
    m = x.dice.value

    user_id = message.from_user.id
    if bet_number == int(m):
        increase_balance(user_id, amount)
        await message.reply_text(f"Hey {message.from_user.mention} you won the bet and got: {amount * 2}", reply_markup=all_platform, quote=True)
    else:
        decrease_balance(user_id, amount)
        await message.reply_text(f"Hey {message.from_user.mention} you lost the bet and lost: {amount}", reply_markup=all_platform, quote=True)

@JN.on_message((filters.regex("⚽️ ꜰᴏᴏᴛʙᴀʟʟ") | filters.command("football")) & filters.private)
async def football(bot, message):
    document = collection.find_one({"user_id": message.from_user.id})
    balance = document.get("balance")
    
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("1 "), KeyboardButton("3 ")],
        [KeyboardButton("5 "), KeyboardButton("10 ")],
        [KeyboardButton("15 "), KeyboardButton("20 ")],
        [KeyboardButton("📍ᴄᴀɴᴄᴇʟ ʙᴇᴛ📍")]
    ], resize_keyboard=True)

    msg1 = await JN.ask(message.from_user.id, "How much money you want to bet in INR format.", reply_markup=keyboard)
    if msg1.text == "📍ᴄᴀɴᴄᴇʟ ʙᴇᴛ📍":
        await message.reply_text("Bet canceled.", reply_markup=all_platform)
        return

    try:
        amount = float(msg1.text)
    except ValueError:
        await message.reply_text("Invalid amount. Please enter a valid number.", reply_markup=all_platform)
        return

    if balance < amount:
        await message.reply_text("Insufficient balance. Share With Your Friend's & Family And Earn Refer Bonus Easily ✨🤑.", reply_markup=all_platform)
        return

    # Roll the dice
    x = await bot.send_dice(message.chat.id, "⚽")
    m = x.dice.value

    user_id = message.from_user.id
    if m in [4, 5, 3]:  # Assuming a win condition for football dice
        increase_balance(user_id, amount)
        await message.reply_text(f"Hey {message.from_user.mention} you won the bet and got: {amount * 2}", reply_markup=all_platform, quote=True)
    else:
        decrease_balance(user_id, amount)
        await message.reply_text(f"Hey {message.from_user.mention} you lost the bet and lost: {amount}", reply_markup=all_platform, quote=True)
