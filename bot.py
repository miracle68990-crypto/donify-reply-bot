import asyncio
import logging
import os
import random
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters,
)

from responses import REPLIES, DEFAULT_REPLY, MATCH_MODE, DEFAULT_REPLY_KEYWORDS

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Random delay range (seconds) before the bot replies, so responses don't
# look instant/bot-like. Adjust these two numbers to taste.
MIN_DELAY_SECONDS = 3
MAX_DELAY_SECONDS = 8


def find_reply(text: str):
    """Look through REPLIES and find a matching canned response."""
    if not text:
        return None

    text_check = text.lower()

    for trigger, reply in REPLIES.items():
        trigger_check = trigger.lower()

        if MATCH_MODE == "exact":
            if text_check.strip() == trigger_check:
                return reply
        else:  # "contains" mode (default)
            if trigger_check in text_check:
                return reply

    return None


def mentions_donify(text: str) -> bool:
    """True if the message contains any of the DEFAULT_REPLY_KEYWORDS."""
    text_check = text.lower()
    return any(kw.lower() in text_check for kw in DEFAULT_REPLY_KEYWORDS)


async def reply_with_delay(message, chat_id, context, text: str):
    """Show a 'typing...' indicator and wait a short random delay before
    sending the reply, so it looks more natural than an instant bot reply."""
    delay = random.uniform(MIN_DELAY_SECONDS, MAX_DELAY_SECONDS)

    try:
        await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    except Exception:
        pass  # non-critical if this fails

    await asyncio.sleep(delay)
    await message.reply_text(text)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message or not message.text:
        return

    reply = find_reply(message.text)

    if reply:
        await reply_with_delay(message, message.chat_id, context, reply)
    elif DEFAULT_REPLY and mentions_donify(message.text):
        # No specific trigger matched, but the message mentions Donify
        # (or a related keyword) -> send the generic fallback instead
        # of staying silent.
        await reply_with_delay(message, message.chat_id, context, DEFAULT_REPLY)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is up and running.")


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is not set.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot started. Listening for messages...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
