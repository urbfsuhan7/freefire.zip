from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import os
import json

TOKEN = os.getenv("7992397959:AAFV08fCoHqIchevCGps334eD16ao9wB6RU")
player_data = {}

def handle_get_message(update: Update, context: CallbackContext):
    text = update.message.text.strip()
    if text.lower().startswith("get"):
        parts = text.split()
        if len(parts) == 2:
            uid = parts[1]
            info = player_data.get(uid)
            if info:
                gl = info['guild_leader']
                message = f"""\U0001F3AE *Free Fire Player Info*:
\U0001F464 Name: {info['name']}
\U0001F194 UID: {info['uid']}
\u2B50 Level: {info['level']}
\U0001F3C6 Rank: {info['rank']}
\U0001F30D Region: {info['region']}
\U0001F465 Guild: {info['guild']}
\U0001F4C5 Account Created: {info['creation_date']}
\U0001F551 Last Login: {info['last_login']}
\U0001F9D9 Character Used: {info['character_used']}
\U0001F48E Prime Level: {info['prime_level']}
\U0001F39F Booyah Pass: {info['boya_pass']} (Level {info['boya_pass_level']})
\U0001F7E2 Active: {"Yes" if info['is_active'] else "No"}

\U0001F451 *Guild Leader Info*:
\U0001F194 Leader UID: {gl['uid']}
\U0001F464 Leader Name: {gl['name']}
\u2B50 Level: {gl['level']}
\U0001F4C5 Created: {gl['creation_date']}
\U0001F551 Last Login: {gl['last_login']}
\U0001F4A0 Premium Level: {gl['premium_level']}
\U0001F39F Booyah Pass: {gl['boya_pass']} (Level {gl['boya_pass_level']})
\U0001F7E2 Active: {"Yes" if gl['is_active'] else "No"}
"""
                update.message.reply_text(message, parse_mode='Markdown')
            else:
                update.message.reply_text(f"❌ Player with UID {uid} not found.", parse_mode='Markdown')
        else:
            update.message.reply_text("⚠️ Format sahi bhejo: Get 12345678", parse_mode='Markdown')

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