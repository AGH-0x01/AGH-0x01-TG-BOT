"""
CTF Telegram Bot — CtffTest_bot 
========================================================

OVERVIEW
- The bot never discloses flags.
- It returns the a response irrespective of the message input. However, the bot should not reveal any information related to the attacker unless the attacker proves their identity to the bot.
Flag10 = CTF{0p3n_S0urc3_1nt3ll1g3nc3}
""""
import os, base64
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()  # loads .env when running locally

BOT_TOKEN     = os.environ["BOT_TOKEN"]
FLAG2_POINTER = os.environ.get("FLAG_2_URL", "https://example.com/next.txt")  # dummy pointer
REFUSAL       = "I can’t share that information."

async def start(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "TBD"
    )

async def help_cmd(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Available: /start — and normal messages.")

async def handle_message(update: Update, _: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip()
    low  = text.lower()

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling(allowed_updates=Update.ALL_TYPES)  # polling is easiest to host anywhere

if __name__ == "__main__":
    main()
