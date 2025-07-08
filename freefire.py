from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import os
import json

# ✅ Bot Token
TOKEN = os.getenv("7992397959:AAFV08fCoHqIchevCGps334eD16ao9wB6RU")

# 🧠 Player data will be loaded from JSON
player_data = {}

# 🔍 "Get" command handler
def handle_get_message(update: Update, context: CallbackContext):
    text = update.message.text.strip()
    if text.lower().startswith("get"):
        parts = text.split()
        if len(parts) == 2:
            uid = parts[1]
            info = player_data.get(uid)

            if info:
                gl = info['guild_leader']
                message = f"""
🎮 *Free Fire Player Info*:
👤 Name: {info['name']}
🆔 UID: {info['uid']}
⭐ Level: {info['level']}
🏆 Rank: {info['rank']}
🌍 Region: {info['region']}
👥 Guild: {info['guild']}
📅 Account Created: {info['creation_date']}
🕐 Last Login: {info['last_login']}
🧙 Character Used: {info['character_used']}
💎 Prime Level: {info['prime_level']}
🎟️ Booyah Pass: {info['boya_pass']} (Level {info['boya_pass_level']})
🟢 Active: {"Yes" if info['is_active'] else "No"}

👑 *Guild Leader Info*:
🆔 Leader UID: {gl['uid']}
👤 Leader Name: {gl['name']}
⭐ Level: {gl['level']}
📅 Created: {gl['creation_date']}
🕐 Last Login: {gl['last_login']}
💠 Premium Level: {gl['premium_level']}
🎟️ Booyah Pass: {gl['boya_pass']} (Level {gl['boya_pass_level']})
🟢 Active: {"Yes" if gl['is_active'] else "No"}
"""
                update.message.reply_text(message, parse_mode='Markdown')
            else:
                update.message.reply_text(f"❌ Player with UID {uid} not found.", parse_mode='Markdown')
        else:
            update.message.reply_text("⚠️ Format sahi bhejo: Get 12345678", parse_mode='Markdown')

# ✅ Start bot
def main():
    global player_data

    try:
        with open("data.json", "r") as f:
            player_data = json.load(f)
            print("📂 Data loaded from data.json")
    except FileNotFoundError:
        print("⚠️ data.json file not found. Please add player data.")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_get_message))
    print("🤖 Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()