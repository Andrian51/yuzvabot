import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from config import my_telegram_bot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Дарова чел.")


if __name__ == '__main__':
    application = ApplicationBuilder().token(my_telegram_bot).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    hello_handler = CommandHandler('hello', hello)
    application.add_handler(hello_handler)

    application.run_polling()
