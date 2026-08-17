import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters,
)

from responses import REPLIES, DEFAULT_REPLY, MATCH_MODE

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")


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


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message or not message.text:
        return

    reply = find_reply(message.text)

    if reply:
        await message.reply_text(reply)
    elif DEFAULT_REPLY:
        await message.reply_text(DEFAULT_REPLY)


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
