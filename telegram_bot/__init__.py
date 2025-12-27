from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_BOT_TOKEN
from .handlers import start, tweet_handler, post_x_handler, discard_handler, help


def bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("tweet", tweet_handler))
    app.add_handler(CommandHandler("post_x", post_x_handler))
    app.add_handler(CommandHandler("discard", discard_handler))
    app.run_polling()
