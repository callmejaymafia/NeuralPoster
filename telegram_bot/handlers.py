import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from ai.providers import ai_generator


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Yoo 🥷
I'm your bot ⚒️
How can I help 😒
Check for /help 🥸
        """
    )


async def tweet_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)

    if not prompt:
        await update.message.reply_text("Usage: /tweet <what you want to post>")
        return

    system_prompt = "Write a concise, engaging tweet. Max 280 characters. Avoid using the sign — . Include nice emojis when appropriate. No hashtags unless necessary."
    user_prompt = f"Topic: {prompt}"

    tweet = await ai_generator(user_prompt, system_prompt, priority="fast")

    tweet = tweet.strip()

    context.user_data["pending_tweet"] = tweet

    await update.message.reply_text(
        f"📝 Draft Tweet:\n\n{tweet}\n\n"
        "Use /post_x to publish or /discard to cancel."
    )


async def post_x_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tweet = context.user_data.get("pending_tweet")
    if not tweet:
        await update.message.reply_text("No pending tweet to post. Use /tweet first.")
        return

    from platforms.x_platform import post_tweet

    try:
        tweet_url = await post_tweet(tweet)
        await update.message.reply_text(f"Tweet posted successfully! 🎉\n\n{tweet_url}")
        del context.user_data["pending_tweet"]
    except Exception as e:
        await update.message.reply_text(f"Failed to post tweet: {str(e)}")


async def discard_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if "pending_tweet" in context.user_data:
        del context.user_data["pending_tweet"]
        await update.message.reply_text("Tweet discarded 😔")
    else:
        await update.message.reply_text("No pending tweet to discard 😒")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Useful commands:

/start
/tweet
/post_x
/discard
/help
        """
    )
