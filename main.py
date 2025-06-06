import os
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام علیرضا جان! ربات با موفقیت راه افتاد 🚀")

app = ApplicationBuilder().token(os.getenv("TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
