import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام علیرضا جان! ربات با موفقیت راه افتاد 🎉")

app = ApplicationBuilder().token(os.getenv("TELE_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
