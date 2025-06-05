import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import openai

# توکن‌ها 🔐
TELEGRAM_TOKEN = "اینجا-توکن-ربات-تلگرام-رو-بذار"
OPENAI_API_KEY = "sk-اینجا-API-Key-OpenAI-رو-بذار"

openai.api_key = OPENAI_API_KEY

# هندل پیام کاربر 📩
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response['choices'][0]['message']['content']
    except Exception as e:
        bot_reply = f"❌ خطا: {e}"

    await update.message.reply_text(bot_reply)

# شروع ربات ▶️
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
